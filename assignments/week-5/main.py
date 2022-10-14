from starlette.responses import StreamingResponse
from fastapi import FastAPI, File, UploadFile
import requests

# Let's generate a new FastAPI app
# Generate a FastAPI instance called `app` with the title 'Triton Health Check'
# https://fastapi.tiangolo.com/
app = FastAPI(title='Triton Health Check')

#Call your get function for a health Check
#to receive both (face-bokeh and face-emotion)
@app.get("/", tags=["Health Check"])
async def root():
    response_items = {}
    
    response = requests.get('http://face-bokeh-cntnr:8000')
    response_items["face_bokeh"] = response.json()
    response = requests.get('http://face-emotion-cntnr:8000')
    response_items["face_emotion"] = response.json()
    line_format = '%s : %s'
    response_string = "\n".join([line_format % (key, str(value)) for key, value in response_items.items()])
    return response_string


#Call your get function for a health Check
#to receive both (face-bokeh and face-emotion)
@app.get("/", tags=["Health Check"])
async def root():
    response_items = {}
    
    response = requests.get('triton:8000')
    response_items["face_bokeh"] = response.json()
    response = requests.get('http://face-emotion-cntnr:8000')
    response_items["face_emotion"] = response.json()
    line_format = '%s : %s'
    response_string = "\n".join([line_format % (key, str(value)) for key, value in response_items.items()])
    return response_string