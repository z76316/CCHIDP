package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"strconv"
	"strings"
)

func main() {
	url := "https://www.honestbee.tw/zh-TW/groceries/stores/american-wholesaler/search?q=%E7%89%9B%E5%A5%B6"

	resp, err := http.Get(url)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()
	html, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}
	htmlS := string(html)

	//remove (\), split by ({"products":[), split by (}],"categories"), convert to json version
	replacer := strings.NewReplacer("\\", "")
	htmlSR := replacer.Replace(htmlS)
	htmlSRA := strings.Split(htmlSR, "{\"products\":[")
	htmlSRA2 := strings.Split(htmlSRA[1], "}],\"categories\"")
	htmlSRA2m := htmlSRA2[0][1:]
	jsonArray := strings.Split(htmlSRA2m, "},{")

	nums := len(jsonArray)
	jsonB := make([][]byte, nums)
	for i := 0; i < nums; i++ {
		jsonArray[i] = "{" + jsonArray[i] + "}"
		jsonB[i] = []byte(jsonArray[i])
	}

	jsonDict := make([]map[string]interface{}, nums)
	jsonMap := make([]map[string]interface{}, nums)
	for i := 0; i < nums; i++ {
		var err2 = json.Unmarshal(jsonB[i], &jsonMap[i])
		if err2 != nil {
			panic(err2)
		}
		jsonDict[i] = jsonMap[i]
	}
	for i := 0; i < nums; i++ {
		fmt.Printf("%T\n", jsonDict[i]["size"])
	}

	type Table struct {
		Name                 string
		ItemQtyPerPackFormat string
		Price                string
		Specification        string
	}

	var table = make([]Table, nums)
	for i := 0; i < nums; i++ {
		table[i].Name = jsonDict[i]["title"].(string)
		table[i].ItemQtyPerPackFormat = strconv.FormatFloat(jsonDict[i]["amountPerUnit"].(float64), 'f', -1, 64)
		table[i].Price = strconv.FormatFloat(jsonDict[i]["price"].(float64), 'f', -1, 64)
		table[i].Specification = jsonDict[i]["size"].(string)
	}

	for i := 0; i < nums; i++ {
		fmt.Printf("%+s\n", table[i].Name)
		fmt.Printf("%+s\n", table[i].ItemQtyPerPackFormat)
		fmt.Printf("%+s\n", table[i].Price)
		fmt.Printf("%+s\n", table[i].Specification)
		fmt.Printf("%s\n", "*******************************************************************************************************")
	}
}
