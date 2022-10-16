from fastapi import FastAPI
from sentiment import BitcoinSentiment

app = FastAPI(title='Bitcoin Sentiment Analysis')

#Call your get function for a health Check
@app.get("/", tags=["Health Check"])
async def root():   
    response = requests.get('http://bitcoin-model-cntr:8000')
    return response.json()



