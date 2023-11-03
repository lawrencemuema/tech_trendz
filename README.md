# tech_trendz
 TechTrendz is a young startup that focuses on developing cutting-edge web applications. They have recently realized the benefits of containerization and have decided to containerize their flagship application using Docker to enhance portability and deployment efficiency.​  As part of the containerization process, the DevOps team at TechTrendz has created a Docker image and Dockerfile for their application. However, due to some mistakes, the image fails to build correctly, leading to deployment issues. The DevOps team needs the assistance of the Azubi Africa Cloud Engineering students to identify and fix the errors.​  
 
 ### Build
```
docker build -t appname .
```
### Run
```
docker run -d -p 800:0 appname
```
### Stop
```
docker stop <container_id>
```
### Remove
```
docker rm <container_id>
```
### List
```
docker ps
```
### List all
```
docker ps -a
```
### Remove all
```
docker rm $(docker ps -a -q)
```
### push to docker hub
```
docker login
docker tag guessing_app <docker_hub_username>/guessing_app  
docker push <docker_hub_username>/guessing_app
```
### pull from docker hub
```
docker pull <docker_hub_username>/guessing_app
```
### run from docker hub
```
docker run -d -p 8080:8080 <docker_hub_username>/guessing_app
```​
