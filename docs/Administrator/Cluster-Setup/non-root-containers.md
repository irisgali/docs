## Introduction

In docker, as well as in Kubernetes, the default for running containers is running as 'root'. The implication of running as root is that processes running within the container have enough permissions to change anything on the machine itself. 

This gives a lot of power to containers, but does not sit well with modern security standards. Specifically enterprise security. 

## Non-root Containers
There are two [runai submit](../../Researcher/cli-reference/runai-submit.md) flags which limit this behavior at the Researcher level:

* The flag ``--run-as-user`` starts the container without root access. 
* The flag ``--prevent-privilege-escalation`` prevents the container from elevating its own privileges into root (e.g. running ``sudo`` or changing system files.). For more information see [Privilege Escalation](https://kubernetes.io/docs/concepts/policy/pod-security-policy/#privilege-escalation){target=_blank}.

However, these flags are voluntary. They are not enforced by the system.

It is possible to set these flags as a __cluster-wide default__ for the Run:AI CLI, such that all CLI users will be limited to non-root containers.

## Setting a Cluster-Wide Default

Save the following in a file (cluster-config.yaml)

``` yaml

apiVersion: v1
data:
  config: |
    enforceRunAsUser: true
    enforcePreventPrivilegeEscalation: true
kind: ConfigMap
metadata:
  name: cluster-config
  namespace: runai
  labels:
    runai/cluster-config: "true"
```

Run:

    kubectl apply -f cluster-config.yaml

!!! Limitation
    This configuration limits non-root for all Run:AI __CLI__ users. However, it does not prevent users or malicious actors from starting containers directly via Kubernetes API (e.g. via YAML files). There are third-party enterprise tools that can provide this level of security. 
 

## Creating a Temporary Home Directory

For containers to run as a specific user, the user needs to have a pre-created home directory within the image. This can be a daunting IT task. 

To overcome this, Run:AI provides an additional flag `--create-home-dir`. Adding this flag creates a temporary home directory for the user within the container.  

!!! Notes
    * Data saved in this directory will not be saved when the container exits. 
    * This flag is set by __default to true__ when the `--run-as-user` flag is used, and false if not.