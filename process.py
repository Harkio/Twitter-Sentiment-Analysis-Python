
import re
import unicodedata


def processTweet(tweet):

       #Convert to lower case
        tweet = tweet.lower()
       #Normalise Unicode
        tweet = tweet.decode('unicode_escape').encode('ascii','ignore')
        #Convert www.* or https?://* to URL
       #Remove Links
        tweet = re.sub('((http\.[\s]+)|(https?://[^\s]+))','URL',tweet)
        #Convert @username to nothing
        tweet = re.sub('@[^\s]+','',tweet)
        #Remove additional white spaces
        tweet = re.sub('[\s]+', ' ', tweet)
        #Replace #word with word
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
        #Remove Small Words
        tweet = re.sub(r'\W*\b\w{1,4}\b','',tweet)
        #Remove Non ASCII
        tweet = re.sub(r'[^\x00-\x7F]+','', tweet)
        #Remove Spaces
        tweet = tweet.lstrip()
        return tweet

