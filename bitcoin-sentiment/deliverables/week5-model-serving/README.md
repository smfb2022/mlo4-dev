# Bitcoin Sentiment Capstone

## Week5 Model Serving Update

### Implementing Triton Serving of a Hugging Face Model on EC2 instance : 11-implement-model-serving branch 

**References**
1. https://medium.com/nvidia-ai/how-to-deploy-almost-any-hugging-face-model-on-nvidia-triton-inference-server-with-an-8ee7ec0e6fc4
2. NVIDIA Triton meets ArangoDB Workshop: https://www.youtube.com/watch?v=vOIm7Hibgdo&t=1958s
3. Deploying an Object Detection Model with Nvidia Triton Inference Server: https://www.youtube.com/watch?v=1ICVRk6bdss

The model and its associated config file was generated from the "ElKulako/cryptobert" hugging face .bin model so it can be served using the triton inference server.  A notebook prototypes/torch_triton_attempt.ipynb was used to generate the torch .pt model and also generate the input and output needed for the config.pbtxt. 
They were placed in bitcoin-model folder and uploaded to ASW s3 bucket using:  aws s3 cp bitcoin-model s3://shobha-mur-week1/bitcoin-model --recursive

Triton inference server, the main app, and the bitcoin-sentiment app were all launched in seperate containers using the right requirements.txt, dockerfile, and docker-compose.yaml.

Currently to prototype the prediction using the model servered by the Triton inference server, predict.py does a simple hardcoded inferennce using triton http calls.  This dummy method is called in sentiment.py just to make sure the server can be reached and the inference can happen.  The call completes without any errors or exceptions but there is still a gap in understanding the inputs and outputs and the inference results.  Further research needs to be done in understanding the model conversion, and the arguments to the triton inference server

PS:  Can a hugging face model be even served on a triton inference server?  Not sue how much longer to spend on this.

## Week 5 progress 

Prototype for displayer the cryto inference web page using Server Side events (SSE) in a tabular format.







