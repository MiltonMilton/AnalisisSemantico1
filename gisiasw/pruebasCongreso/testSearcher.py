from gisiasw.pruebasCongreso.searcher import Searcher

s = Searcher()

keys = ["languague", "python"]
n = 10
engine = "google"

r = s.search(keys,n,engine)
print r
