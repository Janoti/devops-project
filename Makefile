pre-push-build:
	eval $(minikube docker-env)
	docker build ./ -t janotijr/devops-project:latest

local:
	eval $(minikube docker-env)
	docker build ./ -t  stats
	docker run -p 5000:5000 stats

do-push:
	eval $(minikube docker-env)
	docker push janotijr/devops-project
	docker tag janotijr/devops-project gcr.io/elemental-day-302121/stats:latest
	docker push gcr.io/elemental-day-302121/stats:latest
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
	docker image rm stats -f


git:
	sudo git add *
	sudo git commit -m "Automatico"
	sudo git push origin master

help:
	@echo ''
	@echo '  local                 build docker --image-- local'
	@echo '  dockerrepo    	build and push a docker --image-- for janotijr in DockerHub public repo. Might run $ docker login first'
	@echo '  k8s		        buil a local kubernetes cluster with minikube'
	@echo '  clean_k8s             remove deployment and services from minikube'
	@echo '  clean_docker          remove docker image'
