#start '$ source tutorial-env/bin/activate' in terminal
#then type '$ python parsedata.py'

import urllib.request
from bs4 import BeautifulSoup
import json

url = "http://ethans_fake_twitter_site.surge.sh/"

#download the URL and extract the content to the variable html
request = urllib.request.Request(url)
html = urllib.request.urlopen(request).read()

#pass the HTML to Beautifulsoup.
tweetdeck = BeautifulSoup(html,'html.parser')

#go into tweetdeck and get every a element in it which has a class "tweetcontainer"
tweets = tweetdeck.find_all('div', 'tweetcontainer')

#from each tweet extract info about tweet
tweetArr = []
for tweet in tweets:
    tweetObject = {
    "author": tweet.find('h2', 'author').text,
    "date": tweet.find('h5', 'dateTime').text,
    "tweet": tweet.find('p', 'content').text,
    "likes": tweet.find('p', 'likes').text,
    "shares": tweet.find('p', 'shares').text
    }
    tweetArr.append(tweetObject)
    print(tweetObject)

with open('twitterData.json', 'w') as outfile:
    json.dump(tweetArr, outfile)
