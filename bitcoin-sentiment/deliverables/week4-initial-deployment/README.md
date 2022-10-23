<h1 align="center" id="heading">Bitcoin Sentiment Capstone</h1>

<b>week4-initial-deployment</em></b>

# Introduction
Bitcoin attract a lot of attention based on the social media networks.  The project is trying to find the correlation between bitcoin price fluctuations against social media
sentiments.

# Performance Report
Week4 deliverable returns the specified number of bitcoin related tweets along with its sentiments and score.  It can be tested using fast API, docker locally or on EC2. 

# Pre-Trained Model
https://huggingface.co/ElKulako/cryptobert

# Dataset
https://huggingface.co/datasets/ElKulako/stocktwits-crypto (Sept 1st Update)

EDA and Cleanup done on the dataset using in training the model and for any retraining is as follows:
* cashtags, hashtags, usernames,
* URLs, crypto wallets,
* Chinese, Korean and Japanese characters,
(most) UTF-8 encoding issues
* removed all posts shorter than 4 words
* removed all duplicate posts
* fixed spacing and punctuation issues, converted all text to lowercase


# Getting Started
TODO: Guide users through getting your code up and running on their own system. In this section you can talk about:
1.	Installation process
    Download from Git : 
    - https://github.com/jgpeoc/bitcoin-sentiment
2.	Software dependencies
    - Listed in requirements.txt
3.	Latest releases
4.	API references
    - https://docs.tweepy.org/en/v4.0.1/
    - https://docs.tweepy.org/en/v4.0.1/client.html


# Build and Test
TODO: Describe and show how to build your code and run the tests.
* Create a .env file with a twitter developer account BEARER_TOKEN="xxxx" in the project folder.

- Unit Test:
     * Debugging through visual code:
        add "args": ["--config", "/home/csh/workspace/github/capstone/sm-btc-sentiment/config/btc-config.yaml", "--num", "10"] in launch.json 

     or

     * Command Line:
        python predict.py --config ./config/btc-config.yaml --num 14

- Test Fast API:  
    * uvicorn main:app --host 0.0.0.0 --port 8000
    * Test accessing http://127.0.0.1:8000/ or  http://127.0.0.1:8000/docs

- Docker Support
    * docker build -t test-bitcoin .
    * docker run -dp 8000:8000 test-bitcoin
    * Test accessing Test accessing http://127.0.0.1:8000/ or  http://127.0.0.1:8000/docs

- Docker Support
    * docker build -t test-bitcoin .
    * docker run -dp 8000:8000 test-bitcoin
    * Test accessing Test accessing http://127.0.0.1:8000/ or  http://127.0.0.1:8000/docs

 - EC2 installation
    * https://github.com/FourthBrain/MLO-4/tree/main/assignments/week-4#readme 
    * When issuing the docker run command also use the -e option to provide the BEARED_TOKEN to be able to access tweets via its V2.0 API.  Ex: docker run -dp 8000:8000 -e BEARER_TOKEN=='xxxxx' bitcoin-test  

- Misc Useful Cmds
    * delete all docker container: docker rm $(docker ps -a -q)
    * delete all docker images with biton in name: docker images -a | grep bitcoin | awk '{print $3}' | xargs docker rmi -f
    * Test Transformers installation:
    python -c "from transformers import pipeline; print(pipeline('sentiment-analysis')('we love you'))"


# Contribute
TODO: Explain how other users and developers can contribute to make your code better.


