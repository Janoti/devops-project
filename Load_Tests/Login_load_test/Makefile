do_test:
	pip install --no-cache-dir -r requirements.txt
	pip install locust
	locust -f locustfile.py -H http://35.202.104.125/
	
service-ip:
	kubectl describe svc stats-app-gke | grep 'LoadBalancer Ingress'