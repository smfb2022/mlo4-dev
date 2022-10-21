from transformers import TextClassificationPipeline, AutoModelForSequenceClassification, AutoTokenizer
import numpy as np
import tritonhttpclient
from scipy.special import softmax

def build_crypto_sentiment_analyzer(model_name):

    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels = 3)
    pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer)

    return pipe



def run_inference(tweetstr, model_name='bitcoin-model', url='127.0.0.1:8000', model_version='1'):

    VERBOSE = False
    # hypothesis for topic classification
    topic = 'How early did you get into #Bitcoin and #ETH?'
    input_name = ['input__0', 'input__1']
    output_name = 'output__0'

    emotion_dict = {
            0: "Bearish",
            1: "Neutral",
            2: "Bullish"}


    print(f"Input string is  {tweetstr}.")
 
    R_tokenizer = AutoTokenizer.from_pretrained('ElKulako/cryptobert', use_fast=True)

    VERBOSE = False
    triton_client = tritonhttpclient.InferenceServerClient(
        url=url, verbose=VERBOSE)
    model_metadata = triton_client.get_model_metadata(
        model_name=model_name, model_version=model_version)
    print(f"model metadata {model_metadata}")
    model_config = triton_client.get_model_config(
        model_name=model_name, model_version=model_version)
    print(f"model_config {model_config}")
    # I have restricted the input sequence length to 256
    tokens  = R_tokenizer.batch_encode_plus([tweetstr],
                                    return_tensors='pt', max_length=256,
                                    truncation=True, padding='max_length'
                                    )
    print(f'token type {type(tokens)}')

    print(tokens['input_ids'])
    input_ids = np.array(tokens['input_ids'], dtype=np.int32)
    input_ids = input_ids.reshape(1, 256)
    input0 = tritonhttpclient.InferInput(input_name[0], ( 1, 256), 'INT32')
    input0.set_data_from_numpy(input_ids, binary_data=False)

    # print(tokens['attention_mask'])
    # attn_ids = np.array(tokens['attention_mask'], dtype=np.int32)
    # attn_ids = attn_ids.reshape(1, 256)
    # input1 = tritonhttpclient.InferInput(input_name[1], (1,  256), 'INT32')
    # input1.set_data_from_numpy(attn_ids, binary_data=False)

    output = tritonhttpclient.InferRequestedOutput(output_name,  binary_data=False)
    response = triton_client.infer(model_name, model_version=model_version, inputs=[input0], outputs=[output])
    logits = response.as_numpy('output__0')
    logits = np.asarray(logits, dtype=np.float32)

    print(f'logits values {logits}')
    probs = softmax(logits)
    print(f'softmax values {probs}')
    maxindex = int(np.argmax(logits))
    emotion = emotion_dict[maxindex]
    print(f'predicted emotion {emotion}')

