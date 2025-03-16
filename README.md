# Dockerhub

Containts one stop of common environment prepareation for CUDA/ROCM by composing necessary dockerfiles with software SDK (CUDA/CUDNN/CuOpt/ROCM)

# Install

> pip install --verbose -e .

# Usage

## ROCM

To update SDK (defaults to /opt/rocm) to a specific version, execute the following scripts:

> ROCM_VERSION=6.3 bash rocm/update_sdk.sh

#### ROCM rocProfiler-compute (ncu)

ROCM profiler for kernels is now available in SDK 6.3.0 (not shipped with SDK). TO use it, follows the instructions in [install rocprofiler-compute](rocm/install_rocprofiler-compute.sh). See disscussion in https://github.com/ROCm/ROCm/issues/4082.


Usage example :

<img width="700" alt="Image" src="https://github.com/user-attachments/assets/f7cf274f-0d72-43e7-84b8-93990ade0309" />


## CUDA

pending...
