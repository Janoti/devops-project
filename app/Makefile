#### VARIABLES ####
img-name := stats
project-name := devops-306215
version := 1
docker-repo := janotijr/devops-project-1
namespace = "application"

#### GOOGLE CLOUD ####

delete-project: # Deleta o projeto criado no GCP (var project-name) e tudo associado ao projeto
	gcloud projects delete $(project-name)
 
img-update-gke: # Faz um update na imagem usada no projeto no GCP. A imagem precisa estar publicada no GCR
	kubectl set image deployment stats-app-deployment-gke stats-app-gke=gcr.io/$(project-name)/$(img-name):$(version)
 
list-cluster:
	gcloud container clusters list

list-instance:
	gcloud compute instances list

service-ip: 
	kubectl describe svc stats-app-gke | grep 'LoadBalancer Ingress'


horizontal_autoscaler:
	kubectl autoscale deployment/stats-k8s --cpu-percent=50 --min=1 --max=10 -n application

img-update-k8s: # faz o update da versão da imagem utilizada no cluster local. Imagem deve estar publicada no Docker Hub
	kubectl set image deployment/stats-k8s stats=$(docker-repo):$(version) --namespace=$(namespace) --record=true

img-versioning: # permite mudar a tag/version de uma imagem docker builded
	docker tag $(img-name) $(img-name):$(version)

pre-push-build: # Docker daemon do minikube. Builda a imagem docker da app, utilizando o Dockerfile presente.
	eval $(minikube docker-env) 
	docker build ./ -t $(img-name)

local: # roda a app localmente no docker 
	eval $(minikube docker-env)
	docker build ./ -t  $(img-name)
	docker run -p 5000:5000 $(img-name)

do-push: # Nomeia e versiona a img local docker. Depois da push dessa img para o repositório docker e para o GCR atual.
	eval $(minikube docker-env)
	docker tag $(img-name) $(docker-repo):$(version)
	docker push $(docker-repo):$(version)
	docker tag $(img-name) gcr.io/$(project-name)/$(img-name):$(version)
	docker push  gcr.io/$(project-name)/$(img-name):$(version)



k8s: # Roda a app localmente em um cluster k8s. Cria o namespace e expõe a app. Add ingress.yaml
	eval $(minikube docker-env)
	minikube start --vm-driver=virtualbox
	kubectl create namespace $(namespace)
	kubectl apply -f deployment.yaml --namespace=$(namespace) --record
	kubectl apply -f ingress.yaml --namespace=$(namespace)
	kubectl expose deployment stats-k8s --type=NodePort --port=5000 --namespace=$(namespace)
	minikube service stats-k8s --namespace=$(namespace)


scale: # Escala localmente a app. Aumentando ou diminuindo o números de réplicas
	kubectl scale --replicas=$(replicas) deploy stats-k8s -n $(namespace)

rollback_status:
	kubectl rollout status deploy/stats-k8s -n $(namespace)
	kubectl rollout history deploy/stats-k8s -n $(namespace)

clean_k8s: # detona o namespace inteiro e tudo associado
	kubectl delete namespace $(namespace)	
	#kubectl get namespace "$(namespace)" -o json | tr -d "\n" | sed "s/\"finalizers\": \[[^]]\+\]/\"finalizers\": []/" | kubectl replace --raw /api/v1/namespaces/$(namespace)/finalize -f -

	
clean_docker:
	docker image rm $(img-name):$(version) -f
	docker image rm $(docker-repo) -f

kill_rogue_namespace:
	kubectl get namespace "$(namespace)" -o json | tr -d "\n" | sed "s/\"finalizers\": \[[^]]\+\]/\"finalizers\": []/" | kubectl replace --raw /api/v1/namespaces/$(namespace)/finalize -f -

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
