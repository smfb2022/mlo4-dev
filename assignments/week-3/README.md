<p align = "center" draggable=”false”
   ><img src="https://user-images.githubusercontent.com/37101144/161836199-fdb0219d-0361-4988-bf26-48b0fad160a3.png"
     width="200px"
     height="auto"/>
</p>



# <h1 align="center" id="heading">Week 3 - Deploying a Face Segmentation Background Changer on AWS EC2 using FastAPI</h1>

## 🛍️ Overview

Image segmentation has a lot of amazing applications that solve different computer vision problems. Image segmentation is, essentially, a classification task in which we classify each pixel as belonging to one of the target classes. So when you pass an image through a segmentation model, it will give one label to each of the pixels that present in the image. For this assignment, we'll be checking out background segmentation and replacement of those pixels. Background segmentation is a process in which an algorithm removes the static background from an image. This allows only changing a section of the image. This process is important for motion detection or object tracking.

In today's session, we'll be taking a look at face detection and background changer algorithm. Our goal will be to detect the faces in an image and replace the background while retaining those faces. To do this, we'll be utilizing DeepLab!

DeepLab is a state-of-art deep learning model for semantic image segmentation, where the goal is to assign semantic labels (e.g., person, dog, cat and so on) to every pixel in the input image. By using this image segmentation, we can separate the face in the foreground from the background. You can find the code in `deeplab.py`. We will then use a crawling Google image search to replace the original background with a background that matches our query.

## Today's Breakdown
- Part 1 - Introduction to AWS EC2
- Part 2 - Introduction to FastAPI
- Part 3 - Deploying a Face Segmentation Background Changer on AWS EC2 using FastAPI

## 📚 Learning Objectives

By the end of this session, you will be able to:

- Configure and launch AWS EC2 instances
- Write a FastAPI health check implementation
- Write a functioning FastAPI app file for our application
- Deploy a full FastAPI application to an AWS EC2 endpoint
- Access and utilize a FastAPI application using Swagger UI

## 📦 Deliverables
- Make the project public on your GitHub
- Submit a `.zip` file of the following:
  - Your `app.py` python file
  - Image prediction of your deployed model with the query

## 📝 Note
Please note, this is a challenging assignment. You will likely not finish this assignment today and we expect that. We are here to help!

## AWS EC2
####  What is AWS EC2 (Elastic Compute Cloud)?

Among the vast array of services that Amazon offers, EC2 is the core compute component of the technology stack. In practice, EC2 makes life easier for developers by providing secure, and resizable compute capacity in the cloud. It greatly eases the process of scaling up or down, can be integrated into several other services, and comes with a plan where you only pay for how much you use it. You can find out more [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) and [here](https://intellipaat.com/blog/what-is-amazon-ec2-in-aws/)!

#### Choosing an AMI (Amazon Machine Image)

An AMI is a template that is used to create a new instance—or virtual machine—based on user requirements. The AMI will contain information about the software, operating system, volume, and access permissions. There are two types of AMIs:

- Predefined AMIs: Amazon creates these, and the user can modify them.

- Custom AMIs: The user also creates these, and they can be reused. These AMIs are also available in the AMI Marketplace

#### Operating system
EC2 instance supports several OSes such as Linux, Microsoft Windows Server, CentOS and Debian.

#### AWS EC2 vs S3

Both Amazon EC2 and Amazon S3 are important services that allow developers to maximize use of the AWS cloud. The main difference between Amazon EC2 and S3 is that EC2 is a computing service that allows companies to run servers in the cloud. While S3 is an object storage service used to store and retrieve data from AWS through the Internet. S3 is like a giant hard drive in the cloud, while EC2 offers CPU and RAM in addition to storage. Many developers use both services for their cloud computing needs

## Resources

Want more? We've partnered up with [DeepLearning.ai](https://www.deeplearning.ai/) to bring to you a more advanced assignment utilizing docker. Please note, this assignment is optional and will not be graded.
- [Deploy a ML model with fastAPI and Docker](https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public/blob/main/course4/week2-ungraded-labs/C4_W2_Lab_1_FastAPI_Docker/README.md)

[TensorFlow DeepLab 1](https://github.com/tensorflow/models/tree/master/research/deeplab)\
[TensorFlow DeepLab 2](https://github.com/tensorflow/models/tree/master/research/deeplab2)\
[DeepLab: Semantic Image Segmentation with
Deep Convolutional Nets, Atrous Convolution,
and Fully Connected CRFs](https://arxiv.org/pdf/1606.00915.pdf)\
