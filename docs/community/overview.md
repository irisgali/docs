# Overview

Docker allows the allocation of a specified amount of CPU memory for a container.
This is achieved by specifying the required memory as a flag. E.g., `docker run --memory 1GB`.

This project provides similar capabilities for GPUs.

By using `runai-docker` one could isolate a portion of the GPU memory for a specific container.

## Example

Using a GeForce RTX 2080 Ti GPU with 11GB RAM. Replace `docker` with `runai-docker` and add the argument `--gpu-memory 0.3`:

```
$ runai-docker run -it --rm --gpus 1 --gpu-memory 0.3 ubuntu nvidia-smi

Wed Oct 28 08:46:21 2020
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

`nvidia-smi` shows the user as having only 30% of GPU memory. Attempting to allocate beyond that amount will result in an out-of-memory error.

Running the same without `runai-docker` and `--gpu-memory` results in the container being accessible to all GPU memory:

> Trimmed for the sake of comparison
```
$ docker run -it --rm --gpus 1 ubuntu nvidia-smi
...
|===============================+======================+======================|
|   0  GeForce RTX 208...  Off  | 00000000:01:00.0 Off |                  N/A |
| 29%   35C    P8    23W / 250W |     10MiB / 10989MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
...
```
