# Creating Podman Pod

## Prerequisites

- check and build web-app container
  - `podman build -t flask-app-api .`

## Create pod via cli

Create a Pod that will host both the web application and the Redis database:

- pod name: *webapp-pod*
- expose port: *5000:5000*

Add a Redis container to the Pod

- pod name: *webapp-pod*
- container name: *redis-container*
- image name: *docker.io/library/redis:2.8*

Add a API container to the Pod

- container name: *flask-app-api*
- image name: *flask-app-api*

Verify that

- the container is running
- the pod is created (see *podman pod ...*)

## Create pod via k8s pod configuration

Create same pod as before, but using kubernetes pod definition in file *k8s/web-app-pod.yml*
