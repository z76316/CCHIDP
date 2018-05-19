# -*- coding: UTF-8 -*-
import ast
import json


str1 = '{"Id":809,"PictureUrl":"https://carrefoureccdn.azureedge.net/content/images/thumbs/0004716_250.jpeg","Name":"北海鱈魚香絲","XingHao":null,"SeName":"/1420301700101?kw=鱈魚香絲u0026pi=0","SubTitle":null,"ActiveBeginTime":null,"ActiveEndTime":null,"ActiveName":null,"AttributeValueId":0,"ActiveBackColor":null,"ActiveFontSize":0,"ActiveUrl":null,"UnitCode":null,"ItemQtyPerPack":1,"ItemQtyPerPackFormat":"1入","ProductVolume":null,"SpecialPrice":"","Price":"64","ActivityPrice":"","BonusCount":null,"ShortDescription":null,"ProductOperation":{"ItemQtyPerPack":0,"MaxNumberOnSale":0,"IsQuickShippingModel":true,"StockQuantity":null,"IsPreOrderShippingMode":false,"IsOffIslandMode":true,"IsCommonOrder":true,"Id":0},"PromotionAreaType":null,"DisplayId":0,"HomePictureUrl":null,"QucikShippingProductListPicUrl":"https://carrefoureccdn.azureedge.net/content/images/thumbs/0167639.png","SpecialStoreProductListPicUrl":"","OffIslandProductListPicUrl":null,"PromotionProductPicUrl":"","ProductNumShow":null,"IsWish":false,"Specification":"125g克"}'
str2 = str1.replace('null', 'None')

str3 = str2.replace('false', 'False')


d = json.loads(str1)
print d['Id']
