from bs4 import BeautifulSoup
import requests
import sys

url = 'https://twitter.com/search?q=%23bangkokbombing%20since%3A2015-08-10%20until%3A2015-09-30&src=typd&lang=en'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
r = requests.get(url, headers=headers)
data = r.text.encode('utf-8')
soup = BeautifulSoup(data, "html.parser")

name = soup('strong', {'class': 'fullname js-action-profile-name show-popup-with-id'})
username = name[0].contents[0]

#To find all usernames this possible when len(name[i]) >0 i.e one element
usernames = [nm.contents[0] for nm in name if len(nm)>0]

handle = soup('span', {'class': 'username js-action-profile-name'})
userhandle = handle[0].contents[1].contents[0]
#To find all userhandles. We need each handle length ==2
userhandles = [handle[i].contents[1].contents[0] for i in range(len(handle)) if len(handle[i])>1]


#link = soup('a', {'class': 'tweet-timestamp js-permalink js-nav js-tooltip'})
#url = link[0]
link = soup('a', {'class': 'tweet-timestamp js-permalink js-nav js-tooltip'})
url = link[0]["href"]
#To find all links
phrase="href"
urls= [link[i][phrase] for i in range(len(link)) if len(link[i][phrase])>0]
# To print timings. For timestamps other field will be accessed
phrase="title"
url_times= [link[i][phrase] for i in range(len(link)) if len(link[i][phrase])>0]


# Iterate over all links and find urls
#links = soup('a', {'class': 'tweet-timestamp js-permalink js-nav js-tooltip'})
#urls = [link["href"] for link in links]

messagetext = soup('p', {'class': 'TweetTextSize js-tweet-text tweet-text'})
message = messagetext[0].contents[0]
# inorder to print message in one line we use replace('\n',' ') in the text
#message = messagetext[0].contents[0]
#To print all the messages
messages = [messagetext[i].contents[0] for i in range(len(messagetext)) if len(messagetext[i])> 0]
## Replace new line and encode (utf-8)
#messages1 = [msg.replace('\n',' ') for msg in messages]
messages1 = [" ".join(msg.encode('utf-8').split()) for msg in messages]


retweets = soup('button', {'class': 'ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet'})
#retweetcount = retweets[0]
retweetcount = retweets[0].contents[3].contents[1].contents[1].string
#retweetcount = retweets[0].find_all('span', class_='ProfileTweet-actionCountForPresentation')[0].string

## All retweets count
retweetcounts = [rtc.find_all('span', class_='ProfileTweet-actionCountForPresentation')[0].string for rtc in retweets]

favorites = soup('button', {'class': 'ProfileTweet-actionButtonUndo u-linkClean js-actionButton js-actionFavorite'})
#favcount = favorites[0].contents[3].contents[1].contents[1].string
favcount = favorites[0].find_all('span', class_='ProfileTweet-actionCountForPresentation')[0].string

## All favorites count
favcounts = [fvc.find_all('span', class_= 'ProfileTweet-actionCountForPresentation')[0].string for fvc in favorites]


print (username, "\n", "@", userhandle, "\n", "\n", url, "\n", "\n", message, "\n", "\n", retweetcount, "\n", "\n", favcount) #extra linebreaks for ease of reading

import datetime
from datetime import timedelta
#%y  Year without century as a zero-padded decimal number.   00, 01, ..., 99  
#%Y  Year with century as a decimal number.  1970, 1988, 2001, 2013 

tweets = soup.find_all('li', 'js-stream-item')
tweet_text = soup.find_all('p', 'js-tweet-text')
tweet_timestamps = soup.find_all('a', 'tweet-timestamp')
tweet_links = soup.find_all('a', 'js-permalink')
for i in range(0, len(tweet_text)):
	#text1 = tweet_text[i].contents[0].encode('utf-8').lower()
	#text= " ".join(text1.split())
	text1 = tweets[i].get_text().encode('ascii', 'ignore').lower()
	text= " ".join(text1.split())                                        
	timestamp = datetime.datetime.strptime(tweet_timestamps[i]['title'], '%I:%M %p - %d %b %Y')
	link = 'https://twitter.com' + tweet_links[i]['href']
	#disp_str = (usernames[i]+" "+ "@"+userhandles[i]+" "+ text +" "+" "+tweet_timestamps[i]['title']+" "+timestamp+" "+link)
	print (usernames[i]," ", "@",userhandles[i]," ", text ," ",tweet_timestamps[i]['title']," ",timestamp," ",link)
	#if datetime.datetime.now() - timestamp > timedelta(hours=4):
	if (datetime.datetime.now() - timestamp).total_seconds() < timedelta(hours=300).total_seconds():
		if text.find('modi') or text.find('modi') or text.find('gov'):
			print 'Found a tweet on Modi governement'





