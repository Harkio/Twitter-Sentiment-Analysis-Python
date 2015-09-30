import MySQLdb
import process
import time

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from alchemyAPI import AlchemyAPI

#Required Authentication for Twitter API
consumerKey = 'yy7WyvomxBu53C0GlnlzHuAE9'
consumerSecret = '2iiG2KElTmRgER2vs8UhlpqgXYmmJJUBJqlTceDOYMuhpNjf3X'
accessToken = '24804339-711Szhusk6NWE9oa2uYIlH1Tazq1Jjf5zBwuNrcoH'
accessSecret = '36N00STwY038UKBvZ9n5QpJNlkG5vJXt1CbeoWVfcDunv'

#Database Connection
db = MySQLdb.connect(host="localhost",
                     user="graham",
                     passwd="A05bf311",
                     db="twitter",
                     port=3306)

cursor = db.cursor()

#Classes to Perform Analysis on Tweet Stream

class galwaylistener(StreamListener):

    def __init__(self, api=None):
        super(galwaylistener, self).__init__()
        self.num_tweets = 0

    def on_data(self, data):

        counter = 0
        # Just Gets Tweet from Data
        tweet = process.processTweet(data.split(',"text":"')[1].split('","source')[0])
        user = data.split('"screen_name":"')[1].split('","location"')[0]
        location = data.split('"location":"')[1].split('","url"')[0]
        language = data.split('"lang":"')[1].split('","contributors_enabled"')[0]


        alchemyAPI = AlchemyAPI()
        response = alchemyAPI.sentiment("text", tweet)
        self.num_tweets = self.num_tweets + 1
        print self.num_tweets
        print tweet



        #Try for Tweets with No Sentiment Type(Prevents Crashes)
        try:
            t = response["docSentiment"]["type"]
        except:
            t = "Unknown"

        #Try for Tweets with No Sentiment Score(Prevents Crashes)
        try:
            s = response["docSentiment"]["score"]
        except:
            s = 0


        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO galway(time, tweet, user, location, language, sentiment, score) VALUES (%s,%s,%s,%s,%s,%s,%s)",
            (time.asctime(time.localtime(time.time()))
             , tweet
             , user
             , location
             , language
             , t
             , s ))

        cursor.execute("DELETE FROM galway WHERE sentiment='Unknown' OR sentiment='neutral';")
        #cursor.execute("DELETE FROM tweets WHERE language!='en' or language!='en-gb';")

        db.commit()

        ##Only Collect 400 Tweets Per Run
        if (self.num_tweets >= 40):
            return False
        else:
            return True


    def on_event(self, status):
        print status

class dublinlistener(StreamListener):

    def __init__(self, api=None):
        super(dublinlistener, self).__init__()
        self.num_tweets = 0

    def on_data(self, data):

        counter = 0
        # Just Gets Tweet from Data
        tweet = process.processTweet(data.split(',"text":"')[1].split('","source')[0])
        user = data.split('"screen_name":"')[1].split('","location"')[0]
        location = data.split('"location":"')[1].split('","url"')[0]
        language = data.split('"lang":"')[1].split('","contributors_enabled"')[0]


        alchemyAPI = AlchemyAPI()
        response = alchemyAPI.sentiment("text", tweet)
        self.num_tweets = self.num_tweets + 1
        print self.num_tweets
        print tweet



        #Try for Tweets with No Sentiment Type(Prevents Crashes)
        try:
            t = response["docSentiment"]["type"]
        except:
            t = "Unknown"

        #Try for Tweets with No Sentiment Score(Prevents Crashes)
        try:
            s = response["docSentiment"]["score"]
        except:
            s = 0


        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO dublin(time, tweet, user, location, language, sentiment, score) VALUES (%s,%s,%s,%s,%s,%s,%s)",
            (time.asctime(time.localtime(time.time()))
             , tweet
             , user
             , location
             , language
             , t
             , s ))

        cursor.execute("DELETE FROM dublin WHERE sentiment='Unknown' OR sentiment='neutral';")
        #cursor.execute("DELETE FROM tweets WHERE language!='en' or language!='en-gb';")

        db.commit()

        ##Only Collect 400 Tweets Per Run
        if (self.num_tweets >= 40):
            return False
        else:
            return True


    def on_event(self, status):
        print status

