Inside CMD :
- docker version
- mkdir hello-docker
- cd hello-docker
- code .

Create file app.js and Dockerfile

Inside app.js file type the code:
console.log("Hello docker");

Inside Dockerfile type the code :
FROM node:alpine
COPY . /app
WORKDIR /app
CMD node app.js

In the CMD type the command:
docker build -t hello-docker .

Then type the command:
docker image ls

