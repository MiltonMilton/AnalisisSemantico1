import json
import requests

subscriptionKey = "5d91fb8e436c448ebb3988df2a4c51d9"
customConfigId = "1597404721"
searchTerm = "python bing api 2018"

url = 'https://api.cognitive.microsoft.com/bingcustomsearch/v7.0/search?q=' + searchTerm + '&customconfig=' + customConfigId
r = requests.get(url, headers={'Ocp-Apim-Subscription-Key': subscriptionKey})
print r.content
