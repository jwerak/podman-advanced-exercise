# Observe CGroups in action

## Prerequisites

Configure your VM to have at least 2 cpus.

## Test CGroups

Notes:

- Run commands as root
- Use top command to observe cpu loads,
- Use [stress image](https://github.com/progrium/docker-stress/blob/master/README.md) for this exercise.

### Test cases

#### Assigning cpus to containers

- Fully load single CPU core of your choice
  - `podman run -it --rm quay.io/jwerak/stress --cpu 1`
  - Verify that only one core is under load
- Run container again but load both cpus
  - `podman run -it --rm quay.io/jwerak/stress --cpu 2`
  - Modify CPUs that container can access directly in `/sys/fs/cgroup/`

#### Sharing cpu resources between containers

- Run 2 containers, 1 with cpushare 1024, second with 2048
  - observe how much resources each container consumes
  - `podman run -c 1024 -d quay.io/jwerak/stress --cpu 2`
  - `podman run -c 2048 -d quay.io/jwerak/stress --cpu 2`
- Ensure that container won't consume more CPU resources than specified no matter if its the only container on the host
  - See `cpushare` and `cpuquota`
- Experiment with multiple containers

#### Limit memory to container

- Run container (from stress image) with memory limited to `128M`
- Verify that container can't consume more memory than allocated

## Notes

- identify cgroups version
  - `stat -fc %T /sys/fs/cgroup/`
- Issues with cpuset privileges -> it must be [enabled for regular user](https://github.com/containers/podman/blob/main/troubleshooting.md#26-running-containers-with-resource-limits-fails-with-a-permissions-error) or run by root
