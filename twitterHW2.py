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
dt_string = now.strftime("%Y-%m-%d")

def getImgDescription(file_name):
	client = vision.ImageAnnotatorClient()

#Loads the image into memory
	file_name = os.path.abspath(file_name)
	with io.open(file_name, 'rb') as image_file:
		content = image_file.read()
	image = types.Image(content=content)

    # Performs label detection on the image file
	response = client.label_detection(image=image)
	labels = response.label_annotations
	print('Labels:')
	for label in labels:
	    print(label.description)
    # [END vision_quickstart]



	image = types.Image(content=content)

	response = client.face_detection(image=image)
	faces = response.face_annotations
				# Names of likelihood from google.cloud.vision.enums
	likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                   		'LIKELY', 'VERY_LIKELY')
	print('Faces:')

	for face in faces:
		print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
		print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
		print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

		vertices = (['({},{})'.format(vertex.x, vertex.y)
            for vertex in face.bounding_poly.vertices])
				
		print('face bounds: {}'.format(','.join(vertices)))


def getMsgs(username):
	auth = tweepy.OAuthHandler(keys.key, keys.secretKey)
	auth.set_access_token(keys.accessToken, keys.accessTokenSecret)

	api = tweepy.API(auth)
	num = 0
	for status in tweepy.Cursor(api.user_timeline,username).items(20):
    
		tweetDateTime = str(status.created_at)
		dateTime = tweetDateTime.split()
		if (dateTime[0] == dt_string):
			print(status.text)
			try:
				for link in status.entities['media']:
					num = num +1
					url = str(link['media_url'])
					file_name = "image_name" + str(num) + ".jpg"

					print(url)
					req.urlretrieve(url, file_name)

					getImgDescription(file_name)

					#Instantiates a client
					

				#	with io.open(file_name, 'rb') as image_file:
				#		content = image_file.read()
				#		image = vision_client.image(
				#		content=content, )

				#	labels = image.detect_labels()
				#	for label in labels:
				#		print(label.description)

			# Performs label detection on the image file
	#				response = client.label_detection(image=image)
	#				labels = response.label_annotations

	#				print('Labels:')
	#				for label in labels:
	#					print(label.description)

			except (NameError, KeyError):        
				pass
#			else: #where we would do vision ai and all that fun stuff
				#if an image
#				print("")

#getImgDescription("bio.jpg")
getMsgs("alexfatyga_")