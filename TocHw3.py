# -*- coding: utf-8 -*-
#Name:林思潔
#Student ID: F74004062
#description:
# parse一個實價登錄列表，可以得到輸入的地區和路名及交易年月份的平均交易價格

import sys
import urllib2
import json
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

URL = sys.argv[1]
area =sys.argv[2]
road = sys.argv[3]
year = sys.argv[4]

content = urllib2.urlopen(URL).read()
json_string = json.loads(content)

count = 0
total_price = 0
lengh_of_json = len(json_string)

for i in range(lengh_of_json):
	if json_string[i][u'鄉鎮市區'] == area:
		if road in json_string[i][u'土地區段位置或建物區門牌']:
			if str(year) in str(json_string[i][u'交易年月']):
				count = count + 1
				total_price = total_price + int(json_string[i][u'總價元'])

avg_price = 0
if str(count) == '0':
	avg_price = 0
else:
	avg_price = total_price / count

print avg_price
