from starlette.responses import StreamingResponse
from fastapi import FastAPI, File, UploadFile
import requests

#We generate a new FastAPI app in the Prod environment
#https://fastapi.tiangolo.com/
app = FastAPI(title='Two Face')

#Call your get function for a health Check
#to receive both (face-bokeh and face-emotion)
@app.get("/", tags=["Health Check"])
async def root():
    response_string = {}

    response = requests.get('http://week-4_face_bokeh_1:8000')
    response_string["face_bokeh"] = response.json()
    response = requests.get('http://week-4_face_emotion_1:8000')
    response_string["face_emotion"] = response.json()
    return response_string