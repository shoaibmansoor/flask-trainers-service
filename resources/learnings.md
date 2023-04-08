# Explaination

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: flask-app
  template:
    metadata:
      labels:
        app: flask-app
    spec:
      containers:
        - name: flask-app
          image: flask_app
          ports:
            - containerPort: 5000

```


This part of the file defines a Deployment resource:

- `apiVersion`: Specifies the API version to use, which in this case is apps/v1 for the Deployment resource.
- `kind`: Specifies the kind of resource, which in this case is Deployment.
- `metadata`: Contains metadata about the resource, such as its name.
  - `name`: The name of the Deployment, which is flask-app in this case.
- `spec`: Defines the desired state of the Deployment.
  - `replicas`: Specifies the number of replicas (pods) to create for the Deployment. In this case, it is set to 1.
  - `selector`: Specifies how the Deployment should identify the pods it manages.
    - matchLabels: A set of key-value pairs that must match the labels on the pods. In this case, it looks for pods with the label app: flask-app.
  - `template`: Defines the template for creating new pods.
    - `metadata`: Contains metadata about the pod template, such as labels.
      - `labels`: Key-value pairs that will be applied to each pod created from this template. In this case, the label is app: flask-app.
    - `spec`: Defines the desired state of the pod template.
      - containers: A list of containers that should run within each pod.
        - `name`: The name of the container, which is flask-app in this case.
        - `image`: The Docker image to use for the container, which is flask_app in this case.
        - `ports`: A list of ports that should be exposed by the container.
containerPort: The port that the container exposes, which is 5000 for the Flask app.

```
---
apiVersion: v1
kind: Service
metadata:
  name: flask-app
spec:
  selector:
    app: flask-app
  ports:
    - protocol: TCP
      port: 5000
      targetPort: 5000
  type: LoadBalancer

```

This part of the file defines a Service resource:

- `apiVersion`: Specifies the API version to use, which in this case is v1 for the Service resource.
- `kind`: Specifies the kind of resource, which in this case is Service.
- `metadata`: Contains metadata about the resource, such as its name.
  - `name`: The name of the Service, which is flask-app in this case.
- `spec`: Defines the desired state of the Service.
  - `selector`: Specifies how the Service should identify the pods it targets.
    - `app`: A key-value pair that must match the labels on the target pods. In this case, it looks for pods with the label app: flask-app.
  - `ports`: A list of ports that the Service should expose.
    - `protocol`: Specifies the protocol to use, which is TCP in this case.
    - `port`: The port
    - `targetPort`: The port number on the target pod that the Service forwards traffic to, which is also 5000 in this case.

  - `type`: Specifies the type of Service. In this case, it is set to LoadBalancer, which means the Service will be exposed through a cloud provider's load balancer if running on a supported cloud platform. When running on Minikube, it will automatically expose the Service through a NodePort.