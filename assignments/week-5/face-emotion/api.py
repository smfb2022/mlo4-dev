from starlette.responses import StreamingResponse
from fastapi import FastAPI, File, UploadFile
from emotions import Sentiment
import numpy as np
import cv2
import io

# Set triton url path
triton_url =

# We instantiate a face-emotion detector with the location of the pretrained models.
# In this case, the model needs to be set from our emotions.py
face_model_path = './haarcascade_frontalface_default.xml'
model = Sentiment()

# Let's generate a new FastAPI app
# Generate a FastAPI instance called `app` with the title 'Face-Emotion'
# https://fastapi.tiangolo.com/
app =


#The face-sentiment endpoint receives post requests with the image and returns the transformed image
@app.post("/face-sentiment", tags=["Sentiment Analysis"])
async def sentiment(file: UploadFile = File(...)):
    #We read the file and decode it
    contents = await file.read()
    nparr = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    #We run the model to get the transformed image
    return_img = model.transform(img)

    #We encode the image before returning it
    _, png_img = cv2.imencode('.PNG', return_img)
    return StreamingResponse(io.BytesIO(png_img.tobytes()), media_type="image/png")


@app.get("/", tags=["Health Check"])
async def root():
    return {"message": "Ok"}
