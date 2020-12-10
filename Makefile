local:
	eval $(minikube docker-env)
	docker build ./ -t  stats
	docker run -p 5000:5000 stats
