\# OBSERVATIONS — Docker Lab 2



\## 1. docker run vs kubectl run



docker run starts a container on your local machine.

kubectl run sends it to kubernetes which decides where to run it and manages it



\## 2. Scheduler event in kubectl describe



In the events section  first event is  scheduled this comes from the default scheduler.

Its kube scheduler, which decides which node runs the pod based on available resources and rules.



\## 3. Two components from kube-system



etcd: A distributed key value store that keeps the whole cluster state  pods, nodes, and configs. If etcd is lost, the cluster basically forgets everything.  Kube apiserver: The main entry point of Kubernetes. Every kubectl command goes through it. It handles requests and updates the data in etcd.



\## 4. Postgres-specific observation



pod crashed right away with Exit Code 1 because the postgres:16-alpine image needs the POSTGRES\_PASSWORD variable to start. it just fails and exits.This shows that container images expect certain environment variables, and Kubernetes doesn’t provide them automatically. You have to check the image docs or logs to know what required.



\## 5. Task 6 reflection — Why did Kubernetes not restart the pod?



A pod from kubectl run is not managed so if you delete it, it is gone.

Deployment keeps pods running and recreates them if they fail.

