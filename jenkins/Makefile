create:
	#kubectl create namespace jenkins
	kubectl create -f jenkins-deployment.yaml -n jenkins

validate:
	kubectl get deployments -n jenkins

create-service:
	kubectl create -f jenkins-service.yaml -n jenkins

validate-service:
	kubectl get services -n jenkins

create_cluster:
	gcloud container clusters create jenkins-cd \
  --machine-type n1-standard-2 --num-nodes 2 \
  --scopes "https://www.googleapis.com/auth/source.read_write,cloud-platform" \
  --cluster-version 1.15 \
  --zone "us-east1-d"

check_cluster:
	gcloud container clusters list

cluster_info:
	kubectl cluster-cluster_info

install:
	kubectl create -f namespace-jenkins.yaml
	helm repo update
	helm install jenkins -f values.yaml stable/jenkins 	--namespace jenkins		

print-password:
	kubectl get secret --namespace jenkins jenkins -o jsonpath="{.data.jenkins-admin-password}" | base64 --decode
	
