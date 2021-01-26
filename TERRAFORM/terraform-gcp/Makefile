apply:
	./apply.sh
plan:
	./plan.sh
destroy:
	./destroy.sh
build:
	gcloud container clusters get-credentials devops-project-cluster --region us-central1
	kubectl apply --filename deployment.yaml
help:
	@echo ''
	@echo '  apply                  execute apply.sh'
	@echo '  plan                   execute plan.sh'
