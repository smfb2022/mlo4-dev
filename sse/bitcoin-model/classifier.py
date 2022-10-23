from transformers import TextClassificationPipeline, AutoModelForSequenceClassification, AutoTokenizer
import numpy as np
import pandas
import tritonhttpclient
from scipy.special import softmax

def build_crypto_sentiment_analyzer(model_name):

    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels = 3)
    pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer)
    return pipe


emotion_dict = {
            0: "Bearish",
            1: "Neutral",
            2: "Bullish"}

class TritonBitcoinSentiment():

    def __init__(self, url='127.0.0.1:8000', model_name='bitcoin-model',  model_version='1'):
        self.input_name = ['input__0', 'input__1']
        self.output_name = 'output__0'
        self.model_name = model_name
        self.url = url
        self.model_version = model_version
        VERBOSE = False
        
        self.R_tokenizer = AutoTokenizer.from_pretrained('ElKulako/cryptobert', use_fast=True)

        self.triton_client = tritonhttpclient.InferenceServerClient(
            url=url, verbose=VERBOSE)
        # model_metadata = self.triton_client.get_model_metadata(
        #     model_name=model_name, model_version=model_version)
        # #print(f"model metadata {model_metadata}")
        # model_config = self.triton_client.get_model_config(
        #     model_name=model_name, model_version=model_version)
        # #print(f"model_config {model_config}")

    def run_inference(self, tweets):

        no_tweets = 1

        tweetstr = tweets[0:no_tweets]
        #print(f"Input string is  {tweetstr}.")
    
        # I have restricted the input sequence length to 256
        tokens  = self.R_tokenizer.batch_encode_plus([tweetstr],
                                        return_tensors='pt', max_length=256,
                                        truncation=True, padding='max_length'
                                        )
        #print(f'token type {type(tokens)}')

        #print(tokens['input_ids'])
        input_ids = np.array(tokens['input_ids'], dtype=np.int32)
        input_ids = input_ids.reshape(no_tweets, 256)
        input0 = tritonhttpclient.InferInput(self.input_name[0], ( no_tweets, 256), 'INT32')
        input0.set_data_from_numpy(input_ids, binary_data=False)

        #print(tokens['attention_mask'])
        attn_ids = np.array(tokens['attention_mask'], dtype=np.int32)
        attn_ids = attn_ids.reshape(1, 256)
        input1 = tritonhttpclient.InferInput(self.input_name[1], (no_tweets,  256), 'INT32')
        input1.set_data_from_numpy(attn_ids, binary_data=False)

        output = tritonhttpclient.InferRequestedOutput(self.output_name,  binary_data=False)
        response = self.triton_client.infer(self.model_name, model_version=self.model_version, inputs=[input0, input1], outputs=[output])
        logits = response.as_numpy('output__0')
        logitsa = np.asarray(logits, dtype=np.float32)

        df = pandas.DataFrame(columns=['Tweets','Sentiment','Score'])
        for i in range (no_tweets):
            logits = logitsa[i]
            #print(f'logits values {logits}')
            probs = softmax(logits)
            print(f'softmax values {probs}')
            maxindex = int(np.argmax(probs))
            emotion = emotion_dict[maxindex]
            #print(f'EMOTION is {emotion}  with SCORE {probs[:,maxindex]}for tweet {tweetstr}.')
            df = pandas.DataFrame(columns=['Tweets','Sentiment','Score'])
            df = df.append({'Tweets': tweetstr, 'Sentiment': emotion, 'Score': probs[maxindex]}, ignore_index=True)
        print(df)



# def run_inference(tweetstr, model_name='bitcoin-model', url='127.0.0.1:8000', model_version='1'):

#     VERBOSE = False

#     input_name = ['input__0', 'input__1']
#     output_name = 'output__0'

#     emotion_dict = {
#             0: "Bearish",
#             1: "Neutral",
#             2: "Bullish"}


#     #print(f"Input string is  {tweetstr}.")
 
#     R_tokenizer = AutoTokenizer.from_pretrained('ElKulako/cryptobert', use_fast=True)

#     VERBOSE = False
#     triton_client = tritonhttpclient.InferenceServerClient(
#         url=url, verbose=VERBOSE)
#     model_metadata = triton_client.get_model_metadata(
#         model_name=model_name, model_version=model_version)
#     #print(f"model metadata {model_metadata}")
#     model_config = triton_client.get_model_config(
#         model_name=model_name, model_version=model_version)
#     #print(f"model_config {model_config}")
#     # I have restricted the input sequence length to 256
#     tokens  = R_tokenizer.batch_encode_plus([tweetstr],
#                                     return_tensors='pt', max_length=256,
#                                     truncation=True, padding='max_length'
#                                     )
#     #print(f'token type {type(tokens)}')

#     #print(tokens['input_ids'])
#     input_ids = np.array(tokens['input_ids'], dtype=np.int32)
#     input_ids = input_ids.reshape(1, 256)
#     input0 = tritonhttpclient.InferInput(input_name[0], ( 1, 256), 'INT32')
#     input0.set_data_from_numpy(input_ids, binary_data=False)

#     #print(tokens['attention_mask'])
#     attn_ids = np.array(tokens['attention_mask'], dtype=np.int32)
#     attn_ids = attn_ids.reshape(1, 256)
#     input1 = tritonhttpclient.InferInput(input_name[1], (1,  256), 'INT32')
#     input1.set_data_from_numpy(attn_ids, binary_data=False)

#     output = tritonhttpclient.InferRequestedOutput(output_name,  binary_data=False)
#     response = triton_client.infer(model_name, model_version=model_version, inputs=[input0, input1], outputs=[output])
#     logits = response.as_numpy('output__0')
#     logits = np.asarray(logits, dtype=np.float32)

#     #print(f'logits values {logits}')
#     probs = softmax(logits)
#     #print(f'softmax values {probs}')
#     maxindex = int(np.argmax(probs))
#     emotion = emotion_dict[maxindex]
#     print(f'EMOTION is {emotion}  with SCORE {probs[:,maxindex]}for tweet {tweetstr}.')

