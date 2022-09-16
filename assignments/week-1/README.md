<p align = "center" draggable=”false” ><img src="https://user-images.githubusercontent.com/37101144/161836199-fdb0219d-0361-4988-bf26-48b0fad160a3.png"
     width="200px"
     height="auto"/>
</p>

# Week 1 - End-to-end Deployment using Hugging Face and Sagemaker

### 🛍️ Hugging Face and Sagemaker

Hugging Face is the creator of Transformers, the leading open-source library for building state-of-the-art machine learning models. Hugging Face allows you to choose from tens of thousands of machine learning models for Natural Language Processing, Audio, and Computer Vision, publicly available in the Hugging Face Hub, to accelerate your machine learning workload.

Amazon SageMaker is a fully managed machine learning service. With SageMaker, data scientists and developers can quickly and easily build and train machine learning models, and then directly deploy them into a production-ready hosted environment. It provides an integrated Jupyter authoring notebook instance for easy access to your data sources for exploration and analysis, so you don't have to manage servers. It also provides common machine learning algorithms that are optimized to run efficiently against extremely large data in a distributed environment. You can deploy a model into a secure and scalable environment by launching it with a few clicks from SageMaker Studio or the SageMaker console.

One Command is All you Need!

With the new Hugging Face Deep Learning Containers available in Amazon SageMaker, training cutting-edge Transformers-based NLP models is much easier. There are variants specially optimized for TensorFlow and PyTorch, for single-GPU, single-node multi-GPU and multi-node clusters.

In this session, you will learn how to use Amazon SageMaker to train a Hugging Face Transformer model and deploy it afterwards.


### 📚 Learning Objectives

By the end of this session, you will be able to:

- Prepare and upload a test dataset to AWS S3
- Prepare a fine-tuning script to be used with Amazon SageMaker Training jobs
- Launch a training job and store the trained model into S3
- Deploy the model after successful training

### 📝 Note.
In this session, not all the imports are provided; you may need to import necessary modules / functions to be able to run the code successfully.
