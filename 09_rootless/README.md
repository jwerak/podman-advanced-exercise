# Root-less vs Root-full podman

## Inter-container communication

### non-root container comunication on default network

Create 2 containers as non-root user

```bash
podman run --rm -d --name app-rootless quay.io/jwerak/pinger sleep 3600
podman run --rm -d --name db-rootless quay.io/jwerak/pinger sleep 3600
```

Try to ping one container from other.

The result should be that containers are not accessible on default network.

### root container comunication on default network

Create 2 containers as root user

```bash
podman run --rm -d --name app-rootfull quay.io/jwerak/pinger sleep 3600
podman run --rm -d --name db-rootfull quay.io/jwerak/pinger sleep 3600
```

Try to ping one container from other.

The result should be that containers are not accessible on default network.

### non-root container comunication on custom network

Create custom rootless network `rootless-custom-net`

Create 2 containers (`app-rootless`, `db-rootless`) as non-root user with custom network.

```bash
podman run --rm -d --name app-rootless quay.io/jwerak/pinger sleep 3600
podman run --rm -d --name db-rootless quay.io/jwerak/pinger sleep 3600
```

Try to ping one container from other.

The result should be that containers are accessible on custom network.

### Inspect the Default and Custom Networks

Compare the default and custom networks for both rootless and rootful modes:

```bash
podman network inspect podman
podman network inspect rootless-custom-net
sudo podman network inspect podman
```


podman run --rm -d --network rootfull-custom-net --name app-root quay.io/jwerak/pinger sleep 3600
podman run --rm -d --network rootfull-custom-net --name db-root quay.io/jwerak/pinger sleep 3600