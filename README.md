# DEVOPS Project
#### Criado um app inicial, usando python e flask com as libs psutil. Serão feitas várias versões desse app.
#### O intuito é criar um projeto devops, automatizado, com o passo a passo descrito nesse README



## Para rodar a aplicação localmente em containers Docker:

    * Instale o Docker com o comando  no Ubuntu: 
   ``` $apt install docker ```

    * Clone o repositorio da app

    * Dentro do diretório, execute:

   ``` $make local ```
 
    -- Abra seu navegador e digite: http://127.0.0.1:5000/
    
    
## Makefile contém várias opções. Para saber, execute ``` $make help ```

## Para rodar localmente no cluster Kubernetes: 
     * Necessário o kubernetes instalado com minikube, para isso, siga o tutorial oficial https://minikube.sigs.k8s.io/docs/start/
     * Instalar um hypervisor, no exemplo utilizo o Virtualbox.
     * Após tudo instalado e configurado, execute:

   ``` $make k8s ```
   
     * Para saber se tudo funcionou corretamente, execute o comando kubectl get pods. Um output similar a esse deve aparecer:

      NAME                       READY    STATUS    RESTARTS   AGE
      stats-k8s-7448f8cdf6-5h5xp   1/1     Running   0          3m9s
      stats-k8s-7448f8cdf6-6qks8   1/1     Running   0          3m9s
      stats-k8s-7448f8cdf6-hhrcr   1/1     Running   0          3m9s
      stats-k8s-7448f8cdf6-pfml7   1/1     Running   0          3m9s
      
     * Para ver os logs da app, execute: kubectl logs --follow stats

      
## Rotas do app

     -- http://127.0.0.1:5000/ #return cpu and machine stats using psutil python lib
