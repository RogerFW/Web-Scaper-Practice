import requests
from bs4 import BeautifulSoup
import json

url = 'http://ethans_fake_twitter_site.surge.sh/'
response = requests.get(url)
content = BeautifulSoup(response.content,"html.parser")

#print(content)

tweet = content.findAll('p', attrs={"class": "content"}, text=True)

#print(tweet)

for tweet in content.findAll('p', attrs={"class": "content"}):
    print(tweet.text.encode('utf-8'))

tweetObject = {
        "author": "JimmyFallon",
        "date": "02/28/2018",
        "tweet": "Don't miss tonight's show!",
        "likes": "250",
        "shares": "1000"
    }

tweetArr = []
for tweet in content.findAll('div', attrs={"class": "tweetcontainer"}):
    tweetObject = {
        "author": "JimmyFallon",
        "date": "02/28/2018",
        "tweet": "Don't miss tonight's show!",
        "likes": "250",
        "shares": "1000"
    }
    tweetArr.append(tweetObject)
with open('twitterData.json', 'w') as outfile:
    json.dump(tweetArr, outfile)
    
with open('twitterData.json') as json_data:
    jsonData = json.load(json_data)
    
for i in jsonData:
    print(i['date'])
    
for i in jsonData:
    if "obama" in i['tweet'].lower():
        print(i)
