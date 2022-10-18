# Deployment on EC2

## Create EC2 Instance

- Go to EC2 console: <https://us-east-1.console.aws.amazon.com/ec2/home?region=us-east-1>
- Create EC2 instance
- Pick amazon linux
- Pick instance type: At least t3.medium
- Create key-pair
- Download key
- Edit network
- Enable IPV4 address
- Launch Instance
- SSH in the instance

## DVC

- Install pip (`yum install pip`)

- Install DVC with (`pip3 install dvc`)

- Initialize DVC (`dvc init`) in your repo

- Add s3 remote (`dvc remote add -d storage s3://triton-repository/data/`)

- Add files to git (`git add .`)

- Commit changes to git (`git commit -m "dvc init"`)

- Create a data folder (`mkdir data`)

- Download the pets dataset in the data folder:

```
wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/annotations.tar.gz
```

- Add the raw image data to dvc (`dvc add data/`)

- Add files to git (`git add data.dvc .gitignore`)

- Commit changes to git (`git commit -am "Raw data"`)

- Push data with dvc (`dvc push`)

- Uncompress the dataset

```
tar -xzf images.tar.gz
tar -xzf annotations.tar.gz
```

- Add files (`dvc add data/`)

- Add to git (`git add data.dvc`)

- Commit changes to git (`git commit -am "Uncompressed data"`)

- Push data with dvc (`dvc push`)
