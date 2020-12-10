# DEVOPS Project

## Para rodar a aplicação localmente em containers Docker:

    * Instale o Docker: ```apt install docker```

    * Clone o repositorio da app

    * Dentro do diretório, rode:

   ``` $make local ```
 
    -- Abra seu navegador e digite: http://127.0.0.1:5000/
    
## Para rodar localmente no cluster Kubernetes: (TODO)

   ``` $make k8s ```

## Rotas do app

     -- http://127.0.0.1:5000/ #return cpu and machine stats using psutil python lib
