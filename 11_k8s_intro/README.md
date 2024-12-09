# Deploying and Managing a Simple Kubernetes Application

## Prepare the Application YAML

Create an Deployment file and apply it to the cluster.

You may use file [deployment.yml](./k8s/deployment.yml) as a starting point.

> [!TIP]
> Check [Deployment spec](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/deployment-v1/) to validate format

- Create a namespace ***finforce***.
- Create an Deployment application with following values:
  - namespace: *finforce*
  - replica: *1*
  - name: *hello-app*
  - label: *app=hello-app*
  - image: *quay.io/jwerak/hello-app:latest*

> [!TIP]
> Use this command to watch changes in the namespace: `watch kubectl get all`

## Expose application

Create an Service file and apply it to the cluster.

You may use file [service.yml](./k8s/service.yml) as a starting point.

- Create an Service with following values:
  - namespace: *finforce*
  - type: *NodePort*
  - selector: *app = hello-app*
  - port: *8080*
  - nodePort: *30200*

> [!TIP]
> Use this command to connect to the service: `minikube service hello-app-service`

## Scale the application

Scale the deployment using sub-command `kubectl scale ...`

Refresh the application to see if the hostname changes.

> [!TIP]
> Use this command to watch changes in the namespace: `watch kubectl get all`

## Configure the deployment color

Update the color of deployment to red.

You may either update the *deployment.yml* file and *apply*, or do in-place edit using command `kubectl edit deployment hello-app`.

> [!TIP]
> Watch the status of the rolout using command: `kubectl rollout status deployment/hello-app`

## Extra

Build your own container, publish it to container registry and run it in your cluster.
