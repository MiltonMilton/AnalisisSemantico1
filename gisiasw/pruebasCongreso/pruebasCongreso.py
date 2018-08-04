from entityRecognizer import EntityRecognizer

er = EntityRecognizer()

url = "https://www.analyticsvidhya.com/blog/2017/09/common-machine-learning-algorithms/"

a = er.recognizeAndCheckSynset2(url)

for i in a: 
    print i.id + " rs " + str(i.relevance_score) 