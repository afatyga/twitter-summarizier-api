# twitter-summarizer-afatyga

I found Tweepy very easy to use and manage after authenticating. I simply sent the twitter handle in and received an output status object and was then able to filter the tweets to only get the most recent of the past 20 tweets.
Google Vision was trickier because Google kept giving me warnings but I was able to find tutorials that helped me a lot.

Flow of Code:
- I use the Tweepy API to receive a specified user's tweets and images
- Those images are saved to a JPG
- each image goes through Google Vision for analysis

User Story
- A parent wants to see the tweets of their child and get a broader idea of the images they posted in the past day. They see the child's tweets and additionally emotions of the faces in the images are detected.
