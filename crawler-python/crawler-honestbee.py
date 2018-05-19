# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import json

url = "https://www.honestbee.tw/zh-TW/groceries/stores/american-wholesaler/search?q=%E9%9B%9E%E7%B2%BE"
r = requests.get(url)

sourceStr = r.content
start = sourceStr.find('{"products":[')
end = sourceStr.find('}],"categories"')
str1 = sourceStr[start: end]
strList = str1.split('{"id"')

num = len(strList)
lastIndex = num - 1

strList2 = []
for i in range(num):
	if i != 0:
		x = '{"id"' + strList[i]

		if i == lastIndex:
			x = x + '}'
		else:
			x = x[:-1]

		strList2.append(x)
			
		
	

jsonList = [json.loads(x) for x in strList2]


class HonestbeeObject():
	def __init__(self, title, amountPerUnit, price, size):
		self.title = title
		self.amountPerUnit = amountPerUnit #1入
		self.price = price
		self.size = size #125g克
		

# #json to onject
honestbeeObjectList = [
							HonestbeeObject(
												json['title'], 
												json['amountPerUnit'], 
												json['price'], 
												json['size']
											) 
							for json in jsonList
						]



something = honestbeeObjectList
# print "----------------------------------------content--------------------------------------------------"
# print something["title"]
# print "----------------------------------------type-----------------------------------------------------"
print type(something)
print len(something)

for x in something: 
	print "---------------------------------------------------------------------------------------------"
	print x.title, x.price, x.size

