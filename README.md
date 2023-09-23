# fastapi-nats
This is a Python application using FastAPI with NATS, and an example of how to run it using Docker compose

## Description
FastAPI-NATS is a Docker image that combines FastAPI framework with NATS messaging system.
This Docker image provides a ready-to-use environment for building microservices with FastAPI and NATS. FastAPI is a modern web framework for building APIs with Python, while NATS is a lightweight and high-performance messaging system.

## Installing and running
If you use Linux make sure the docker compose plugin is installed on your system using command```docker compose version``` if not then install it [https://docs.docker.com/compose/install/linux/](https://docs.docker.com/compose/install/linux/)

#### You can easily build the image using the following commands
Cloning repository  

``` 
git clone https://github.com/qalansiyah/fastapi-nats.git
```

Сhange to directory ```cd  /your path/fastapi-nats``` Use docker compose to create an image

```
docker compose build
```
and run it  

``` 
docker compose up
```
#### Or download  docker image  from DockerHub
Create docker-compose.yml in your working directory and put this code to in it

```services:
  main:
    image: kihaadhuffaru/fastapi-nats
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8888:8888"
    networks:
      - nats
    #volumes
      #- ./data:/app/data
    depends_on:
      - nats
    container_name: container-main

  nats:
    image: kihaadhuffaru/nats
    ports:
      - "4222:4222"
      - "8222:8222"
    container_name: container-nats
    networks:
      - nats
    #command: "-DV"
networks:
  nats:
    driver: bridge
```
Pull docker

```
 docker pull kihaadhuffaru/fastapi-nats 

```
and run it
``` 
docker compose up

 ``` 


