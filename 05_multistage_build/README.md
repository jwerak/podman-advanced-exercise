# Dockerfile - Multistage build

Test build and run simple go app in docker container:

## Build docker image with the app:

```bash
docker build -t my-golang-app .
```

## Run the app

```bash
docker run -it --rm --name my-running-app my-golang-app
```

Check the size of image that has been built:

```bash
docker images
```

expected result:

```bash
REPOSITORY       z                           TAG                 IMAGE ID            CREATED             SIZE
my-golang-app                               latest              a689673636ba        42 minutes ago      778MB
```

Now try build smaler image that contains only golang app. And compare size.
