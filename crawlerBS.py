# Use BeautifulSoup and urllib
import urllib2
from bs4 import BeautifulSoup
import unicodedata
import requests
import urllib

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Google Chrome')]
var = "ArvindKejriwal"
# var = raw_input("Enter your Twitter id: ")
print "Tweets of", var
f = open(var + ".txt", "w")
url = "https://twitter.com/" + var
ur = urllib.urlopen(url)
# ur = opener.open(url).read()
# ur=requests.get(url).text.encode('utf-8')
soup = BeautifulSoup(ur, "html.parser")
what = soup.get_text()
print soup.title.string
f.write("%s\n" % (soup.title.string))
z = ""
for item in soup.find_all('p', {'class': 'TweetTextSize TweetTextSize--16px js-tweet-text tweet-text'}):
    try:
        item = item.text.lower().rstrip()
        print item
        new_str = unicodedata.normalize("NFKD", item)
        z = z + new_str
        f.write(z + "\n\n")
        z = ""
    except:
        pass
f.close()
