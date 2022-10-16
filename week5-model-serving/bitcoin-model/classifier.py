from transformers import TextClassificationPipeline, AutoModelForSequenceClassification, AutoTokenizer


def build_crypto_sentiment_analyzer(model_name):

    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels = 3)
    pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer)

    return pipe