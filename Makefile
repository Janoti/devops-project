local:
	eval $(minikube docker-env)
	docker build ./ -t  stats
	docker run -p 5000:5000 stats

dockerrepo:
	eval $(minikube docker-env)
	docker tag stats janotijr/stats
	docker build ./ -t janotijr/stats
	docker push janotijr/devops-project:stats

k8s:
	eval $(minikube docker-env)
	minikube start --vm-driver=virtualbox
	kubectl apply -f deployment.yaml
	kubectl expose deployment stats-k8s --type=NodePort --port=5000
	minikube service stats-k8s 

help:
	@echo ''
	@echo '  local                 build docker --image-- local'
	@echo '  dockerrepo    	build docker --image-- for janotijr in Docker Hub public repo. Might run $ docker login first'
	@echo '  k8s		        buil a local kubernetes cluster with minikube'
