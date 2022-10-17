from transformers import TextClassificationPipeline, AutoModelForSequenceClassification, AutoTokenizer
import numpy as np
import tritonhttpclient

from transformers import TextClassificationPipeline, AutoTokenizer
from scipy.special import softmax


def build_crypto_sentiment_analyzer(model_name):

    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels = 3)
    pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer)

    run_inference()

    return pipe



def run_inference(model_name='bitcoin-model', url='127.0.0.1:8000', model_version='1'):

    VERBOSE = False
    # hypothesis for topic classification
    topic = 'bitcoin is great'
    premise = 'Bullish'
    input_name = ['input__0', 'input__1']
    output_name = 'output__0'


    R_tokenizer = AutoTokenizer.from_pretrained('ElKulako/cryptobert')


    VERBOSE = False
    # hypothesis for topic classification
    topic = 'bitcoin is great'
    input_name = ['input__0', 'input__1']
    output_name = 'output__0'
    triton_client = tritonhttpclient.InferenceServerClient(
        url=url, verbose=VERBOSE)
    model_metadata = triton_client.get_model_metadata(
        model_name=model_name, model_version=model_version)
    model_config = triton_client.get_model_config(
        model_name=model_name, model_version=model_version)
    # I have restricted the input sequence length to 256
    input_ids = R_tokenizer.encode(premise, topic, max_length=256, truncation=True, padding='max_length')
    input_ids = np.array(input_ids, dtype=np.int32)
    mask = input_ids != 1
    mask = np.array(mask, dtype=np.int32)
  
    mask = mask.reshape(1, 256) 
    input_ids = input_ids.reshape(1, 256)
    input0 = tritonhttpclient.InferInput(input_name[0], (1,  256), 'INT32')
    input0.set_data_from_numpy(input_ids, binary_data=False)
    input1 = tritonhttpclient.InferInput(input_name[1], (1, 256), 'INT32')
    input1.set_data_from_numpy(mask, binary_data=False)
    output = tritonhttpclient.InferRequestedOutput(output_name,  binary_data=False)
    response = triton_client.infer(model_name,         model_version=model_version, inputs=[input0, input1], outputs=[output])
    logits = response.as_numpy('output__0')
    logits = np.asarray(logits, dtype=np.float32)
# we throw away "neutral" (dim 1) and take the probability of
    # "entailment" (2) as the probability of the label being true 
    entail_contradiction_logits = logits[:,[0,2]]
    probs = softmax(entail_contradiction_logits)
    true_prob = probs[:,1].item() * 100
    print('Probability that the label is true: ' + true_prob)

    

