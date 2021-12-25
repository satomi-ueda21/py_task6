import csv
import sys
import codecs
import math
import random
from typing import Counter
import requests
from time import sleep
import re

serch_keyword = input("検索する商品名を入力してください>>>")

url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
payload = {
  'applicationId':str(1033241985764370332),
  'hits':30,
  'keyword':serch_keyword,
  'page':1,
  'postageFlag':1,
  }

r = requests.get(url, params=payload)
resp = r.json()
total = int(resp['count'])
Max = total/30 + 1
print (f"【num of item】{total}")
print (f"【num of page】{Max}")
print ("===================================")

counter = 0
for i in resp['Items']:
  counter = counter + 1
  item = i['Item']
  name = item['itemName']
  print('【No.】' + str(counter))
  print('【Name】' + str(name[:30].encode('utf-8_sig')) + '...')
  print('【Price】' + '￥' + str(item['itemPrice']))
  print('【URL】' + item['itemUrl'])
  print('【shop】' + item['shopName'])
  print ('【text】' + item['itemCaption'])
