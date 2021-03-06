### Namespace Monitor (Prometheus and Grafana) ###

helm-install:
	curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 
	chmod 700  get_helm.sh ./get_helm.sh

namespace_monitor:
	kubectl create ns monitor

prometheus:
	helm install prometheus-operator stable/prometheus-operator --namespace monitor	

list:
	kubectl --namespace monitor get pods	

pf-prometheus:
	kubectl port-forward -n monitor prometheus-prometheus-operator-prometheus-0   9090

pf-grafana:
	kubectl port-forward $(kubectl get pods --selector=app=grafana -n monitor --output=jsonpath="{.items..metadata.name}") -n monitor 3000		

### Namespace Logging ELK Stack (ElasticSearch, Logstach and Kibana)

namespace_logging:
	kubectl create -f kube-logging-ns.yaml

create-elastic:
	kubectl create -f elastic.yaml 

create kibana:
	kubectl create -f kibana.yaml -n logging

create-statefulset:
	kubectl create -f elasticsearch_statefulset.yaml -n logging


#### ELK Stack with Helm ####	

ElasticSearch_install:
	#curl -O https://raw.githubusercontent.com/elastic/Helm-charts/master/elasticsearch/examples/minikube/values.yaml
	helm install --name elasticsearch elastic/elasticsearch -f ./values.yaml 
