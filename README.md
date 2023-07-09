### Deploy app on docker
- Build
```
docker build -t flask-trainer-api .
```

- Start Container
```
docker run -p 5000:5000 flask-trainer-api
```


### Install docker on Ubuntu 20.04
```
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install docker-ce
docker --version
sudo service docker status

# If the Docker service is not running, you can start it with
sudo service docker start
```

### Create docker group and add a user
```
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
```

### Verify installation
```
docker run hello-world
```

### Troubleshoot docker
- Ensure that the user is a member of the docker group using the groups command:
```
groups <username>
```
- Check the permissions on the Docker daemon socket file:
```
ls -l /var/run/docker.sock
```
Ensure that the file has the correct ownership and permissions. By default, the file is owned by the root user and the docker group, and has permissions set to srw-rw---- (660).

- If the ownership or permissions are incorrect, you can fix them using the chown and chmod commands:
```
sudo chown root:docker /var/run/docker.sock
sudo chmod 660 /var/run/docker.sock
```

- sudo service docker restart
```
sudo service docker restart
```

### Install minikube
```
sudo apt update
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
kubectl version --client
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
chmod +x ./minikube-linux-amd64
sudo mv ./minikube-linux-amd64 /usr/local/bin/minikube
minikube version
minikube start --driver=docker
# Verify that the cluster is running and kubectl is configured to communicate with it
kubectl get nodes
# You should see one node with the status "Ready."
```

### Minikube build
Make sure minikube is installed properly at this stage
- Start Minikube
```
minikube start

```
- Deploy your application

You can now deploy your application on the Minikube cluster. To do this, you'll need a Kubernetes configuration file (YAML) that describes your application's deployment, service, and other necessary resources.

Replace <your-docker-image> with the name of your Docker image. Make sure your Docker image is available to Minikube, either by pushing it to a container registry like Docker Hub or by building it directly within Minikube using the eval $(minikube docker-env) command.

Apply the configuration file to create the resources in the Minikube cluster:
```
kubectl apply -f flask-app.yaml
```

- Access your application
```
minikube service flask-app
```
- This will open your application in your default web browser. Alternatively, you can get the Minikube IP and the service's NodePort to access the application:

```
minikube ip
kubectl get service flask-app
```


### Python Anywhere Deployment Instrcutions
- Sign up for a free account on PythonAnywhere.
- Start a new web app, select "Manual configuration", and the Python version you need.
- In a new Bash console, create a virtual environment with mkvirtualenv --python=/usr/bin/python3.x myenv.
- Install Flask (and other dependencies) in the virtual environment with pip install flask.
- Link the virtual environment to your web app in the "Virtualenv" section of the "Web" tab.
- Upload your Flask application files to the "Source code" directory.
- Edit the WSGI configuration file under the "Code" section of the "Web" tab to set the correct path and import your app.
- Hit "Reload" on the "Web" tab to launch your Flask app.