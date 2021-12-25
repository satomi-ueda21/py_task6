import csv
import sys
import codecs
import math
import random
from typing import Counter
import requests
from time import sleep
import re
import pprint

def search_keyword(keyword:str):
  url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
  payload = {
    'applicationId':str(1033241985764370332),
    'hits':10,
    'keyword':keyword,
    'page':1,
    'postageFlag':1,
    }

  r = requests.get(url, params=payload)
  resp = r.json()
  #price_resp = search_price(keyword)
  # print(resp)

  total = int(resp['count'])
  Max = total/30 + 1
  print (f"【num of item】{total}")
  print (f"【num of page】{Max}")
  print ("===================================")

  counter = 0
  for i in resp['Items']:
    counter = counter + 1
    item = i['Item']
    payment = search_price(item['itemCode'])
    print(item['itemCode'])
    print('【No.】' + str(counter))
    # print('【Name】' + str(name[:30].encode('utf-8_sig')) + '...')
    print('【商品名】' + '￥' + str(item['itemName']))
    # print('【商品名】' + '￥' + str(payment['productName']))
    # print('【商品価格】' + '￥' + str(item['itemPrice']))
    # print('【最安値】' + '￥' + str(payment['minPrice']))
    # print('【最高値】' + '￥' + str(payment['maxPrice']))
    # print('【URL】' + item['itemUrl'])
    # print('【shop】' + item['shopName'])
    # print ('【text】' + item['itemCaption'])

def search_price(key:str):
  url = "https://app.rakuten.co.jp/services/api/Product/Search/20170426?"
  payload = {
    "format" : "json",
    'applicationId':str(1033241985764370332),
    'hits':30,
    'productId':key,
    'page':1,
    'postageFlag':1,
  }

  r = requests.get(url, params=payload)
  return r.json()

if __name__ == "__main__":
  keyword = input("検索するキーワードを入力してください>>>")
  search_keyword(keyword)

