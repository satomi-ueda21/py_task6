import csv
import sys
import codecs
import math
import random
from typing import Counter
import requests
from time import sleep

def search_keyword(keyword:str):
  url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
  payload = {
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
    for i in resp['Items']:
      counter = counter + 1
      item = i['Item']
      print('【No.】' + str(counter))
      print('【商品名】' + '￥' + str(item['itemName']))
      print('【商品価格】' + '￥' + str(item['itemPrice']) + "\n")

  except requests.exceptions.RequestException as e:
    print("リクエストエラー発生")
    print(e)
  except Exception as error:
    print("その他のリクエストエラー発生")
    print(error)



if __name__ == "__main__":
  keyword = input("検索するキーワードを入力してください>>>")
  search_keyword(keyword)

