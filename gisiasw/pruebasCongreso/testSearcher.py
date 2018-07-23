from gisiasw.pruebasCongreso.searcher import Searcher

s = Searcher()

keys = ["languague", "python"]
n = 10
engine = "bing"

r = s.search(keys,engine,n)
print r
