# Prod Images Exercise

**Table of Contents**

- [Prod Images Exercise](#prod-images-exercise)
  - [Scanning Docker images using Clair](#scanning-docker-images-using-clair)
    - [Setup Clair Server](#setup-clair-server)
      - [Start Clair](#start-clair)
    - [Use Clair to scan image](#use-clair-to-scan-image)
      - [Install clair-scanner](#install-clair-scanner)
      - [Scan image and print report](#scan-image-and-print-report)
      - [Clair notes](#clair-notes)
  - [Labeling Docker objects](#labeling-docker-objects)
    - [Adding label to image](#adding-label-to-image)
      - [Adding label to container](#adding-label-to-container)

## Scanning Docker images using Clair

Walk through with mentor

### Setup Clair Server

#### Start Clair

```bash
podman play kube clair-pod.yml
```

### Use Clair to scan image

#### Install clair-scanner

Download clairctl tool [from the release page](https://github.com/quay/clair/releases).

#### Scan image and print report

Submit report (for simplicity from same container).

```bash
podman exec -it clair-scanner-clair bash
clairctl -D manifest docker.io/dockerskoleni/nginx:1.11.6-alpine
clairctl -D report docker.io/dockerskoleni/nginx:1.11.6-alpine
```

Vulnerabilities are print to stout.

#### Clair notes

[Vulnerability sources](https://github.com/coreos/clair/blob/master/Documentation/drivers-and-data-sources.md)
[Other clair client tools](https://github.com/coreos/clair/blob/master/Documentation/integrations.md)

## Labeling Docker objects

### Adding label to image

**Exercise:** Create docker image with label `com.example.label-with-value="foo"` and prove that image contains the label.

**Hint:** Use Dockerfile to create image and `docker images --help`

#### Adding label to container

**Exercise:** Override container labels at runtime.
**Hint:** Alter label - `docker run --help`, Check label - `docker ps --help`.
