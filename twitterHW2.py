#EC500 HW 2
#Alex Fatyga

import keys
import tweepy

import io
import os
import re
import urllib.request as req

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

from datetime import datetime
# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)
# dd/mm/YY H:M:S
dt_string = now.strftime("%Y-%m-%d")
print("date = ", dt_string)	


def getMsgs(username):
	auth = tweepy.OAuthHandler(keys.key, keys.secretKey)
	auth.set_access_token(keys.accessToken, keys.accessTokenSecret)

	api = tweepy.API(auth)
#	for tweet in tweepy.Cursor(api.statuses_lookup, id='tweepy').items(10):
#		print(tweet.text)
#		print(tweet.created_at)

	for status in tweepy.Cursor(api.user_timeline,username).items(20):
    
		tweetDateTime = str(status.created_at)
		dateTime = tweetDateTime.split()
		if (dateTime[0] == dt_string):
			print(status.text)
			try:
				url = str(status.entities['media'][0]['media_url'])
				print(url)
				req.urlretrieve(url, "image_name.jpg")

			except (NameError, KeyError):        
				pass
			else: #where we would do vision ai and all that fun stuff
				print("not within the past day!")
				#if an image
			#Instantiates a client
			client = vision.ImageAnnotatorClient()

			#The name of the image file to annotate
			file_name = "image_name.jpg"

#			Loads the image into memory
			with io.open(file_name, 'rb') as image_file:
			   content = image_file.read()

			image = types.Image(content=content)

			# Performs label detection on the image file
			response = client.label_detection(image=image)
			labels = response.label_annotations

			print('Labels:')
			for label in labels:
			    print(label.description)





getMsgs("alexfatyga_")