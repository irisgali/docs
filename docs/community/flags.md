
Following is a list and description of the `runai-docker` flags.


`--gpu-memory <fraction>` 

> Exposes the container to a portion of GPU memory. 

> The fraction should be a floating-point number greater than 0.0 and less than or equal to 1.0. At most two digits are allowed after the decimal point (e.g. `0.17`).

> The flag affects all GPUs which are accessible by the container. Meaning, if the container is accessible to more than a single GPU, then it is exposed to the same portion of each and every one of the GPUs.

> Example:  `--gpu-memory 0.25`


`--gpu-memory-request <fraction>` 

> Request a portion of GPU memory to be available for the container at any time upon demand.

> This is most commonly used together with `--gpu-memory-limit` to allow dynamic memory usage.

> Example:  `--gpu-memory-request 0.25`

!!! Important note
    This flag cannot be used together with `--gpu-memory`.


---
`--gpu-memory-limit <portion>` 

> Exposes the container to a portion of GPU memory for allocation if there's available memory. This is not guaranteed to be available and is a best-effort concept. The container is exposed to this limit and cannot exceed it.

> Example: `--gpu-memory-limit 0.75`

!!! Important note
    * This flag must be used together with `--gpu-memory-request` and be greater than or equal to it.
    * This flag must be used together with `--gpu-memory-request`.


