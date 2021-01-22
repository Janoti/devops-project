
## Devops Project
 Criado um app inicial, usando python e flask com as libs psutil. Serão feitas várias versões desse app.
 O intuito é criar um projeto devops, automatizado, com o passo a passo descrito nesse README

## Versioning

1.0.0.2


## Authors

* **Paulo Janoti**: @janoti (https://github.com/janoti)


Please follow github and join us!
Thanks to visiting me and good coding!


## Technology 

Here are the technologies used in this project.

* python  3
* flask 1.1.2
* docker 20.10.2
* terraform 0.14.4
* kubernetes 1.16.15-gke.6000
* Grafana and Prometheus for monitoring
* Helm


## Services Used

* Github
* [Docker Hub](https://hub.docker.com/repository/docker/janotijr/devops-project)
* IBM Cloud
* GCP (Google Cloud Plataform) and GKE (Google Kubernetes Engine)


## Getting started
* Install Kubernetes and minikube, [follow the official tutorial](https://minikube.sigs.k8s.io/docs/start/)
* Install [Helm](https://helm.sh/docs/intro/install/)
* Install an hypervisor, like Virtualbox.
* Install [Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
* For Google Cloud, install [Gcloud SDK](https://cloud.google.com/sdk/docs/install)

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
     
### Run the app with Docker locally:

 * Clone the repository

 * Inside app directory, run:

   >  $ make local
 
 * Open your browser and type: http://127.0.0.1:5000/
 
### Run the app locally in a Kubernetes Cluster (minikube): 
 
 * Clone the repository

 * Inside app directory, run:

   >  $ make k8s 
    
 * Run the following command to make sure if everything is working:

   >  $ kubectl get pods
   
 * An similar output is show:
  
  | NAME | READY| STATUS | RESTARTS |AGE |
  | ---- | ---- |------- | -------- | --- |
  | stats-k8s-7448f8cdf6-5h5xp| 1/1 | Running |  0 | 3m9s|
  |stats-k8s-7448f8cdf6-6qks8 | 1/1 | Running |  0 | 3m9s|
  |stats-k8s-7448f8cdf6-hhrcr | 1/1 | Running |  0 | 3m9s|
  |stats-k8s-7448f8cdf6-pfml7 | 1/1 | Running |  0 | 3m9s|

      
## Running in GCP (Google Cloud Platform)
   * Create a [GCP Account](https://console.cloud.google.com)
   
   * Create a new project in GCP. After the creation, save the project_id.  
   
   * Clone the repository
   
   * Login GCE
     > gcloud auth login
   
   * For this project, i use Google Service Account with permissions to write to the storage bucket used by Terraform to save the states. To create, in GCP, go to IAM -> Service Account. Follow the default steps to create the account. Select the account and generate a private key in json format (Actions button). Save the file with the name **service-account.json** in TERRAFORM/terraform-gke folder.
   
   * Create a **Bucket** to save Terraform states. Save the bucket name.
   
   * Go to **app directory** of the cloned repository(devops-project), edit the **MakeFile** and modify the following itens:
   
    * pre-push-build:
       eval $(minikube docker-env)
       docker build ./ -t **< your-docker-user >**/**< your-project-name >**:latest


     * do-push:
       eval $(minikube docker-env)
       docker push **< your-docker-user >**/**< your-project-name>**
       docker tag **< your-docker-user >**/**< your-project-name >** gcr.io/**< your-project_id >**/stats:latest
       docker push gcr.io/**< your-project_id >**/stats:latest
       
   * After the modifications, do the following command:
      > make pre-push-build
     - A docker image of the app is created
      > make do-push
     - Your docker image is pushed to your Docker Hub Account and Google Image Repository.root
    
   * Go to **TERRAFORM/terraform-gke**  directory
   
   * Edit the **main.tf file**, and modify the following itens:
   
    * bucket = **< name-of-your-bucket >**
    * variable "project" {default = **< project_id >**}
    * variable "region" {default= **< your_project_region >**}
    * variable "cluster_name" {default = **< name_your_cluster >**}
 
   * Edit the **MakeFile** file, and modify the following itens:
     
    * gcloud container clusters get-credentials **< your-cluster-name >** --region **< your-project-region >**
   
   * After the modifications, do the following command:
     > terraform init
    
   * Make sure to activate the Kubernetes Engine API  and Compute Engine API in your project
   
   * Execute the command to save the Terraform Plan in a file (out.plan)
     > terraform plan -out out.plan
    
   * If everything is ok, its time to APPLY:
     > terraform apply out.plan
      
   * After all infra is created, deploy the Load Balancer and 4 replicas of our app:
     > make -f Makefile
     
   * Use kubectl commands to explore and manage your pods
   
   * List the cluster container:
     > gcloud container clusters list
   
   A similar output is show:
    
   | NAME | LOCATION | MASTER_VERSION |MASTER_IP | MACHINE_TYPE | NODE_VERSION | NUM_NODES | STATUS |
   |---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
   | devops-project-cluster | us-central1 | 1.16.15-gke.6000 | 34.70.62.209 | n1-standard-1 | 1.16.15-gke.6000 | 3 | RUNNING |

   * List the instances:
     > gcloud compute instances list
   
   A simular output is show:
   
   | NAME | ZONE | MACHINE_TYPE | PREEMPTIBLE | INTERNAL_IP | EXTERNAL_IP | STATUS |
   | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
   | gke-devops-project-c-default-node-poo-403d3662-fzg8 | us-central1-a | n1-standard-1 | | 10.128.0.2 | 35.223.67.181 | RUNNING |
   | gke-devops-project-c-default-node-poo-9761de40-xh71 | us-central1-b | n1-standard-1 | | 10.128.0.3 | 34.122.122.63 | RUNNING |
   | gke-devops-project-c-default-node-poo-ab784f34-qj4q | us-central1-f | n1-standard-1 | | 10.128.0.4 | 34.72.68.144 | RUNNING |

   * To expose the IP Address of Load Balancer and access the application, do the following:
     > kubectl describe svc stats-app-gke | grep 'LoadBalancer Ingress'
    
## Monitoring Kubernetes using Grafana and Prometheus (manual install)

   * Install Helm:
     > curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 chmod 700 get_helm.sh ./get_helm.sh
     
   * For good pratice, install Prometheus containers in separeted namespace:
     > kubectl create ns monitor
     
   * Install Prometheus:
     > helm install prometheus-operator stable/prometheus-operator --namespace monitor
     
   Verify the instalation, a similar output is show:
   
   | NAME | READY | STATUS | RESTARTS | AGE |
   | ---- | ---- | ---- | ---- | ---- |
   | alertmanager-prometheus-operator-alertmanager-0 | 2/2 | Running | 0 | 49s |
   | prometheus-operator-grafana-5bd6cbc556-w9lds | 2/2 | Running | 0 | 59s |
   | prometheus-operator-kube-state-metrics-746dc6ccc-gk2p8 | 1/1 | Running | 0 | 59s |
   | prometheus-operator-operator-7d69d686f6-wpjtd | 2/2 | Running | 0 | 59s |
   | prometheus-operator-prometheus-node-exporter-4nwbf | 1/1 | Running | 0 | 59s |
   | prometheus-operator-prometheus-node-exporter-jrw69 | 1/1 | Running | 0 | 59s |
   | prometheus-operator-prometheus-node-exporter-rnqfc | 1/1 | Running | 0 | 60s |
   | prometheus-prometheus-operator-prometheus-0 | 3/3 | Running | 1 | 39s |
   
   * Port-forward the Prometheus 
     > kubectl port-forward -n monitor prometheus-prometheus-operator-prometheus-0 9090
   * Port-forward Grafana
     > kubectl port-forward $(kubectl get pods --selector=app=grafana -n monitor --output=jsonpath="{.items..metadata.name}") -n monitor 3000

   * Access http://127.0.0.1:3000 (Grafana). Login: **admin** and Password: **prom-operator**
   
   * To create a Prometheus data source in Grafana:

    * Click on the "cogwheel" in the sidebar to open the Configuration menu.
    * Click on "Data Sources". and "Add data Source"
    * Select "Prometheus" as the type.
    * Set the Prometheus server URL (for example, http://localhost:9090/)
    * Adjust other data source settings as desired (Http Access = Browser).
    * Click "Save & Test" to save the new data source.


## Distributed load testing using Google Kubernetes Engine and LOCUST


## Clean up (save money in GCP)

    * In the Cloud Console, go to the Manage resources page.Go to the Manage resources page
      In the project list, select the project that you want to delete and then click Delete delete.
      In the dialog, type the project ID and then click Shut down to delete the project.
