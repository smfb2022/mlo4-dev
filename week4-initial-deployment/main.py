from starlette.responses import StreamingResponse
from fastapi import FastAPI, File, UploadFile
from sentiment import BitcoinSentiment

config_path = './config/btc-config.yaml'
model = BitcoinSentiment(config_path)

#We generate a new FastAPI app in the Prod environment
#https://fastapi.tiangolo.com/
app = FastAPI(title='Bitcoin Sentiment Analysis')

#Call your get function for a health Check
#to receive both (face-bokeh and face-emotion)
@app.get("/", tags=["Health Check"])
async def root():
    return {"message": "Ok"}


#The bitcoin-sentiment endpoint receives number of twitter posts to analyze and returns the posts and sentiments
@app.post("/bitcoin-sentiment", tags=["Sentiment Analysis"])
async def sentiment(num_tweets: int = 10):

    #We run the model to get the tweets and analyze them
    tweets_with_sentiments = model.predict(num_tweets=num_tweets)
    
    #We encode the sentiments before returning it
    tweets_with_sentiments = tweets_with_sentiments.to_dict()

    return tweets_with_sentiments