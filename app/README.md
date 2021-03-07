## How to use

### App Routes

 * "/" - Show stats of your computer using psutil lib
 * "/login" - Show a login screen (no use)
 * "/users" - show a list of users created in memory 
 * "/users/ <cpf> " - search user by cpf
 * To insert a new user, replace the itens: 

     > curl --location --request POST 'http://<ip-load-balancer(GCP)-or-localhost(Docker/K8s)>/users' \--header 'Content-Type: application/json' \--data-raw '{
     "nome": "InsiraSeuNome",
     "sobrenome": "InsiraSeu Sobrenome",
     "cpf": 122312321321,
     "email": "ninguemusa@yahoo.com.br",
     "data_nasc": "19/01/1989"}' 
     
# Run the app with Docker locally:

 * Clone the repository

 * Inside app directory, run:

   >  $ make local img-name=<name-imagem>
 
 * Open your browser and type: http://127.0.0.1:5000/
 
# Run the app locally in a Kubernetes Cluster (minikube): 
 
 * Clone the repository

 * Inside app directory, run:

   >  $ make k8s 

 * In deployment.yaml, imagePullPolicy is set to  ** Always*, forcing pull latest image in Docker Hub. 

 
 * Run the following command to make sure if everything is working:

   >  $ kubectl get pods
   
 * An similar output is show:
  
  | NAME | READY| STATUS | RESTARTS |AGE |
  | ---- | ---- |------- | -------- | --- |
  | stats-k8s-7448f8cdf6-5h5xp| 1/1 | Running |  0 | 3m9s|
  |stats-k8s-7448f8cdf6-6qks8 | 1/1 | Running |  0 | 3m9s|
  |stats-k8s-7448f8cdf6-hhrcr | 1/1 | Running |  0 | 3m9s|
  |stats-k8s-7448f8cdf6-pfml7 | 1/1 | Running |  0 | 3m9s|

* Horizontal Pod AutoScaler
