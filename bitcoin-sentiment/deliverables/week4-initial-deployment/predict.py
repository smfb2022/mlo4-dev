
import argparse

import logging
from utils.logging import getLogger
from model.classifier import build_crypto_sentiment_analyzer
from utils.io import load_yaml
from data.load import LoadTweets
from sentiment import BitcoinSentiment

logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.FileHandler("run.log"), logging.StreamHandler()],
)

def get_args():
    """Parse commandline."""
    parser = argparse.ArgumentParser(
        description="Bitcoin sentiment analysis",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--config", "-c", help="model yaml file")
    parser.add_argument("--num", "-n", help="number of tweets")

    args = parser.parse_args()

    ## TODO - handle missing arguments

    return args



def main():
    """_summary_"""
    args = get_args()

    config_file = args.config
    num_tweets = args.num

    model = BitcoinSentiment(config_file)

    #We run the model to get the tweets and analyze them
    tweets_with_sentiments = model.predict(num_tweets=num_tweets)
    
    #We encode the sentiments before returning it
    tweets_with_sentiments = tweets_with_sentiments.to_dict()
    print(tweets_with_sentiments)

    
if __name__ == "__main__":
    main()

