### This code crawls the page of crickbuzz for live score. 
# If a wicket falls you will get 
import urlparse
import urllib2
import pdb
from bs4 import BeautifulSoup
from pprint import pprint
import time

## Authentication Code for message sending
from twilio.rest import TwilioRestClient

account_sid = ""
auth_token  = ""

client = TwilioRestClient(account_sid,auth_token)



#url = "https://www.google.com.hk/finance?q=0001&ei=yF14VYC4F4Wd0ASb64CoCw"
#url = "http://www.moneycontrol.com/india/stockpricequote/banks-private-sector/icicibank/ICI02"
url = "http://www.cricbuzz.com/live-cricket-scores/17007/pak-vs-wi-3rd-odi-pakistan-v-west-indies-in-uae-2016"

def WebCrawl(url):
    htmltext = urllib2.urlopen(url).read()
    soup = BeautifulSoup(htmltext,"html.parser")
    P = soup.find()
    #print P
    return soup
wks0=0
while(True):
	soup=WebCrawl(url)
	p1= soup.find("span", {"class":"cb-font-20 text-bold"}).text
	#p1 = soup.find("span", attrs={"id": "Bse_Prc_tick"}).text
	print p1
	p2=p1.split()
	runs = int(p2[1].split('/')[0])
	wks = int(p2[1].split('/')[1])
	print runs, wks
	
	#if (runs>110 or wks > wks0):
	if (wks > wks0):
		body1= "PAK runs = "+str(runs)+" and wkts= "+str(wks)
		message = client.messages.create(to="+919868633003", from_="+12059286849", body=body1)
	wks0=wks
	time.sleep(60)
#p = soup.find("meta", attrs={"itemprop": "price"})
#print p['content']

#divdata = soup.find('div', id='b_bidprice_qty').text
#print divdata
#p1 = soup.find("span", attrs={"id": "ref_164573760542896_l"}).text

#p1 = soup.find("span", attrs={"id": "Bse_Prc_tick"}).text
#print p1

'''
from twilio.rest import TwilioRestClient

account_sid = "ACad1e2e8130037e300dc20989a4ab8464"
auth_token  = "2946358a4dcd20d0b1f83f79d391ba15"

client = TwilioRestClient(account_sid,auth_token)

#message = client.messages.create(to="+919868633003", from="+919650690223", body="Hello dear")
message = client.messages.create(to="+919868633003", from_="+12059286849", body="Hello dear")
'''
