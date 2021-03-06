## Devops Project
 Criado um app inicial, usando python e flask com as libs psutil. Serão feitas várias versões desse app.
 O intuito é criar um projeto devops, automatizado, com o passo a passo descrito nesse README.
 * Run the app with Docker locally
 * Run the app locally in a Kubernetes Cluster (minikube)
 * Running in GCP (Google Cloud Platform)
 * Monitoring Kubernetes using Grafana and Prometheus
 * Kubernetes Dashboard
 * Distributed load testing using Kubernetes Engine and LOCUST



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
* kubernetes 1.17.15-gke.800
* Grafana and Prometheus for monitoring
* Helm
* Jenkins
* Kubernetes Dashboard

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

     
# Running in GCP (Google Cloud Platform)
   * Create a [GCP Account](https://console.cloud.google.com)
   
   * Create a new project in GCP. After the creation, save the project_id.  
   
   * Clone the repository
   
   * Login GCE
     > gcloud auth login
   
   * Create a service account in GCP with permissions to write to the storage bucket used by Terraform to save the states: 
     > Go to IAM -> Service Account. Follow the default steps to create the account. Select the account and generate a private key in json format (Actions button). Save the file with the name **service-account.json** in TERRAFORM/terraform-gke folder.
   
   * Go to **TERRAFORM/terraform-gcp/bucket** and create a **Bucket** to save Terraform states. Modify **variables.tf** with your project values. After, run:
      > make bucket

   * Go to **app**  directory
   * Edit the **MakeFile** and modify the following itens:
   
    * variables:
       img-name := <your-image-name>
       project-name := <your-project-name>
       docker-repo := <your-docker-repository>
       
   * After the modifications, do the following command:
      > make pre-push-build 
     - A docker image of the app is created

      > make do-push version="version-of-your-app"
     - Your docker image is pushed to your Docker Hub Account and Google Image Repository
    
   * Go to **TERRAFORM/terraform-gke**  directory
   
   * Edit the **variables.tf file**, and modify the following itens:
   
    * variable "project" {default = **< project_id >**}
    * variable "region" {default= **< your_project_region >**}
     
   * Edit the **MakeFile** file, and modify the following itens:
     
    * gcloud container clusters get-credentials **< your-cluster-name >** --region **< your-project-region >**
   
   * After the modifications, do the following command:
     > make plan .
     
     > make apply .
     
   * After all infra is created, deploy the Load Balancer and 4 replicas of our app:

     > make build 
    
   * Make sure to activate the Kubernetes Engine API  and Compute Engine API in your project
 
     
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
     > make service-ip
  

  ## Update a Docker Image in GKE
   
   * After modifications in main.py, you should rebuild the new docker image of app and update the pods and repositories with the new image. Assuming that you already made the alterations in the variables in MakeFile, do the following:

   * Build the new image (inside /app directory):
     > make pre-push-build img-name="<name-docker-image>"

     > make do-push version="tag-or-version"

     > make img-update-gke version="tag-or-version"

   * After that, a Rolling-update will occur, destroying the old pods and replacing with the new ones.

# Monitoring Kubernetes using Grafana and Prometheus (manual install)
   
   * Go to **Monitoring** directory

   * If **Helm** not already installed, run :
     > make helm-install

   * For good pratice, install Prometheus containers in separeted namespace:
     > make namespace
     
   * Install Prometheus:
     > make prometheus
     
   * List the Pods of Prometheus anda Grafana:
     > kubectl --namespace monitor get pods
     
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
     > make pf-prometheus

   * Port-forward Grafana
     > make pf-grafana

   * Access http://127.0.0.1:3000 (Grafana). Login: **admin** and Password: **prom-operator**
   
   * To create a Prometheus data source in Grafana:

    * Click on the "cogwheel" in the sidebar to open the Configuration menu.
    * Click on "Data Sources". and "Add data Source"
    * Select "Prometheus" as the type.
    * Set the Prometheus server URL (for example, http://localhost:9090/)
    * Adjust other data source settings as desired (Http Access = Browser).
    * Click "Save & Test" to save the new data source.

## Kubernetes Dashboard
   * The Dashboard UI is not deployed by default. To deploy it, run the following command:

    > kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0/aio/deploy/recommended.yaml

   * You can access Dashboard using the kubectl command-line tool by running the following command:

    > kubectl proxy

   * Kubectl will make Dashboard available at http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/.
   
   * We are creating Service Account with name **admin-user** in namespace **kubernetes-dashboard** first.
      ```
      cat <<EOF | kubectl apply -f -    
       apiVersion: v1   
       kind: ServiceAccount   
       metadata:  
         name: admin-user  
         namespace: kubernetes-dashboard  
      EOF
      ```
   * In most cases after provisioning cluster using kops, kubeadm or any other popular tool, the ClusterRole cluster-admin already exists in the cluster. We can use it and create only ClusterRoleBinding for our ServiceAccount. If it does not exist then you need to create this role first and grant required privileges manually.
      ```
      cat <<EOF | kubectl apply -f -
      apiVersion: rbac.authorization.k8s.io/v1
      kind: ClusterRoleBinding
      metadata:
        name: admin-user
      roleRef:
        apiGroup: rbac.authorization.k8s.io
        kind: ClusterRole
        name: cluster-admin
      subjects:
      - kind: ServiceAccount
        name: admin-user
        namespace: kubernetes-dashboard
      EOF
      ```
   * Now we need to find token we can use to log in. Execute following command:

      > kubectl -n kubernetes-dashboard get secret $(kubectl -n kubernetes-dashboard get sa/admin-user -o jsonpath="{.secrets[0].name}") -o go-template="{{.data.token | base64decode}}"

   * It should print something like:

      > eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlcm5ldGVzLWRhc2hib2FyZCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJhZG1pbi11c2VyLXRva2VuLXY1N253Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImFkbWluLXVzZXIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiIwMzAzMjQzYy00MDQwLTRhNTgtOGE0Ny04NDllZTliYTc5YzEiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZXJuZXRlcy1kYXNoYm9hcmQ6YWRtaW4tdXNlciJ9.Z2JrQlitASVwWbc-s6deLRFVk5DWD3P_vjUFXsqVSY10pbjFLG4njoZwh8p3tLxnX_VBsr7_6bwxhWSYChp9hwxznemD5x5HLtjb16kI9Z7yFWLtohzkTwuFbqmQaMoget_nYcQBUC5fDmBHRfFvNKePh_vSSb2h_aYXa8GV5AcfPQpY7r461itme1EXHQJqv-SN-zUnguDguCTjD80pFZ_CmnSE1z9QdMHPB8hoB4V68gtswR1VLa6mSYdgPwCHauuOobojALSaMc3RH7MmFUumAgguhqAkX3Omqd3rJbYOMRuMjhANqd08piDC3aIabINX6gP5-Tuuw2svnV6NYQ

   * Now copy the token and paste it into Enter token field on the login screen.


   # Clean up
   * Remove the admin ServiceAccount and ClusterRoleBinding.

      > kubectl -n kubernetes-dashboard delete serviceaccount admin-user
      
      > kubectl -n kubernetes-dashboard delete clusterrolebinding admin-user

## Jenkins with Google Cloud Platform
#  With YAML Files
   * Go to jenkins folder
   * Run:
     > make create
   * This command will create a namespace jenkins and deploy jenkins

   * You can validade if is everything ok with:
     > make validate
    
   * Create a service, in this case, a loadBalancer to access jenkins
     > make create-service
   * Wait for the creation os the service and the external IP
     > make validate-service

   * The initial user and password of jenkins:
     > kubectl get pods -n jenkins
     > kubectl logs <pod-name> -n jenkins



## Distributed load testing using Kubernetes Engine and LOCUST


## Clean up (save money in GCP)

    * In the Cloud Console, go to the Manage resources page.Go to the Manage resources page
      In the project list, select the project that you want to delete and then click Delete delete.
      In the dialog, type the project ID and then click Shut down to delete the project.