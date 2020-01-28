import keys
import tweepy
def getMsgs(username):
	auth = tweepy.OAuthHandler(keys.key, keys.secretKey)
	auth.set_access_token(keys.accessToken, keys.accessTokenSecret)

	api = tweepy.API(auth)
	for tweet in tweepy.Cursor(api.search, q='tweepy').items(10):
		print(tweet.text)

#	public_tweets = api.home_timeline()
#	for tweet in public_tweets:
#		print(tweet.text)


getMsgs("afatyga")