Below are the prerequisites of a cluster installed with Run:AI. 


## Kubernetes Software

Run:AI requires Kubernetes 1.16 or above. Kubernetes 1.20 is recommended (as of April 2021).

If you are using Red Hat OpenShift. The minimal version is OpenShift 4.3 which runs Kubernetes 1.16.

## NVIDIA Driver

Run:AI requires all GPU nodes to be installed with NVIDIA driver version 410.104 or later and CUDA 9.0 or later. 

## Hardware Requirements

(see picture below)

*   (Production only) Dedicated __Run:AI System__ Nodes: To reduce downtime and save CPU cycles on expensive GPU Machines, we recommend that production deployments will contain at least one, dedicated worker machine, designated for Run:AI Software:
    
    *   4 CPUs
    *   8GB of RAM
    *   50GB of Disk space 
    
    
*   __Shared data volume:__ Run:AI uses Kubernetes to abstract away the machine on which a container is running:

    * Researcher containers: The Researcher's containers need to be able to access data from any machine in a uniform way, to access training data and code as well as save checkpoints, weights, and other machine-learning-related artifacts. 
    * The Run:AI system needs to save data on a storage device that is not dependent on a specific node.  

    Typically, this is achieved via Network File Storage (NFS) or Network-attached storage (NAS). NFS is usually the preferred method for Researchers which may require multi-read/write capabilities.


* __Docker Registry__ With Run:AI, Workloads are based on Docker images. For container images to run on any machine, these images must be downloaded from a docker registry rather than reside on the local machine (though this also is [possible](../../Researcher-Setup/Switch-from-working-with-Docker-to-working-with-Run-AI-/#image-repository)). You can use a public registry such as [docker hub](https://hub.docker.com/){target=_blank} or set up a local registry on-premise (preferably on a dedicated machine). Run:AI can assist with setting up the repository.

*  __Kubernetes__: Though out of scope for this document, Production Kubernetes installation requires separate nodes for the Kubernetes master. 

![img/prerequisites.png](img/prerequisites.jpg)

## User requirements

__Usage of containers and images:__ The individual Researcher's work should be based on [container](https://www.docker.com/resources/what-container){target=_blank} images. 

## Network Requirements

Run:AI user interface runs from the cloud. All container nodes must be able to connect to the Run:AI cloud. Inbound connectivity (connecting from the cloud into nodes) is not required. If outbound connectivity is proxied/limited, the following exceptions should be applied: 

### During Installation

Run:AI requires an installation over the Kubernetes cluster. The installation access the web to download various images and registries. Some organizations place limitations on what you can pull from the internet. The following list shows the various solution components and their origin: 

<table border="1" style="width: 650px; margin-left: 0px; margin-right: auto;">
<tbody>
<tr>
<th scope="row" style="width: 114.375px;">Name</th>
<th scope="row" style="width: 308.92px;">Description</th>
<th scope="row" style="width: 227.102px;">URLs</th>
<th scope="row" style="width: 43.4659px;">Ports</th>
</tr>
<tr>
<td style="padding: 6px; width: 104.375px;">
<p>Run:AI  Repository</p>
</td>
<td style="padding: 6px; width: 298.92px;">
<p> The Run:AI Package Repository is hosted on Run:AI’s account on Google Cloud </p>
</td>
<td style="padding: 6px; width: 217.102px;">
<p> <a href="http://runai-charts.storage.googleapis.com/">runai-charts.storage.googleapis.com</a> </p>
</td>
<td style="padding: 6px; width: 33.4659px;">
<p>443</p>
</td>
</tr>
<tr>
<td style="padding: 6px; width: 104.375px;">
<p>Docker Images Repository</p>
</td>
<td style="padding: 6px; width: 298.92px;">
<p>Various Run:AI images</p>
</td>
<td style="padding: 6px; width: 217.102px;">
<p><a href="http://hub.docker.com/">hub.docker.com </a></p>
<p>gcr.io/run-ai-prod </p>
</td>
<td style="padding: 6px; width: 33.4659px;">
<p>443</p>
</td>
</tr>
<tr>
<td style="padding: 6px; width: 104.375px;">
<p> Docker Images Repository </p>
</td>
<td style="padding: 6px; width: 298.92px;">
<p> Various third party Images</p>
</td>
<td style="padding: 6px; width: 217.102px;">
<p><a href="http://quay.io/">quay.io</a>  </p>
</td>
<td style="padding: 6px; width: 33.4659px;">
<p>  443   </p>
</td>
</tr>
</tbody>
</table>

### Post Installation

In addition, once running, Run:AI will send metrics to two sources:

<table border="1" style="margin-left: 0px; margin-right: auto; width: 650px;">
<tbody>
<tr style="height: 22px;">
<th scope="row" style="width: 116px; height: 22px;">Name</th>
<th scope="row" style="width: 314px; height: 22px;">Description</th>
<th scope="row" style="width: 215px; height: 22px;">URLs</th>
<th scope="row" style="width: 42px; height: 22px;">Ports</th>
</tr>
<tr>
<td style="padding: 6px; width: 106px;">
<p>Grafana</p>
</td>
<td style="padding: 6px; width: 304px;">
<p>Grafana Metrics Server</p>
</td>
<td style="padding: 6px; width: 205px;">
<p>prometheus-us-central1.grafana.net</p>
</td>
<td style="padding: 6px; width: 32px;">
<p>443 </p>
</td>
</tr>
<tr>
<td style="padding: 6px; width: 106px;">
<p> Run:AI </p>
</td>
<td style="padding: 6px; width: 304px;">
<p> Run:AI   Cloud instance </p>
</td>
<td style="padding: 6px; width: 205px;">
<p> <a href="https://app.run.ai">app.run.ai</a> </p>
<p> </p>
</td>
<td style="padding: 6px; width: 32px;">
<p>443</p>
</td>
<tr>
<td style="padding: 6px; width: 106px;">
<p> Auth0 </p>
</td>
<td style="padding: 6px; width: 304px;">
<p> Authentication Provider </p>
</td>
<td style="padding: 6px; width: 205px;">
<p> <a href="https://runai-prod.auth0.com/">runai-prod.auth0.com</a> </p>
<p> </p>
</td>
<td style="padding: 6px; width: 32px;">
<p>443</p>
</td>

</tbody>
</table>


