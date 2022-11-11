# Kubeflow

## Create MiniKF Instance

- We are going to use MiniKF: <https://aws.amazon.com/marketplace/pp/prodview-7shm7yqkubjhg>
- You can ignore the red permission issues at the top
- Launch an instance using the EC2 console
- Make sure to enable public ip
- Open ports 22, 80, 443, 8443, 32123
- ssh into the machine and run minikf to see the progress
- Wait for it to finish and log into kubeflow in the address and the credentials provided
![creds](https://user-images.githubusercontent.com/37101144/201231660-5ef1ce4a-b0e6-4150-acd5-5fb8807fd51a.png)
- Make sure to allow self signed certificates
- Create a new volume called `models`
- Create a notebook instance that uses that volume
- Open a terminal in the notebook instance and clone the repo
- Create a data directory and download data


```
wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/annotations.tar.gz
tar -xzf images.tar.gz
tar -xzf annotations.tar.gz
```

- Install requirements
- Open the training notebook Training.ipynb
- Train and save the model on the `models` volume
- ssh back into the machine and deploy the model

```
kubectl apply -f K8s/
```

- Make sure the deployment is running

```
kubectl get pods -n kubeflow-user
```

- Check the model with the Inference.ipynb notebook
