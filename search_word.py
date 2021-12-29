import pprint
from typing import Counter
import requests
import gspread
from gspread import worksheet
from oauth2client.service_account import ServiceAccountCredentials
import os
import pandas as pd
from spread_sheet_manager import SpreadsheetManager
from dotenv import load_dotenv
load_dotenv() #環境変数のロード

SHEET_NAME = "テスト"
SPREADSHEET_ID = os.environ["SPREADSHEET_ID"]

def search_keyword():
  url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
  payload = {
    'applicationId':str(1033241985764370332),
    'hits':10,
    'keyword':keyword,
    'page':1,
    'postageFlag':1,
    }

  ss = SpreadsheetManager()
  ss.connect_by_sheetname(SPREADSHEET_ID, "keyword")
  key_df = ss.fetch_all_data_to_df()
  word_list = key_df["keyword"].values.tolist()

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
    # pprint.pprint(resp)

    counter = 0
    for i in resp['Items']:
      counter = counter + 1
      item = i['Item']
      print('【No.】' + str(counter))
      print('【商品名】' + '￥' + str(item['itemName']))
      print('【商品価格】' + '￥' + str(item['itemPrice']) + "\n")
    return resp

  except requests.exceptions.RequestException as e:
    print("リクエストエラー発生")
    print(e)
  except Exception as error:
    print("その他のリクエストエラー発生")
    print(error)



if __name__ == "__main__":
  #スプレッドシートから検索キーワードを読み込む
  # keyword = input("検索するキーワードを入力してください>>>")
  search_keyword()

