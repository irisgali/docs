# Overview

[Docker](https://www.docker.com/){target=_blank} allows the allocation of a specified amount of __CPU__ memory for a container. This is achieved by specifying the required memory as a flag. E.g., `docker run --memory 1g`.

However, there is no equivalent Docker flag for allocating a specified amount of __GPU__ memory. _Run:AI Docker_ is an extension of Docker that allows the user to isolate a portion of a GPU or a certain amount of GPU memory for a specific container.

_Run:AI docker_ is the community edition of the _Run:AI orchestration and virtualization platform_

The command `runai-docker` is a wrapper on top of `docker` with additional support for GPU memory virtualization.
Any `docker` command would work as-is with `runai-docker`.

## How it Works
GPU memory virtualization enables exposing containers to only a portion of the GPU memory.

An application sees only a portion of the total GPU memory. Furthermore, the container cannot exceed the amount of memory they should use. Trying to allocate more memory than deserved would fail. This makes it impossible for containers to exceed their share and cause failures to other containers.

When running the command `nvidia-smi` inside the container, it show only the allotted portion of the GPU memory.


## Example

Create an `ubuntu` based container on a machine containing a GeForce RTX 2080 Ti GPU with 11GB RAM.

``` console hl_lines="10"
$ docker run -it --rm --gpus 1 ubuntu nvidia-smi

+-----------------------------------------------------------------------------+
| NVIDIA-SMI 418.116.00   Driver Version: 418.116.00   CUDA Version: N/A      |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce RTX 208...  Off  | 00000000:01:00.0 Off |                  N/A |
| 29%   35C    P8    23W / 250W |     10MiB / 10989MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```

!!! Note
    The container has access to __all__ GPU memory (10989 MiB).



Now, replace the term `docker` with `runai-docker` and add the argument `--gpu-memory 0.3`:

``` console hl_lines="10"
$ runai-docker run -it --rm --gpus 1 --gpu-memory 0.3 ubuntu nvidia-smi

+-----------------------------------------------------------------------------+
| NVIDIA-SMI 418.116.00   Driver Version: 418.116.00   CUDA Version: N/A      |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce RTX 208...  Off  | 00000000:01:00.0 Off |                  N/A |
| 30%   35C    P8    23W / 250W |      0MiB /  3296MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```

!!! Notes
    * `nvidia-smi` shows the user as having only 30% of GPU memory (3296 MiB).
    * Attempting to allocate beyond that amount will result in an out-of-memory error.

Similarly, one can pass an absolute amount of GPU memory. For example, passing `--gpu-memory 3g` would make the container accessible to 3GB of GPU memory.
