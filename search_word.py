import pprint
from typing import Counter
import requests
from oauth2client.service_account import ServiceAccountCredentials
import os
import pandas as pd
from time import sleep
from spread_sheet_manager import SpreadsheetManager
from dotenv import load_dotenv
load_dotenv() #環境変数のロード

SPREADSHEET_ID = os.environ["SPREADSHEET_ID"]
RAKUTEN_API_KEY = os.environ["RAKUTEN_API_KEY"]

def search_keyword():
  ss = SpreadsheetManager()
  ss.connect_by_sheetname(SPREADSHEET_ID, "keyword")
  key_df = ss.fetch_all_data_to_df()
  word_list = key_df["keyword"].values.tolist()
  url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'

  try:
    for word in word_list:
      payload = {
        'applicationId':RAKUTEN_API_KEY,
        'hits':30,
        'keyword':word,
        'page':1,
        'postageFlag':1,
        }
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
        item_dic = []
        counter = counter + 1
        item = i['Item']
        print('【No.】' + str(counter))
        print('【商品名】' + '￥' + str(item['itemName']))
        print('【商品価格】' + '￥' + str(item['itemPrice']) + "\n")
        item_dic.append({"No." : str(counter),
                        "商品名" : item['itemName'],
                        "商品コード" : item['itemCode'],
                        "商品価格" : item['itemPrice'],
                        "ジャンルID" : item['genreId'],
                        "URL" : item['itemUrl'],
                        "レビュー平均" : item['reviewAverage'],
                        "レビュー数" : item['reviewCount']
                        })
        # pprint.pprint(item_dic)

        # 書き込み
        ss.connect_by_sheetname(SPREADSHEET_ID, "item_list")
        ss.bulk_insert(item_dic)
        sleep(3)

    return resp

  except requests.exceptions.RequestException as e:
    print("リクエストエラー発生")
    print(e)
  except Exception as error:
    print("その他のエラー発生")
    print(error)


if __name__ == "__main__":
  #スプレッドシートから検索キーワードを読み込む
  # keyword = input("検索するキーワードを入力してください>>>")
  search_keyword()

