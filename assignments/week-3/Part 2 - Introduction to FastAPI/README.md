<p align = "center" draggable=”false” ><img src="https://user-images.githubusercontent.com/37101144/161836199-fdb0219d-0361-4988-bf26-48b0fad160a3.png"
     width="200px"
     height="auto"/>
</p>



# <h1 align="center" id="heading">Part 2: Introduction to FastAPI</h1>

For this portion of the assignment, our goal will be to deploy a health check endpoint in FastAPI on AWS EC2.

To do so we will need to:
- Setup our environment
- Write our health check code for `FastAPI`
- Push the code to our repository
- Pull the code to our instance
- Deploy the code using `uvicorn`
- Hit our `docs` endpoint

Let's get started. We'll get this to work locally first and then we will pull onto EC2.


Create a `conda` virtual environment using the following code block

``` bash
conda create -n aws_fastapi python=3.8 pip
```

![image](https://user-images.githubusercontent.com/72572922/164943060-02a71406-73fd-4ea4-ae06-5163812d77cf.png)

Activate the environment using the following code block

``` bash
conda activate aws_fastapi
```

![image](https://user-images.githubusercontent.com/72572922/164943075-aa6f66cc-68bb-46a6-bd59-054049d3bd7c.png)

Install FastAPI using the following code block

``` bash
pip install fastapi
```

![image](https://user-images.githubusercontent.com/72572922/164943085-a806dcdf-a7cf-432e-be9c-efd2e0bb0855.png)

Install uvicorn using the following code block

``` bash
pip install uvicorn
```

![image](https://user-images.githubusercontent.com/72572922/164943092-07bf364a-2c26-4a08-ab51-ed989b2502f3.png)

Save all the `pip` requirements using the following code block

``` bash
pip freeze > requirements.txt
```

![image](https://user-images.githubusercontent.com/72572922/164943122-cac80461-cdba-4130-9026-e45033ec1db6.png)

Open VS Code in your current conda environment

![image](https://user-images.githubusercontent.com/72572922/164943215-3c8cb8b9-5147-40b5-8858-f4020395a4dc.png)

## Write the Health Check endpoint

1. In `main.py` import FastAPI

``` python
from fastapi import FastAPI
```
2. Instantiate FastAPI server object

``` python
app = FastAPI()
```

3. Create a `get` endpoint through the `app` called `/health` with a `health` function that returns the following string: `Service is online.`

4. Launch server with the following command locally: `uvicorn main:app --port 8000`

5. Commit changes and push up to your Git repository (same as in part 1).

6. Connect to EC2 instance

7. Pull changes onto EC2 instance

8. Install libraries in `conda` environment on EC2 instance by running `pip install -r requirements.txt`
9. Launch server again by using `uvicorn main:app --host 0.0.0.0 --port 8000`

10. Hit your server! Go to browser and go to `{public_ip}:8000/docs` and you should see the Swagger `docs` where you can hit your health check endpoint.

11. Nice! You did it! Let's move on to Part 3!
