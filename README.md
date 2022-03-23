# Usefull commands

```bash
# start minikube
minikube start

# make locally built docker images available to minikube
eval $(minikube docker-env)

# build your docker image
docker build -t medium-app-image:latest .

# deploy your resources on k8s
k apply -f medium-app.yaml

# get url you can use to test your endpoints
minikube service mediumapp-service --url

# adding more resources
k edit deployment mediumapp-deployment
```
