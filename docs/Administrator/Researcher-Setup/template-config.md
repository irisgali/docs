# Configure Command-Line Interface Templates

## What are Templates?

Templates are a way to reduce the number of flags required when using the Command-Line Interface to start workloads. The researcher can:

*   Use a template by running ``runai submit --template <template-name>``
*   Review list of templates by running ``runai template list``
*   Review the contents of a specific template by running ``runai template get <template-name>``

The purpose of this document is to provide the administrator with guidelines on how to create & maintain templates.

## Template and Kubernetes

CLI Templates are implemented as_ Kubernetes <a href="https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/" target="_self">ConfigMaps</a>. A Kubernetes ConfigMap is the standard way to save cluster-wide settings.

### Template Usage

To create a template, create a file (e.g. `my-template.yaml`) with:

``` YAML
apiVersion: v1
kind: ConfigMap
data:
  name: template-1
  description: "my first template"
  values: |
    gpu: 
      required: true
    image:
      value: nvcr.io/nvidia/tensorflow:20.03-tf1-py3
    environments:
      - LEARNING_RATE=0.2
      - MYUSER=$USER
metadata:
  name: template-1
  labels:
    runai/template: "true"
```

To store this template run:

``` 
kubectl apply -f my-template.yaml -n runai
```

!!! Notes
    *   The template above sets the following:
        * That --gpu (or -g) is a required field when using this template
        * The default image file will be `nvcr.io/nvidia/tensorflow:20.03-tf1-py3`. The user can override this value and use a different image by setting the --image (-i) flag. 
        * There are two environment variables set `LEARNING_RATE` and `MYUSER`. Note that `MYUSER` will be set at runtime according to the value of `$USER`. The user can __add__ environment variables, and __override__ existing ones.  
    *   The label `runai/template` marks the ConfigMap as a Run:AI template.
    *   The name and description will show when using the `runai template list` command.
    *   See additional information below on flag syntax.


To see this template in the template list run:

```
runai template list
```

To show the properties of the created template run:

```
runai template get template-1
```

Use the template when submitting a workload

```
runai submit my-job1 ....  --template template-1
```



## Flag Syntax

* When specifying a single-valued flag, use the full name of the flag. For example, for setting `--gpu` use `gpu`. For a list of flags, see the [runai-submit reference document](../../Researcher/cli-reference/runai-submit.md). 
* When specifying a multi-valued flag, use the _plural_ of the flag name. For example: for setting the `--environment` flag use `environments`. For setting the `--volume` flag. Use `volumes` 


## The Default Template

The administrator can also set a default template that is always active:

``` YAML
apiVersion: v1
kind: ConfigMap
data:
  name: template-default
  description: "my first template"
  values: |
    job-name-prefix:
      value: acme
    volumes:
      - /mnt/nfs-share/john:/workspace/john
metadata:
  name: template-default
  labels:
    runai/template: "true"
  annotations: 
    runai/admin: "true"

```

!!! Notes
    * The template is denoted as the __default__ template with the annotation `runai/admin: "true"`
    * You can only have a single default template. If you set more than one default template, Run:AI will choose one at random.


# Override rules

* The User, when running `runai submit` always overrides the default template and a template specified with `--template`
* The default template overrides any specified template.



## See Also

For a list of `runai submit` flags, see the Run:AI [command-line reference](../../Researcher/cli-reference/runai-submit.md)