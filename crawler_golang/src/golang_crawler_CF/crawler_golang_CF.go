package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"
)

func main() {
	url := "https://online.carrefour.com.tw/search?key=%E9%B1%88%E9%AD%9A%E9%A6%99%E7%B5%B2&categoryId="

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

	//remove (\), split by (ProductListModel":[), split by (,"ProductIds":), convert to json version
	replacer := strings.NewReplacer("\\", "")
	htmlSR := replacer.Replace(htmlS)
	htmlSRA := strings.Split(htmlSR, "ProductListModel\":[")
	htmlSRA2 := strings.Split(htmlSRA[1], "}],\"ProductIds\":")
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
	//for i := 0; i < nums; i++ {
	//	fmt.Printf("%s\n", jsonDict[i]["Name"])
	//}

	type Table struct {
		Name                 string
		ItemQtyPerPackFormat string
		Price                string
		Specification        string
	}

	var table = make([]Table, nums)
	for i := 0; i < nums; i++ {
		table[i].Name = jsonDict[i]["Name"].(string)
		table[i].ItemQtyPerPackFormat = jsonDict[i]["ItemQtyPerPackFormat"].(string)
		table[i].Price = jsonDict[i]["Price"].(string)
		table[i].Specification = jsonDict[i]["Specification"].(string)
	}

	for i := 0; i < nums; i++ {
		fmt.Printf("%+s\n", table[i].Name)
		fmt.Printf("%+s\n", table[i].ItemQtyPerPackFormat)
		fmt.Printf("%+s\n", table[i].Price)
		fmt.Printf("%+s\n", table[i].Specification)
		fmt.Printf("%s\n", "*******************************************************************************************************")
	}
}
