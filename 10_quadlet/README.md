# Quadlet

See official [documentation and examples](https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html) for this exercise.

Following exercises will be done as non-root user using quadlet files.

hint: Use following command to debug quadlet

```bash
/usr/libexec/podman/quadlet -dryrun -user
```

## Create Volume

Create volume called **httpd** using quadlet.

## Create Network

Create network called **frontend** using driver **bridge**.

Note: the network will be created only after it is referenced by another running container or pod.

## Create Container

Create a Container with following:

- Description - *HTTPD Container*
- Image: *docker.io/library/httpd*
- Label: *zone=frontend*
- Network: *systemd-frontend*
- External port: *80*
- Volume: *httpd* mounted in */usr/local/apache2/htdocs*

Populate volume with simple *index.html* file, e.g.

```bash
podman run --rm -v httpd:/data:z busybox sh -c "echo 'Hello, Quadlet!' > /data/index.html"
```
