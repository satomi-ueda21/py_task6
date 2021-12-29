from search_price import search_price

#search_price関数テスト
def test_search_price():
  keyword = "ウールダスター"
  res = search_price(keyword=keyword)

  assert len(res['Products']) >= 1
  assert res["Products"][0]["Product"]["makerPageUrlPC"]