import tweepy
from tweepy.auth import OAuthHandler, AppAuthHandler

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

my_info = api.me()
friends_ids = []
for friend_id in tweepy.Cursor(api.friends_ids, user_id=my_info.id).items():
	friends_ids.append(friend_id)
for i in range(0, len(friends_ids), 100):
	for user in api.lookup_users(user_ids=friends_ids[i:i+100]):
		print unicode(user.name) + " ::: @" + unicode(user.screen_name)
