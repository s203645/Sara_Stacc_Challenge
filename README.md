# Sara_Stacc_Challenge
## My app is running as a docker container on a linux vm on linode.
## To run the docker image you can pull it from my docker hub repo
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
