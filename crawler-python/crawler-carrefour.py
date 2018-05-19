# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import json
import urllib

class CarrefourObject():
	def __init__(self, Name, ItemQtyPerPackFormat, Price, Specification):
		self.Name = Name
		self.ItemQtyPerPackFormat = ItemQtyPerPackFormat #1入
		self.Price = Price
		self.Specification = Specification #125g克

class CarrefourSearch():

	def __init__(self, searchKeyWord):
		self.searchKeyWord = searchKeyWord

	def getSourceStr(self):

		searchKeyWord_transform = urllib.quote(self.searchKeyWord)
		url = "https://online.carrefour.com.tw/search?key=" + searchKeyWord_transform
		r = requests.get(url)

		sourceStr = r.content
		return sourceStr

	def getJsonList(self):

		sourceStr2 = self.getSourceStr().replace('\\', '')

		start = sourceStr2.find('"ProductListModel":[')
		end = sourceStr2.find('],"ProductIds"')

		str1 = sourceStr2[start: end]

		strList = str1.split('{"Id"')

		num = len(strList)
		lastIndex = num - 1
		strList2 = []
		for i in range(num):
			if i != 0:
				x = '{"id"' + strList[i]

				if i == lastIndex:
					x = x 
				else:
					x = x[:-1]

				strList2.append(x)
		jsonList = [json.loads(x) for x in strList2]
		return jsonList

	def getObjectList(self):

		# json to onject
		carrefourObject_list = [
									CarrefourObject(
														json['Name'], 
														json['ItemQtyPerPackFormat'], 
														json['Price'], 
														json['Specification']
													) 
									for json in self.getJsonList()
								]

		return carrefourObject_list


a = CarrefourSearch('汽水')
b = a.getObjectList()




something = b
# print "----------------------------------------content--------------------------------------------------"
# print something
# print "----------------------------------------type-----------------------------------------------------"
print type(something)
print len(something)

for x in something:
	print "----------------------------------------content--------------------------------------------------"
	print x.Name
	print x.ItemQtyPerPackFormat
	print x.Price
	print x.Specification

