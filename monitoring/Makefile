helm-install:
	curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 
	chmod 700  get_helm.sh ./get_helm.sh

namespace:
	kubectl create ns monitor

prometheus:
	helm install prometheus-operator stable/prometheus-operator --namespace monitor	

list:
	kubectl --namespace monitor get pods	

pf-prometheus:
	kubectl port-forward -n monitor prometheus-prometheus-operator-prometheus-0   9090

pf-grafana:
	kubectl port-forward $(kubectl get pods --selector=app=grafana -n monitor --output=jsonpath="{.items..metadata.name}") -n monitor 3000		