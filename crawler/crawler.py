# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import json

url = "https://online.carrefour.com.tw/search?key=%E9%B1%88%E9%AD%9A%E9%A6%99%E7%B5%B2&categoryId="
r = requests.get(url)
# print r.content


soup = BeautifulSoup(r.content)
# print soup


# links = soup.find_all("a")
# for link in links:
	# print link.get("href")

g_data = soup.find_all("script", {"type": "text/javascript"})
print "**********************************************************************************************"


productInfo_bsTag = g_data[9]
productInfo_bsNavigableString = productInfo_bsTag.string # tag to NavigableString
productInfo_bsStr = productInfo_bsNavigableString.encode('utf8') # unicode to str
productInfo_bsStr_remove_backslash = productInfo_bsStr.replace('\\', '') #remove \

infoList = re.findall(r'\[(.*?)\]', productInfo_bsStr_remove_backslash) # retrieve product info, [str]
info = infoList[0] # str

product_str_List = info.split('},{') # get products list, [str]

product_str_List_forJson = []
for x in product_str_List:

	if x[0] != '{': 
		x = '{' + x

	if x[-1] != '}': 
		x = x + '}'

	# print x
	product_str_List_forJson.append(x)



product_dict_list = [json.loads(x) for x in product_str_List_forJson]



class CarrefourObject():
	def __init__(self, Name, ItemQtyPerPackFormat, Price, Specification):
		self.Name = Name
		self.ItemQtyPerPackFormat = ItemQtyPerPackFormat #1入
		self.Price = Price
		self.Specification = Specification #125g克
		


carrefourObject_list = [
							CarrefourObject(
												product_dic['Name'], 
												product_dic['ItemQtyPerPackFormat'], 
												product_dic['Price'], 
												product_dic['Specification']
											) 
							for product_dic in product_dict_list
						]



# something = carrefourObject_list
# print "----------------------------------------content--------------------------------------------------"
# print something
# print "----------------------------------------type-----------------------------------------------------"
# print type(something)
# print len(something)

for carrefourObject in carrefourObject_list: 
	print carrefourObject.Name

