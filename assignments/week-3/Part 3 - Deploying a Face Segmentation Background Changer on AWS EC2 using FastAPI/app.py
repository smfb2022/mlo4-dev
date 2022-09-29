from starlette.responses import StreamingResponse
from fastapi import FastAPI, File, UploadFile
from deeplab import DeepLabModel
from mangum import Mangum
import numpy as np
import cv2
import io

#We instantiate a deeplab model with the location of the pretrained models
#https://github.com/tensorflow/models/tree/master/research/deeplab
model_path =
model = DeepLabModel(model_path)

#We generate a new FastAPI app in the Prod environment
#https://fastapi.tiangolo.com/
app = FastAPI(title='Face Segmentation Background Changer')  #, root_path="/Prod/")


#The face-bokeh endpoint receives post requests with the image and returns the transformed image
# Create an async POST function for "/face-bokeh/{query}" and look for tags = tags=["Face Bokeh"]
async def bokeh(file: UploadFile = File(...), query: str = ''):
    #We await the string, then read it
    contents =
    #Let's convert it from a string to a 8bit image
    nparr =
    #Decode the image in color
    img =
    #We run the model to get the segmentation masks
    mask =
    #We add the background
    return_img =
    #We encode the image before returning it
    _, png_img =
    return StreamingResponse(io.BytesIO(png_img.tobytes()), media_type="image/png")


#The root path will be used as the health check endpoint
@app.get("/", ##Code here##)
##Code here##

#Mangum is an adapter for running ASGI applications in AWS Lambda
#https://github.com/jordaneremieff/mangum
handler = Mangum(app=app)
