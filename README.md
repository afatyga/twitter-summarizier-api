# twitter-summarizer-afatyga

# Assignment
Let’s build a module with an API that will return to the user of the API in text the twitter feed summary (Twitter Feeds and Text description of the images) => prints out the twitter feed summary in the terminal, returns a 1 on success <br>
I am expecting to use CB and CI in the exercise => completed <br>
I am also expecting you to developing examples using your API => See below <br>

# Flow of Code:
- I use the Tweepy API to receive a specified user's tweets and images
- Those images are saved to a JPG
- Each image goes through the Google Vision API for analysis
- A 1 is returned to indicate a success, a 0 for failure (incorrect input, not a real twitter handle, etc)
- At most 20 tweets of the past day will be printed on the terminal for the user to see

# The Actual Process
I found Tweepy very easy to use and manage after authenticating. I simply sent the twitter handle in and received an output status object and was then able to filter the tweets to only get the most recent of the past 20 tweets. <br>
Google Vision was trickier because Google kept giving me warnings but I was able to find tutorials that helped me a lot. <br>
I filtered for the most recent tweets by checking the created at date in the Status object and comparing it to today's date. <br>
I found myself having to create a new key for Google Vision each day which was tedious and a difficult problem to figure out at first <br>


# User Story Examples
- A parent wants to see the tweets of their child and get a broader idea of the images they posted in the past day. They see the child's tweets and additionally emotions of the faces in the images are detected.

# Examples of Use
My own twitter handle on 2/4/2020: <br>
<img src="termina.png" width="55%" />
<img src="twitterEx.png" width="55%" />
<br> Another twitter handle at use on 2/2/2020 <br>
<img src="dogterminal.png" width="55%" />
<img src="dogex.png" width="55%" />
