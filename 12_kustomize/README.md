# Kustomize

## Review Base configuration

Review files in [base folder](./base/):

- deployment.yml
- service.yml
- kustomization.yml <--- New file declaring files for kustomize

> [!TIP]
> Check [kustomize examples](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/)

## Create Environment Overlays

Create namespaces: *app-dev* and *app-prod*

Finish the file *overlays/dev/deployment-patch.yml* to fulfill:

- replica count: *2*
- namespace: *app-dev*
- Add env variable:
  - *COLOR: green*

Finish the file *overlays/prod/deployment-patch.yml* to fulfill:

- replica count: *5*
- namespace: *app-prod*
- Add env variable:
  - *COLOR: blue*
  - *ENVIRONMENT: production*

## Deploy Configurations

- Apply the Development overlay: `kubectl apply -k overlays/dev`
- Verify deployments
- Apply the Production overlay: `kubectl apply -k overlays/prod`
- Verify deployments

## Observe Differences

**Development Environment**:

- Number of replicas: 2
- Environment variable ENVIRONMENT: "development"

**Production Environment**:

- Number of replicas: 5
- Environment variable ENVIRONMENT: "production"
