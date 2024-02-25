# fastapi-nats
This is a microservice  using FastAPI with NATS, and an example of how to run it using Docker compose

## Description
FastAPI with NATS is a Docker image that combines FastAPI framework with NATS messaging system.
This is a microservice using FastAPI and NATS. FastAPI is a modern asynchronous web framework for building APIs with Python, while NATS is a lightweight and high-performance messaging system written in Go.

## Installing and running
#### You can easily build the image manually
If you use Linux make sure the docker compose plugin is installed on your system using command 
``` 
docker compose version
``` 
if not then install it [https://docs.docker.com/compose/install/linux/](https://docs.docker.com/compose/install/linux/)

Use the following commands
Cloning repository  
``` 
git clone https://github.com/qalansiyah/fastapi-nats.git
```
Сhange to directory ```cd  /your path/fastapi-nats``` 
Use docker compose to create an image
```
docker compose build
```
and run it  
``` 
docker compose up
```
#### Or download docker image  from DockerHub
```
docker pull kihaadhuffaru/fastapi-nats
```
```
docker pull kihaadhuffaru/nats
```
```
docker network create nats
```
```
docker run --name nats --network nats --rm -p 4222:4222 -p 8222:8222 kihaadhuffaru/nats
```
```
docker run --name fastapi-nats --network nats --rm -p 8888:8888 kihaadhuffaru/fastapi-nats
```




