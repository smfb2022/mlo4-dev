import os
import dotenv
import tweepy as tw
import requests

class LoadTweets:
    '''
        Loads twitter data from twitter API 1 or 2
    '''

    def __init__(self, config_dict, logger):
        super().__init__()


        dotenv.load_dotenv(dotenv.find_dotenv())
        consumer_key = os.getenv('CONSUMER_KEY')
        consumer_secret = os.getenv('CONSUMER_SECRET')
        access_token = os.getenv('ACCESS_TOKEN')
        access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
        bearer_token = os.getenv('BEARER_TOKEN')

        self.client = tw.Client(bearer_token,  return_type=requests.Response, wait_on_rate_limit=True)
        self.query = config_dict["v2_query"]

    def get_tweets(self, max_tweets=10):    
         
        tweets = self.client.search_recent_tweets(query=self.query, 
            tweet_fields=['text'], max_results=max_tweets).json()['data']
        return [tweet['text'] for tweet in tweets]
 
    

        
        
