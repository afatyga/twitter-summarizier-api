#EC500 HW 2
#Alex Fatyga

import keys
import tweepy

import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

def getMsgs(username):
	auth = tweepy.OAuthHandler(keys.key, keys.secretKey)
	auth.set_access_token(keys.accessToken, keys.accessTokenSecret)

	api = tweepy.API(auth)
#	for tweet in tweepy.Cursor(api.search, q='tweepy').items(10):
#		print(tweet.text)
#		print(tweet.created_at)
	for status in tweepy.Cursor(api.user_timeline,username).items(20):
    # process status here
		print(status.text)
		try:
			print(status.entities['media'][0]['media_url'])
		except (NameError, KeyError):             #we dont want to have any entries without the media_url so lets do nothing
			pass
		else: #where we would do vision ai and all that fun stuff
			print("\nah")
				#if an image
			#Instantiates a client
#			client = vision.ImageAnnotatorClient()

			#The name of the image file to annotate
#			file_name = (status.entities['media'][0]['media_url'])

#			Loads the image into memory
#			with io.open(file_name, 'rb') as image_file:
#			   content = image_file.read()

#			image = types.Image(content=content)

			# Performs label detection on the image file
#			response = client.label_detection(image=image)
#			labels = response.label_annotations

#			print('Labels:')
#			for label in labels:
#			    print(label.description)





getMsgs("alexfatyga_")