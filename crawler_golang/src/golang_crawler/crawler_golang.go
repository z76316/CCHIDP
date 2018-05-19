package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"
)

func main() {
	url := "https://online.carrefour.com.tw/search?key=%E9%B1%88%E9%AD%9A%E9%A6%99%E7%B5%B2&categoryId="
	//fmt.Printf("HTML code of %s ...\n", url)
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
	//fmt.Printf("%s\n", html)
	//fmt.Printf("%T\n", html)

	//remove (\) and (") version
	//replacer := strings.NewReplacer("\\", "", "\"", "")
	//htmlSR := replacer.Replace(htmlS)
	//fmt.Printf("%s\n", htmlSR)

	//split by ("Name\":\")
	//htmlSArray := strings.Split(htmlS, "\"Name\\\":\\\"")
	//fmt.Printf("%s\n", htmlSArray[1])

	//remove (\), split by (ProductListModel":[), split by (,"ProductIds":), convert to json version
	replacer := strings.NewReplacer("\\", "")
	htmlSR := replacer.Replace(htmlS)
	htmlSRA := strings.Split(htmlSR, "ProductListModel\":[")
	htmlSRA2 := strings.Split(htmlSRA[1], "}],\"ProductIds\":")
	htmlSRA2m := htmlSRA2[0][1:]
	jsonArray := strings.Split(htmlSRA2m, "},{")

	for i := 0; i < len(jsonArray); i++ {
		jsonArray[i] = "{" + jsonArray[i] + "}"
	}
	fmt.Printf("%s\n", jsonArray[0])
}
