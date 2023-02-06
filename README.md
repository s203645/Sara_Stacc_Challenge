# Sara_Stacc_Challenge

This is an application that displays the consumer's energy consumption for the past 500 hours. Then, based on this information, the application calculates which power provider that is the cheapest for this consumer to use. The cheapest power provider will appear in a green box. The others appear in red boxes. The boxes also contain information about the estimated monthly payment per power provider.

## My app is running as a docker container on a Linux VM on Linode.
### The IP address to the website can be found in the mail I sent you. I didn't have time to set up a domain name. Maybe next time :) 
## To run the docker image you can pull it from my docker hub repo:
https://hub.docker.com/repository/docker/sarabirkeland/stacchallenge

### Command for pulling docker image
```
docker pull sarabirkeland/stacchallenge
```

## Build and run docker image 
### Build docker image
```
docker build -t "navn" .
```
### Build docker image arm --> amd
```
docker buildx build --platform=linux/amd64 -t "name of image" . --push
```
### Pull docker image 
```
docker pull "name of image"
```
### Run docker image
```
docker run -d -p 80:80 "name of image"
```

Forgot to remove debug=True
