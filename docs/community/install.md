Why....

## Prerequisites
1. Have `docker` installed
2. Have NVIDIA drivers and [container runtime](https://github.com/NVIDIA/nvidia-container-runtime) installed

### Install
Run the following commands to install `runai-docker`:
```
$ curl -fsSL https://raw.githubusercontent.com/run-ai/runai-docker/master/get.sh -o get-runai-docker.sh
$ sh get-runai-docker.sh
```
> Note that you might have to use `sudo`

### Validation
After a successful installation you should be able to:
1. Run `runai-docker` and see the help information of `docker`
2. See that the vGPU daemon is running using the command `docker ps | grep runai-dockerd`

## Usage
`runai-docker` is a wrapper on top of `docker` with additional support for GPU memory virtualization.
Any `docker` command would work as-is with `runai-docker`.

To allow containers to allocate only a portion of GPU memory, use `runai-docker run` and pass as an argument `--gpu-memory` with the required amount of GPU memory. The specified value must be greater than 0 and smaller or equal to the size of the GPU Memory.

GPU memory queries from within the container will show information only about its portion.
GPU memory allocations from any application in the container will be allowed only if it does not exceed the specified portion.

`runai-docker` calls `docker` by default.
To use another command one can specify the `RUNAI_DOCKER` environment variable.

## Overview
GPU memory virtualization enables exposing containers to only a portion of the GPU memory.

This means that applications inside the container cannot exceed the amount of memory they should use.
Trying to allocate more memory than deserved would fail.
This makes it impossible for containers to exceed their share and cause failures to other containers.

Only a portion of the GPU memory is visible to applications inside the container.
This eliminates the need for any code changes for applications that allocate the entire GPU memory.

This makes GPU sharing among containers scalable and convenient.
No cooperation and code changes are necessary as every application assumes to have an entire GPU for its own use.
This virtual GPU has less memory than the actual GPU with respect to the portion it was specified.

Memory allocations are ceased in case of an application exceeding its container's share.

Memory queries are processed and memory information for the container only is returned, such as the total, free, and used GPU memory.
This causes `nvidia-smi` to show only the available portion of the GPU memory.
