import io
import asyncio
from pathlib import Path
from fastapi import FastAPI
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sse_starlette.sse import EventSourceResponse
from sentiment import BitcoinSentiment

# Set triton url path
triton_url = 'triton:8000'

model = BitcoinSentiment(triton_url)

app = FastAPI(title='bitcoin-model')

# async def sentiment_generator(request):
#     while True:
#         if await request.is_disconnected():
#             break
#         tweets_with_sentiments = model.predict()
#         table = tweets_with_sentiments.to_html(index=False, justify="center", classes='styled-table', table_id="sentiment")
#         yield {
#             "event": "sentiment_data",
#             "retry": 5000,  # miliseconds
#             "data": table,  # HTML representation
#         }
#         await asyncio.sleep(10)  # in seconds


# BASE_DIR = Path(__file__).resolve().parent
# templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))

# @app.get("/", response_class=HTMLResponse)
# async def home(request: Request):
#     context = {"request": request}
#     return templates.TemplateResponse("index.html", context)

# @app.get("/sentiment_updates")
# async def runStatus(request: Request):
#     return EventSourceResponse(sentiment_generator(request))

# if __name__ == "__main__":
#     uvicorn.run(app, port=8000, host="0.0.0.0", debug=True)


#The bitcoin-sentiment endpoint receives number of twitter posts to analyze and returns the posts and sentiments
@app.post("/bitcoin-sentiment", tags=["Analysis"])
async def sentiment(num_tweets: int = 10):

     #We run the model to get the tweets and analyze them
     tweets_with_sentiments = model.predict(num_tweets=num_tweets)
    
     #We encode the sentiments before returning it
     tweets_with_sentiments = tweets_with_sentiments.to_dict()

     return tweets_with_sentiments


@app.get("/", tags=["Health Check"])
async def root():
     return {"message": "Ok"}

