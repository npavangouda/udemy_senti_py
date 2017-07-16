import twitter
from PreProcessTweets import PreProcessTweets 


twitterApi = twitter.Api(
    consumer_key='uQPJ9NGi8mzQmA8f1Zofogb3R',
    consumer_secret='CTB1xubRtcZdN2Nj4W6II5OS2C56Nfk3PKlQiElz65YaL6yOY9',
    access_token_key='767254634587095041-uXjg0HlwY74cvip6vp8xg9olYJWZSkp',
    access_token_secret='K6N6phclz7g7jTi2KM5j41Uk2T8dpptTy2BhrTXcvr6m6'
)

# print(twitterApi.VerifyCredentials())

def createTestData(search_string):
    try:
        english_tweets = []
        tweets_fetched = twitterApi.GetSearch(search_string, count=100)
        for curLoopTweet in tweets_fetched:
            if curLoopTweet.lang == 'en':
                english_tweets.append(curLoopTweet)
        print('great! We fetched ' + str(len(tweets_fetched)) + ' tweets with the term ' + search_string + '!!')
        print('english tweets ' + str(len(english_tweets)) + ' tweets with the term ' + search_string + '!!')
        return [{'tweetText':status.text, 'sentiment':None} for status in english_tweets]
    except:
        print('something went wrong with twitter api')
        return None

testData = createTestData('#Apple')

tweetProcessor = PreProcessTweets()
trainingData = tweetProcessor.createTrainingCorpus('full-corpus.csv')
ppTrainingData = tweetProcessor.processTweets(trainingData)
ppTestData = tweetProcessor.processTweets(testData)
print(ppTestData[0:2])
