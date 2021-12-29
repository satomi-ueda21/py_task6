from search_word import search_keyword

#search_word関数テスト
def test_search_keyword():
  keyword = "ウールダスター"
  res = search_keyword(keyword=keyword)

  assert len(res["Items"]) >= 1
  assert res["Items"][0]["Item"]["itemUrl"]
