# The difference between CMD and ENTRYPOINT

Create Dockerfiles for these variations and check how command is executed in container.

Use container `docker.io/library/httpd` as base.

## Plain string

```Dockerfile
CMD ping localhost
```

## Array of commands

```Dockerfile
CMD["ping", "localhost"]
```

## Separate entrypoint

```Dockerfile
ENTRYPOINT ["ping"]
CMD ["localhost"]
```

## Extra

- Specify Environemnt variables in different forms and observe behavior
