# `showittome`

## Context

### Purpose

People adjacent to data science (data engineers, data scientists, data analysts, business
analysts) are usually not familiar with the concepts of Supply Chain attacks or
securing their credentials. The purpose of this repository is to showcase an
example of how an attacker could steal unencrypted SSH keys from someone's
environment using an R package with very little dependencies and sending it to a
Flask API to be stored and processed.

### License

**All of the code hereby included is protected under the Hippocratic License Version Number: 2.1.**

## Infrastructure

### R Package

The R package is contained in the `R_pkg` directory. It contains one function, `grabber()`, that looks at all of the credentials files in the `~/.ssh/` folder and sends the private keys via a POST request to a server. It has one R package dependency, the `httr` package. 

### Python API

The Python API is contained in the `Python_API` direcotry. It contains the Flask API and the Docker Compose files to deploy the API succesfully. 

#### Flask API

The Flask API is contained within the `Python_API/api` directory. The API has one POST endpoint at `/showittome` that returns a 200 code. If there is a GET request the API will deny the request so the API is not visible by visiting the website's endpoint in a browser. The connections to the API are handled by a `Gunicorn` server. 

#### Docker Compose

The `docker-compose.yaml` file brings up two services to serve the API. The first service is the API itself and the second service is an Nginx proxy to handle the connections to the `Gunicorn` server.
