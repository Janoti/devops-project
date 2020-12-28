
## Devops Project
 Criado um app inicial, usando python e flask com as libs psutil. Serão feitas várias versões desse app.
 O intuito é criar um projeto devops, automatizado, com o passo a passo descrito nesse README

## Versioning

1.0.0.0


## Authors

* **Paulo Janoti**: @janoti (https://github.com/janoti)


Please follow github and join us!
Thanks to visiting me and good coding!


## Technology 

Here are the technologies used in this project.

* python  x.x.x
* flask x.x.x
* docker
* terraform
* kubernetes


## Services Used

* Github
* Docker Hub
* IBM Cloud


## Getting started
* Install Kubernetes and minikube,follow the official tutorial >  https://minikube.sigs.k8s.io/docs/start/
* Install an hypervisor, like Virtualbox.
* Install Docker (ubuntu): 
>    $ apt install docker

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

      
   
      


## Features

  - Here will be the features.


## Links

  - Link of deployed application: (if has been deployed)
  - Repository: https://link_of_repository
    - In case of sensitive bugs like security vulnerabilities, please contact
      YOUR EMAIL directly instead of using issue tracker. We value your effort
      to improve the security and privacy of this project!






    
    
## Makefile contém várias opções. Para saber, execute ``` $make help ```


      
## Rotas do app

     -- http://127.0.0.1:5000/ #return cpu and machine stats using psutil python lib
