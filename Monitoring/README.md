# Monitoring Kubernetes using Grafana and Prometheus (manual install)

   Go to **Monitoring** directory

   * If **Helm** not already installed, run :
     > make helm-install

   * For good pratice, install Prometheus containers in separeted namespace:
     > make namespace
     
   * Install Prometheus:
     > make prometheus
     
   * List the Pods of Prometheus anda Grafana:
     > make list
     

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
     > pf-grafana

   * Access http://127.0.0.1:3000 (Grafana). Login: **admin** and Password: **prom-operator**
   
   * To create a Prometheus data source in Grafana:

    * Click on the "cogwheel" in the sidebar to open the Configuration menu.
    * Click on "Data Sources". and "Add data Source"
    * Select "Prometheus" as the type.
    * Set the Prometheus server URL (for example, http://localhost:9090/)
    * Adjust other data source settings as desired (Http Access = Browser).
    * Click "Save & Test" to save the new data source.

# Kubernetes Dashboard
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

# Log Aggregation Using ELK Stack

   * The ELK stack is a popular log aggregation and visualization solution that is maintained by elasticsearch. The word “ELK” is an abbreviation for the following   components:

    **E**lasticSearch: this is where the data gets stored.

    **L**ogstash: the program responsible for transforming logs to a format that is suitable for being stored in the ElasticSearch database.

    **K**ibana: where you can communicate with the Elasticsearch API, run complex queries and visualize them to get more insight into the data. You can also use Kibana to set and send alerts when a threshold is crossed. For example, you can get notified when the number of 5xx errors in Apache logs exceeds a certain limit.

    * Install Elasticsearch
      > todo:https://www.magalix.com/blog/kubernetes-observability-log-aggregation-using-elk-stack   and https://codeburst.io/google-kubernetes-engine-by-example-part-3-9b7205ad502f