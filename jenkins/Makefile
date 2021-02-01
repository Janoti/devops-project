create:
	#kubectl create namespace jenkins
	kubectl create -f jenkins-deployment.yaml -n jenkins

validate:
	kubectl get deployments -n jenkins

create-service:
	kubectl create -f jenkins-service.yaml -n jenkins

validate-service:
	kubectl get services -n jenkins
