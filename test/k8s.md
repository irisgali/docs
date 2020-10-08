## Install a bare-bones Kubeneretes

## Prerequisites:

* All machines use Ubuntu 18.04
* NVIDIA Drivers are installed for machines with GPUs.



### Run on Master Node (only)


Install docker by performing the instructions here: https://docs.docker.com/engine/install/ubuntu/

Restart the docker service:

`sudo systemctl restart docker`


Install k8s:
```
sudo sh -c 'cat <<EOF >  /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
EOF'

sudo apt-get update && sudo apt-get install -y apt-transport-https curl
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
cat <<EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
deb https://apt.kubernetes.io/ kubernetes-xenial main
EOF
sudo apt-get update
sudo apt-get install -y kubelet=1.18.4-01 kubeadm=1.18.4-01 kubectl=1.18.4-01

swapoff -a
sudo kubeadm init --pod-network-cidr=10.244.0.0/16 --kubernetes-version=v1.18.4
```
Permanently disable swap:
1. Edit the file /etc/fstab
2. Comment out any swap entry

Save the output of the init command.

```
mkdir .kube
sudo cp -i /etc/kubernetes/admin.conf .kube/config
sudo chown $(id -u):$(id -g) .kube/config

kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml

```

Test that Kubernetes is up and running:

```
kubectl get nodes
```
See that the master is ready


### Run on Kubernetes Workers 




Install docker by performing the instructions here: https://docs.docker.com/engine/install/ubuntu/

Restart the docker service:

`sudo systemctl restart docker`


Install k8s:
```
sudo sh -c 'cat <<EOF >  /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
EOF'

sudo apt-get update && sudo apt-get install -y apt-transport-https curl
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
cat <<EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
deb https://apt.kubernetes.io/ kubernetes-xenial main
EOF
sudo apt-get update
sudo apt-get install -y kubelet=1.18.4-01 kubeadm=1.18.4-01

swapoff -a
```

Replace the following command with the one saved from the init command above:

```
sudo kubeadm join 10.0.0.3:6443 --token 7wo4nf.ojpxltg7wbf7pqgj \
    --discovery-token-ca-cert-hash sha256:f4f481eba0d6a094d092a956f9d0bbd4e316211212bd58f445665e3fced399e3
```

