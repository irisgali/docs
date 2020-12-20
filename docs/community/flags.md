
Following is a list and description of the `runai-docker` flags.


`--gpu-memory <fraction | absolute>`

> Exposes the container to a fraction of GPU memory or to a specific amount of it.

> A fraction should be a floating-point number greater than 0.0 and less than or equal to 1.0. At most two digits are allowed after the decimal point (e.g. `--gpu-memory 0.17`).
> An absolute specification must be an integer and is in bytes by default. Use the suffix `b` for bytes, `k` for kilobytes, `m` for megabytes and `g` for gigabytes (e.g. `--gpu-memory 3g` or `--gpu-memory 6543m`).

> The flag affects all GPUs which are accessible by the container. Meaning, if the container is accessible to more than a single GPU, then it is exposed to the same amount of memory of each and every one of the GPUs.

> Example:  `--gpu-memory 0.25` or `--gpu-memory 4g`


`--gpu-memory-request <fraction | absolute>`

> Request a portion of GPU memory to be available for the container at any time upon demand.

> This is most commonly used together with `--gpu-memory-limit` to allow dynamic memory usage.

> Example:  `--gpu-memory-request 0.25` or `--gpu-memory-request 2g`

!!! Important note
    This flag cannot be used together with `--gpu-memory`.


---
`--gpu-memory-limit <fraction | absolute>`

> Exposes the container to a portion of GPU memory for allocation if there's available memory. This is not guaranteed to be available and is a best-effort concept. The container is exposed to this limit and cannot exceed it.

> Example: `--gpu-memory-limit 0.75` or `--gpu-memory-limit 8g`

!!! Important note
    * This flag must be used together with `--gpu-memory-request` and be greater than or equal to it.
