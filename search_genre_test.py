from search_genre import search_genre

def test_search_genre():
  keynumber = 100283
  res = search_genre(keynumber=keynumber)

  assert len(res['Items']) >= 1
  assert res["Items"][0]["Item"]["itemUrl"]