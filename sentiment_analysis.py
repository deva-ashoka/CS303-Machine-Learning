import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from textblob import TextBlob
import io
 
#consumer_key='scQwhMkuP4cWkc5IUVLVA0ott'
#consumer_secret='Your Consumer Secret'
 
#access_token='Your Access Token'
#access_secret='Your Access Secret'

access_token = "243588726-jVHiUEmarkClphqHKpk6S7aPYK6aUTOLoQ0Mu2AU"
access_secret = "Xvu0pbNxliD6XbiZ8CNGAWdjVSbGldHdylwQpj20nkpyH"
consumer_key = "scQwhMkuP4cWkc5IUVLVA0ott"
consumer_secret = "vyBDAlpxdkuGZzD1A7or3UJDQ3Z4FmiuHnEJ5I5zWEFAvWUFy1"

 
auth=OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
 
api=tweepy.API(auth)
fw=open("./sentiment.txt","w")
class Listener(StreamListener):
 
    def on_data(self, raw_data):
        tweet= raw_data.split('text":')[1].split('","source"')[0]
        pol= str(TextBlob(tweet).polarity)
        full_tweet=tweet+" : "+pol
        fw.write(full_tweet+"\n")                                        #write the data to a file called sentiment.txt
        print full_tweet
    def on_error(self, status_code):
        print "Error :",status_code
 
 
choice=raw_input("Enter the choice: ")                                   #Enter the term which is to be searched in the streaming tweets
tweets=Stream(auth,Listener())
tweets.filter(track=[choice])
fw.close()
