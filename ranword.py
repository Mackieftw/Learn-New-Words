import random #imports random module
import time #imports time module, use to create timers (Quick infin loop)
import tweepy #imports tweepy module
import sys #imports system module
import datetime #imports datetime, set vars for this to be useable module
from tweepy import OAuthHandler #imports auth handler module
from wordkeys import Tkey, Tsecret, access_token, access_token_secret  #imports from the keyys script

#-----------------------------------auth details - App (Learn New Words)-----------------------------------
auth = tweepy.OAuthHandler(Tkey, Tsecret)
auth.set_access_token(access_token, access_token_secret)

#--------------------------------API setup-----------------------------------------
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
now = datetime.datetime.now() #sets datetime with system
current_hour = now.hour #takes hours from the now var  (Maybe change from 24 hour time)
current_min = now.minute #takes mins from the now var
t=1 # do this for a quick infinite loop


while t > 0:  # set up said infinite loop
	now = datetime.datetime.now() #sets datetime with system
	current_hour = now.hour #takes hours from the now var  (Maybe change from 24 hour time)
	current_min = now.minute #takes mins from the now var
	word_to_print = random.choice(open("words.txt", encoding = "ISO-8859-1").readlines()) # random line from the file, this is the word, bird is the word? ;)
	f ="\n"+''.join(["http://www.thefreedictionary.com/",word_to_print]) # Create this as a var so the api.update_status does not break, due to the [] "\n"+''.join adds the following things together.
	api.update_status(status=word_to_print + f + "#Learn #Words #Dictionary"  ) # updates the status using the information from the variables
	print ("Tweet sent at",current_hour, ":", current_min) #prints me the time, so i know the tweets are being sent
	time.sleep(3600)#sets up a timer and only tweets every 4 hours
