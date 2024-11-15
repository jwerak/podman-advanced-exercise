# Creating Podman Pod

## Prerequisites

- check and build web-app container
  - `podman build -t flask-app-api .`

## Create pod via cli

Create a Pod that will host both the web application and the Redis database:

```bash
podman pod create --name webapp-pod -p 5000:5000
```

Add a Redis container to the Pod

- pod name: *webapp-pod*
- container name: *redis-container*
- image name: *docker.io/library/redis:2.8*

```bash
podman run -d --pod webapp-pod --name redis-container docker.io/library/redis:2.8
```

Add a API container to the Pod

- container name: *flask-app-api*
- image name: *flask-app-api*

```bash
podman run -d --replace  --pod webapp-pod --name flask-app-api flask-app-api
```

Verify that

- the container is running
- the pod is created (see *podman pod ...*)

## Create pod via k8s pod configuration

Create same pod as before, but using kubernetes pod definition

```bash
podman kube play k8s/web-app-pod.yml
```
