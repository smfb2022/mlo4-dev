from fastapi import FastAPI
import pandas
import io
import asyncio
from pathlib import Path
from fastapi import FastAPI
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sse_starlette.sse import EventSourceResponse
import requests
from pandas.io.json import json_normalize

app = FastAPI(title='Bitcoin Sentiment Analysis')

# #Call your get function for a health Check
# @app.get("/", tags=["Health Check"])
# async def root():   
#     response = requests.get('http://bitcoin-model-cntr:8000')
#     return response.json()


async def sentiment_generator(request):
    while True:
        if await request.is_disconnected():
            break
        tweets_with_sentiments = requests.post('http://bitcoin-model-cntr:8000/bitcoin-sentiment') #model.predict()
        print(tweets_with_sentiments.status_code)
        print(tweets_with_sentiments.json())
        df = json_normalize(tweets_with_sentiments.json())
        print(df.head())    
        datadf = {'tweets':  ['aaaa', 'bbbb', 'cccc'],
        'sentiment': ['Bullish', 'Bearish', 'Neutral'],
        'score': ['0.111', '0.2222', '0.33333'],
        }
        df = pandas.DataFrame(datadf)
        table = df.to_html(index=False, justify="center", classes='styled-table', table_id="sentiment")
        yield {
            "event": "sentiment_data",
            "retry": 5000,  # miliseconds
            "data": table,  # HTML representation
        }
        await asyncio.sleep(10)  # in seconds


BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    response = requests.get('http://bitcoin-model-cntr:8000')
    print(response)
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)

@app.get("/sentiment_updates")
async def runStatus(request: Request):
    return EventSourceResponse(sentiment_generator(request))

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0", debug=True)



