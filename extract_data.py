import json
with open('twitterData.json') as json_data:
    jsonData = json.load(json_data)

#get dates of tweets
for i in jsonData:
    print(i['date'])
