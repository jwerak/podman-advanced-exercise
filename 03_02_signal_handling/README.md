# Signal handling

## Prerequisite

Explore and understand go source code (*cmd* dir) and *trap-example.sh* entrypoint.

## Exercise 1

Build and start container using following commands:

``` bash
export CMD=plain; podman build --file Dockerfile-shell-go --build-arg CMD -t signal-handling:shell-${CMD} .
podman run -d signal-handling:shell-${CMD}
```

stop image using command:

``` bash
podman stop <CONTAINER_ID>
```

- Explain why podman stop doesn't stop process immediately and
- fix Dockerfile to receive termination signals.

Hints:
- use `podman inspect <CONTAINER_ID>` to explore container runtime settings
- remember previous exercise

## Exercise 2

Verify that signals being sent to process end in successful closing of process.

``` bash
export CMD=signal; podman build --file Dockerfile-shell-go --build-arg CMD -t signal-handling:shell-${CMD} .
podman run -d signal-handling:shell-${CMD}
```

Fix the Dockerfile if the signals is still ignored.

## Exercise 3

Operations version of Ex2

Verify that signals being sent to process end in successful closing of process.

``` bash
podman build --file Dockerfile-trap -t signal-handling:trap .
podman run -d signal-handling:trap
```
