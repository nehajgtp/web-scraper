#start 'source tutorial-env/bin/activate' in terminal

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTweets(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), features="html.parser")
        count = 1
        for tweet in bsObj.find_all('p', 'content'):
            print(str(count) + '. ' + tweet.getText())
            count += 1
    except AttributeError as e:
        return None
    return tweet

tweets = getTweets("http://ethans_fake_twitter_site.surge.sh/")
if tweets == None:
    print("Tweets not found")
