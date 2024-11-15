# Setup Podman environment

## Prerequisities for this exercise

### Podman

[Install Latest Podman](https://podman.io/docs/installation)

or

[Install Podman Desktop](https://podman-desktop.io/downloads)

#### Linux

[Install on Linux](https://podman-desktop.io/docs/installation/linux-install)

#### Mac

[Download and install Podman Desktop for Mac](https://podman-desktop.io/docs/installation/macos-install)

or

```bash
brew install podman-desktop
```

Start podman-desktop to finish the installation

#### Win

[Download and install Podman Desktop for Windows](https://podman-desktop.io/docs/installation/windows-install)

or

```bash
winget install -e --id RedHat.Podman-Desktop
```

Start podman-desktop to finish the installation

## Validate the installation

```bash
podman info
```

## Running first container

```bash
podman run --replace -p 8080:8080 --name hello-world -d quay.io/jwerak/hello-world:latest
```

Stop and remove the container

```bash
podman stop hello-world
podman rm hello-world
```