class corklistener(StreamListener):

    def __init__(self, api=None):
        super(corklistener, self).__init__()
        self.num_tweets = 0

    def on_data(self, data):

        counter = 0
        # Just Gets Tweet from Data
        tweet = process.processTweet(data.split(',"text":"')[1].split('","source')[0])
        user = data.split('"screen_name":"')[1].split('","location"')[0]
        location = data.split('"location":"')[1].split('","url"')[0]
        language = data.split('"lang":"')[1].split('","contributors_enabled"')[0]


        alchemyAPI = AlchemyAPI()
        response = alchemyAPI.sentiment("text", tweet)
        self.num_tweets = self.num_tweets + 1
        print self.num_tweets
        print tweet



        #Try for Tweets with No Sentiment Type(Prevents Crashes)
        try:
            t = response["docSentiment"]["type"]
        except:
            t = "Unknown"

        #Try for Tweets with No Sentiment Score(Prevents Crashes)
        try:
            s = response["docSentiment"]["score"]
        except:
            s = 0


        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO cork(time, tweet, user, location, language, sentiment, score) VALUES (%s,%s,%s,%s,%s,%s,%s)",
            (time.asctime(time.localtime(time.time()))
             , tweet
             , user
             , location
             , language
             , t
             , s ))

        cursor.execute("DELETE FROM cork WHERE sentiment='Unknown' OR sentiment='neutral';")
        #cursor.execute("DELETE FROM tweets WHERE language!='en' or language!='en-gb';")

        db.commit()

        ##Only Collect 40 Tweets Per Run Per City
        if (self.num_tweets >= 40):
            return False
        else:
            return True

class belfastlistener(StreamListener):

    def __init__(self, api=None):
        super(belfastlistener, self).__init__()
        self.num_tweets = 0

    def on_data(self, data):

        counter = 0
        # Just Gets Tweet from Data
        tweet = process.processTweet(data.split(',"text":"')[1].split('","source')[0])
        user = data.split('"screen_name":"')[1].split('","location"')[0]
        location = data.split('"location":"')[1].split('","url"')[0]
        language = data.split('"lang":"')[1].split('","contributors_enabled"')[0]


        alchemyAPI = AlchemyAPI()
        response = alchemyAPI.sentiment("text", tweet)
        self.num_tweets = self.num_tweets + 1
        print self.num_tweets
        print tweet



        #Try for Tweets with No Sentiment Type(Prevents Crashes)
        try:
            t = response["docSentiment"]["type"]
        except:
            t = "Unknown"

        #Try for Tweets with No Sentiment Score(Prevents Crashes)
        try:
            s = response["docSentiment"]["score"]
        except:
            s = 0


        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO belfast(time, tweet, user, location, language, sentiment, score) VALUES (%s,%s,%s,%s,%s,%s,%s)",
            (time.asctime(time.localtime(time.time()))
             , tweet
             , user
             , location
             , language
             , t
             , s ))

        cursor.execute("DELETE FROM belfast WHERE sentiment='Unknown' OR sentiment='neutral';")
        #cursor.execute("DELETE FROM tweets WHERE language!='en' or language!='en-gb';")

        db.commit()

        ##Only Collect 400 Tweets Per Run
        if (self.num_tweets >= 40):
            return False
        else:
            return True


    def on_event(self, status):
        print status
    def on_event(self, status):
        print status

#Calling the Classes
auth = OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessSecret)

twitterStream = Stream(auth, galwaylistener())
twitterStream.filter(track=['galway'])

twitterStream = Stream(auth, dublinlistener())
twitterStream.filter(track=['dublin'])

twitterStream = Stream(auth, corklistener())
twitterStream.filter(track=['cork'])

twitterStream = Stream(auth, belfastlistener())
twitterStream.filter(track=['belfast'])
