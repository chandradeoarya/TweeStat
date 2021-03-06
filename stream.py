from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import json
import csv,sys
import matplotlib.pyplot as plt
from alchemyapi import AlchemyAPI

#pub = api.home_timeline()
class StdOutListener(StreamListener):
	#Prints received tweets to stdout.
	def on_data(self, data):
		# print(data)
		# return True
		decoded = json.loads(data)

		# Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
		print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
		#print decoded

		def on_error(self, status):
			print(status)

			def readHome(n):
				for status in tweepy.Cursor(api.home_timeline).items(n):
					print status.user.screen_name, status.text
					print "\n"

					if __name__ == '__main__':
						l = StdOutListener()

def saveData(SEARCHTERM,FILE,NUM):
	print "Entering Twitter API "
	SEARCHTERM = SEARCHTERM.lower()
	#print "Enter File Name "
	FILE = FILE
	#print "Enter number of tweets "
	NUM = int(NUM)
	#stream = Stream(auth, l)
	#stream.filter(track=[HASHTAG])
	FILE = open(FILE,'wb')
	fi = csv.writer(FILE)
	HASHTAG = SEARCHTERM.replace(" ","")
	arr = tweepy.Cursor(api.search, q=SEARCHTERM, lang="en").items(NUM)
	for item in arr:
		try:
			item.text = item.text.lower().encode('ascii', 'ignore')
			# Remove reduntant retweets and only check English tweets
			if (item.retweeted == False) and ((SEARCHTERM in item.text) or HASHTAG in item.text) and ("rt " not in item.text):
				item.text = item.text.replace(HASHTAG,SEARCHTERM)
				fi.writerow([item.text])
				#print item.text+'\n'
			# textRefined = item.text.encode('ascii', 'ignore')
			# response = alchemyapi.sentiment_targeted('text', textRefined, SEARCHTERM)
			# print textRefined, response["docSentiment"]["type"]
			#fi.writerow([textRefined,response["docSentiment"]["type"]])
		except Exception as e:
			print e
			continue
		#decoded = json.loads(item)
		# Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
		#print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
	FILE.close()

access_token = "2895960169-Q8hQuNMLpybYSMgRba9g1hfS6gL5XGzzpCdt305"
access_token_secret = "CNFM2jQpqmOYcf4F8jhFa89jvGEKYdkIsVC0ZPKqrL1FY"
consumer_key = "Ucgj0ZotxSKez6fecx1FkbRQp"
consumer_secret = "ITKErjm9dGCVBIZmgL3fujzc1lpSMyztXbWfy8AsBonZEEtzxG"
alchemyapi = AlchemyAPI()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

if __name__ == "__main__":
	if len(sys.argv) <= 3:
		print "usage: .py <search_term> <filename> <number_tweets>"
		sys.exit(0)
	saveData(sys.argv[1],sys.argv[2],sys.argv[3])