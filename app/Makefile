#variables
#tag-gcp :=tag your docker img
img-name := stats
project-name := devops-304915
#version := version img docker
docker-repo := janotijr/devops-project-1
namespace = "application"


delete-project:
	gcloud projects delete $(project-name)

img-update-gke:
	kubectl set image deployment stats-app-deployment-gke stats-app-gke=gcr.io/$(project-name)/$(img-name):$(version)
 
img-update-k8s:
	kubectl set image deployment stats-k8s stats-container=$(docker-repo):$(version) --namespace=$(namespace)

img-versioning:
	docker tag $(img-name) $(img-name):$(version)

pre-push-build:
	eval $(minikube docker-env)
	docker build ./ -t $(img-name)

local:
	eval $(minikube docker-env)
	docker build ./ -t  $(img-name)
	docker run -p 5000:5000 $(img-name)

do-push:
	eval $(minikube docker-env)
	docker tag $(img-name) $(docker-repo):$(version)
	docker push $(docker-repo):$(version)
	docker tag $(img-name) gcr.io/$(project-name)/$(img-name):$(version)
	docker push  gcr.io/$(project-name)/$(img-name):$(version)

list-cluster:
	gcloud container clusters list

list-instance:
	gcloud compute instances list

service-ip:
	kubectl describe svc stats-app-gke | grep 'LoadBalancer Ingress'


k8s:
	eval $(minikube docker-env)
	minikube start --vm-driver=virtualbox
	kubectl create namespace $(namespace)
	kubectl apply -f deployment.yaml --namespace=$(namespace)
	kubectl expose deployment stats-k8s --type=NodePort --port=5000 --namespace=$(namespace)
	minikube service stats-k8s --namespace=$(namespace)


clean_k8s:
	kubectl delete namespace $(namespace)	
	
clean_docker:
	docker image rm $(img-name):$(version) -f
	docker image rm $(docker-repo) -f


git:
	sudo git add *
	sudo git commit -m "$(comment)"
	sudo git push origin master

help:
	@echo ''
	@echo '  img-update-gke        Change the docker image used in GKE. Usage: make img-update-gke project-name="gcp-project-name" img-name="name-of-docker-img" version="img version" '
	@echo '  img-update-k8s        Change the docker image user in kubernetes cluster. Usage:   make img-update-gke docker-repo="docker-repository-name" version="img version" '
	@echo '  img-versioning        Tag a image. Usage: make img-versioning img-name="docker image name" version="tag-or-version"  '	
	@echo '  local                 build docker image named "stats" - local'
	@echo '  pre-push-build    	build a docker image with Dockerfile. Needs a argument img-name '
	@echo '  do-push               Push your docker image to Docker repository and GCR. '
	@echo '  list-cluster          List GCP container clusteres'
	@echo '  list-instance         List GCP Compute Instances'
	@echo '  service-ip            Show IP of LoadBalancer GKE (access the app)'
	@echo '  k8s		        build a local kubernetes cluster with minikube'
	@echo '  clean_k8s             remove deployment and services from minikube'
	@echo '  clean_docker          remove docker image'
