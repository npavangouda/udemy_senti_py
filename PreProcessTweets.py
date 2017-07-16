import re
from nltk.tokenize import word_tokenize
from string import punctuation
from nltk.corpus import stopwords

class PreProcessTweets:
    def __init__(self):
        self._stopwords = set(stopwords.words('english')+list(punctuation)+['AT_USER', 'URL', '-'])
    
    def createTrainingCorpus(self, corpusFile):
        import csv
        corpus = []
        print('start reading: ' + corpusFile)
        with open(corpusFile, 'r') as csvfile:
            lineReader = csv.reader(csvfile)
            for row in lineReader:
                corpus.append({'tweetText':row[4], 'sentiment': row[1], 'topic': row[0]})
        
        print(len(corpus))
        return corpus

    def processTweets(self, list_of_tweets):
        processedTweets = []
        for tweet in list_of_tweets:
            processedTweets.append((self._processTweet(tweet['tweetText']), tweet['sentiment']))
        
        return processedTweets

    def _processTweet(self, tweet):
        #1. convert to lower case
        tweet = tweet.lower()
        #2. Replace links with the word URL
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)
        #3. Replace @username with 'AT_USER'
        tweet = re.sub('@[^\s]+', 'AT_USER', tweet)
        #4. Replace #word with word
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
        
        tweet = word_tokenize(tweet)
        
        return [word for word in tweet if word not in self._stopwords]


