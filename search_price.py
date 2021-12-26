import csv
import sys
import codecs
import math
import random
from typing import Counter
import requests
from time import sleep

def search_price(keyword:str):
  url = "https://app.rakuten.co.jp/services/api/Product/Search/20170426?"
  payload = {
    "format" : "json",
    'applicationId':str(1033241985764370332),
    'hits':30,
    'keyword':keyword,
    'page':1,
    'postageFlag':1,
  }

  try:
    r = requests.get(url, params=payload)
    resp = r.json()
    total = int(resp['count'])
    if total > 30:
      Max = total/30 + 1
    else:
      Max = 1
    print (f"【num of item】{total}")
    print (f"【num of page】{Max}")
    print ("===================================")

    counter = 0
    for i in resp['Products']:
      counter = counter + 1
      item = i['Product']
      print('【No.】' + str(counter))
      print('【商品名】' + str(item['productName']))
      print('【最安値】' + '￥' + str(item['minPrice']))
      print('【最高値】' + '￥' + str(item['maxPrice'])  + "\n")

  except requests.exceptions.RequestException as e:
    print("リクエストエラー発生")
    print(e)
  except Exception as error:
    print("その他のリクエストエラー発生")
    print(error)

if __name__ == "__main__":
  keyword = input("最安値と最高値を検索する商品名を入力してください>>>")
  search_price(keyword)