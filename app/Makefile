#variables
#tag-gcp :=tag your docker img
img-name := stats
project-name := devops-project-304014
#version := version img docker
docker-repo := janotijr/devops-project-1


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
	kubectl apply -f deployment.yaml
	kubectl expose deployment stats-k8s --type=NodePort --port=5000
	minikube service stats-k8s 


clean_k8s:
	kubectl delete deployment stats-k8s	
	kubectl delete service stats-k8s

clean_docker:
	docker image rm $(img-name):$(version) -f
	docker image rm $(docker-repo) -f


git:
	sudo git add *
	sudo git commit -m "Automatico"
	sudo git push origin master

help:
	@echo ''
	@echo '  local                 build docker image named "stats" - local'
	@echo '  pre-push-build    	build a docker image with Dockerfile. Needs a argument img-name 
	@echo '  k8s		        buil a local kubernetes cluster with minikube'
	@echo '  clean_k8s             remove deployment and services from minikube'
	@echo '  clean_docker          remove docker image'
