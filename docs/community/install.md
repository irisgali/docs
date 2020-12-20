Follow the process below to install `runai-docker`.


## Prerequisites
1. Docker is [installed](https://docs.docker.com/get-docker/){target=_blank}
2. NVIDIA drivers and [NVIDIA container runtime](https://github.com/NVIDIA/nvidia-container-runtime){target=_blank} is installed

## Installation

Run the following:

``` bash
$ curl -fsSL https://raw.githubusercontent.com/run-ai/runai-docker/master/get.sh -o get-runai-docker.sh
$ sh get-runai-docker.sh
```

!!! Note
    You might have to use `sudo` in some machines


## Validation

After a successful installation you should be able to:

1. Run `runai-docker` and see the help information of `docker`
2. See that the daemon is running using the command `docker ps | grep runai-dockerd`

## Usage

`runai-docker` is a wrapper on top of `docker` with additional support for GPU memory virtualization.
Any `docker` command would work as-is with `runai-docker`.

To allow containers to allocate only a portion of GPU memory, use `runai-docker run` and pass as an argument `--gpu-memory` with the required amount of GPU memory.

The specified value could be one of the following:

* An absolute amount of GPU memory. Use the suffix `b` for bytes, `k` for kilobytes, `m` for megabytes and `g` for gigabytes (e.g. `--gpu-memory 3g` or `--gpu-memory 6543m`).
* A portion of the GPU. A floating point number which must be greater than 0 and smaller than or equal to 1.0 (e.g. `--gpu-memory 0.25` to make a container accessible to a quarter of the GPU memory).

GPU memory queries from within the container will show information only about its portion.
GPU memory allocations from any application in the container will be allowed only if it does not exceed the specified portion.
