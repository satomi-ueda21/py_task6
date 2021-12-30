from typing import Counter
import requests
from time import sleep
import pandas as pd

def search_genre(keynumber:int):
  url = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?"
  payload = {
    "format" : "json",
    'applicationId':str(1033241985764370332),
    'hits':1,
    'genreId':keynumber,
    'page':1,
    'postageFlag':1,
  }

  try:
    r = requests.get(url, params=payload)
    resp = r.json()
    print (f"【ランキングタイトル】{resp['title']}")
    print ("===================================")
    csv_path = (f"./{resp['title']}.csv")
    df = pd.DataFrame(columns=["順位", "商品名", "価格"])

    counter = 0
    for i in resp['Items']:
      counter = counter + 1
      item = i['Item']
      print('【順位】' + str(item['rank']))
      print('【商品名】' + '￥' + str(item['itemName']))
      print('【価格】' + '￥' + str(item['itemPrice']) + "\n")
      df = df.append({"順位" : item['rank'],
                      "商品名" : item['itemName'],
                      "価格" : item['itemPrice']},
                      ignore_index=True)

    df.to_csv(csv_path, encoding="utf_8-sig")
    return resp

  except requests.exceptions.RequestException as e:
    print("リクエストエラー発生")
    print(e)
  except Exception as error:
    print("その他のエラー発生")
    print(error)

if __name__ == "__main__":
  keynumber = int(input("検索したいジャンルIDを入力してください>>>"))
  search_genre(keynumber)