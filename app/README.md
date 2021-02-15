##main.py
*Python with flash app

*(/) Route --> psutil library monitoring some hardware componentes.
Shows Number of physical and logical cpus, boot time, docker container name, kubernetes cluster name, S.O.

*(/login) Route --> uses flask  to create a HTML file for a future Login Page.

*(/users) Route --> List a array of users saved in memory. In future will save and read from a DB.

*(/users/<cpf>) --> Search a user in memory by CPF

*(/users/--payload--) --> insert a user im memory

##deployment.yaml
* Kubernetes deployment

* Define a Deployment named stats-k8s with 4 replicas and a container named stats-container, port 5000 and a image pulled from docker registry.

