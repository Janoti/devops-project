
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


## Services Used

* Github
* Docker Hub (https://hub.docker.com/repository/docker/janotijr/devops-project)
* IBM Cloud
* GCP (Google Cloud Plataform)


## Getting started
* Install Kubernetes and minikube, follow the official tutorial >  https://minikube.sigs.k8s.io/docs/start/
* Install an hypervisor, like Virtualbox.
* Install [Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
* For Google Cloud, install [Gcloud SDK](https://cloud.google.com/sdk/docs/install)

## How to use

### Run the app with Docker locally:

 * Clone the repository

 * Inside app directory, run:

   >  $ make local
 
 * Open your browser and type: http://127.0.0.1:5000/
 
 ### Run the app locally in a Kubernetes Cluster: 
 
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

      
## RUNNING IN GOOGLE CLOUD PLATFORM (GCP) AND GKE ( GOOGLE KUBENETES ENGINE)
   * Create a [GCP Account](https://console.cloud.google.com)
   
   * Create a new project in GCP. After the creation, save the project_id.  
   
   * Clone the repository
   
   * For this project, i use Google Service Account with permissions to write to the storage bucket used by Terraform to save the states. To create, in GCP, go to IAM -> Service Account. Follow the default steps to create the account. Select the account and generate a private key in json format (Actions button). Save the file with the name **service-account.json** in TERRAFORM/terraform-gke folder.
   
   * Create a **Bucket** to save Terraform states. Save the bucket name.
   
   * Go to **root directory** (devops-project), edit the **MakeFile** and modify the following itens:
     - pre-push-build:
       eval $(minikube docker-env)
       docker build ./ -t **< your-docker-user >**/**< your-project-name >**:latest


     - do-push:
       eval $(minikube docker-env)
       docker push **< your-docker-user >**/**< your-project-name>**
       docker tag **< your-docker-user >**/**< your-project-name >** gcr.io/**< your-project_id >**/stats:latest
       docker push gcr.io/**< your-project_id >**/stats:latest
       
   * After the modifications, do the following command:
     > make pre-push-build
     > make do-push
    * A docker image of the app is created and your docker image is pushed to your Docker Hub Account and Google Image Repository.
    
   * Go to **TERRAFORM/terraform-gke**  directory
   
   * Edit the **main.tf file**, and modify the following itens:
     - bucket = **< name-of-your-bucket >**
     - variable "project" {default = **< project_id >**}
     - variable "region" {default= **< your_project_region >**}
     - variable "cluster_name" {default = **< name_your_cluster >**}
 
   * Edit the **MakeFile** file, and modify the following itens:
     - gcloud container clusters get-credentials **< your-cluster-name >** --region **< your-project-region >**
   
   * After the modifications, do the following command:
     > terraform init
    
   * Make sure to activate the Kubernetes Engine API  and Compute Engine API in your project
   
   * Execute the command to save the Terraform Plan in a file (out.plan)
     > terraform plan -out out.plan
    
   * If everything is ok, its time to APPLY:
     > terraform apply out.plan
  
   * After 
   
   ## Features

  - Here will be the features.


## Links

  - Link of deployed application: (IBM CLOUD and HEROKU)
  


