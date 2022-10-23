import logging
import pandas as pd

from utils.logging import getLogger
from model.classifier import build_crypto_sentiment_analyzer
from utils.io import load_yaml
from data.load import LoadTweets


logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.FileHandler("run.log"), logging.StreamHandler()],
)

class BitcoinSentiment():
    def __init__(self,config_path):
        # create logging 
        self.logger = getLogger("tweet sentiment")
        self.logger.propagate = True

        #load config
        self.config_dict = load_yaml(config_path)

        # create sentiment classifer
        self.btc_analyzer = build_crypto_sentiment_analyzer(self.config_dict["model_name"])
        
        # create twitter data loader
        self.dl = LoadTweets(self.config_dict, self.logger)

    def predict(self, num_tweets = 10):

        # get tweets and predict sentiments
        posts = self.dl.get_tweets(num_tweets)
        preds = self.btc_analyzer(posts)
        return pd.concat([pd.DataFrame(posts), pd.DataFrame(preds)], axis=1)
        #print(pd.concat([pd.DataFrame(posts), pd.DataFrame(preds)], axis=1))








