# Podman basics

We will learn with `podman` cli tool to grasp basics of managing linux containers.

## Getting started

List available podman commands and explore help

```bash
podman --help
podman run --help
podman container --help
podman image --help
podman volume --help
podman search --help
```

## Find container image

- List available images for keyword `httpd`.
- Download "official" image version from docker hub (`library`).

## Create custom image

- Inspect the image
- Rename the image to `httpd-acme`

## Create the container

- run container with following
  - name: `acme-web`
  - image: `httpd-acme`
  - external port: `8080`
  - run as daemon
- Check running container
- Access the httpd port and explore logs
- Stop and Start the container

## Create Container with Volume

- stop and remove the container `acme-web`
- create same container and mount volume from `02_podman_basics` to `/usr/local/apache2/htdocs/`
- validate if the httpd is serving correct file

## Clean your environment

- prune containers and images
