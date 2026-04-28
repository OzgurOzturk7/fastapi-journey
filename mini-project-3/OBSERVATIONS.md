\# OBSERVATIONS — Mini Project 3



\## 1. Pod vs Deployment

A Pod is a single container instance. If it crashes it does not restart on its own.

A Deployment watches the Pods and if one goes down it automatically creates a new one to replace it.



\## 2. ConfigMap for MongoDB URL

If URL is hardcoded every change requires editing the Deployment file. With ConfigMap you update one place and all Pods get the change automatically.



\## 3. Scaling to 3 replicas

The original Pod was not removed. Kubernetes just added 2 more Pods next to it to reach 3 total.



\## 4. MongoDB Pod crash

If MongoDB crashes webapp stops working. Kubernetes restarts it automatically, but there is a short downtime until it recovers.



\## 5. Surprising moment

I didn't expect minikube service command to automatically open the browser. I expect I  need to manually find the URL and open it myself.

