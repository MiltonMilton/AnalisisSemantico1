import requests

SPOTLIGHT_ENDPOINT = "http://api.dbpedia-spotlight.org/en/annotate"
class SpotLight:
    def getResources(self, text):
        result = requests.get(SPOTLIGHT_ENDPOINT,params=text)

        return result.json()