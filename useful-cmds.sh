# start minikube
minikube start

# make locally built docker images available to minikube
eval $(minikube docker-env)

# build your docker image
docker build -t live-debug-image:latest .

# deploy your resources on k8s
kubectl apply -f app-deployment.yaml

# get url you can use to test your endpoints
minikube service live-debug-service --url

# adding more resources
kubectl edit deployment live-debug-deployment