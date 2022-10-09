# Introduction
# bitcoin-sentiment
Cryptocurrencies like Bitcoin attract a lot of attention based on the social media networks
sentiment, trying to find the correlation between bitcoin price fluctuations against social media
sentiments.


Models:https://huggingface.co/ElKulako/cryptobert
datasets:https://huggingface.co/datasets/ElKulako/stocktwits-crypto
EDA and Cleanup done on the dataset:
cashtags, hashtags, usernames,
URLs, crypto wallets,
Chinese, Korean and Japanese characters,
(most) UTF-8 encoding issues
removed all posts shorter than 4 words
removed all duplicate posts
fixed spacing and punctuation issues, converted all text to lowercase



# Getting Started
TODO: Guide users through getting your code up and running on their own system. In this section you can talk about:
1.	Installation process
    Download from Git : https://github.com/jgpeoc/bitcoin-sentiment
2.	Software dependencies
    Listed in requirements.txt
3.	Latest releases
4.	API references

# Build and Test
TODO: Describe and show how to build your code and run the tests.
Unit Test:
     Debugging through visual code:
        add "args": ["--config", "/home/csh/workspace/github/capstone/sm-btc-sentiment/config/btc-config.yaml", "--num", "10"] in launch.json 
     or
     Command Line:
        python predict.py --config ./config/btc-config.yaml --num 14
Test Fast API:  
    uvicorn main:app --host 0.0.0.0 --port 8000

Test Transformers installation
    python -c "from transformers import pipeline; print(pipeline('sentiment-analysis')('we love you'))"

Docker Build
    docker build -t test-bitcoin .

Docker Run
    docker run -dp 8000:8000 test-bitcoin

Misc Useful Cmds
    delete all docker container: docker rm $(docker ps -a -q)
    delete all docker images with biton in name: docker images -a | grep bitcoin | awk '{print $3}' | xargs docker rmi -f

Docker Test locally
    http://127.0.0.1:8000/
    http://127.0.0.1:8000/docs

# Contribute
TODO: Explain how other users and developers can contribute to make your code better.


