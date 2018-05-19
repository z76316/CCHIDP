# -*- coding: UTF-8 -*-
import urllib



searchKeyWord = '汽水'
test = urllib.quote(searchKeyWord)
url = "https://www.honestbee.tw/zh-TW/groceries/stores/american-wholesaler/search?q=" + test
print type(test)