# Dockerhub

Containts one stop of common environment prepareation for CUDA/ROCM by composing necessary dockerfiles with software SDK (CUDA/CUDNN/CuOpt/ROCM)

# Install

> pip install --verbose -e .

# Usage

## ROCM

To update SDK (defaults to /opt/rocm) to a specific version, execute the following scripts:

> ROCM_VERSION=6.3 bash rocm/update_sdk.sh

#### ROCM rocProfiler-compute (ncu)

ROCM profiler for kernels is now available in SDK 6.3.0 (not shipped with SDK). To use it, follows the instructions in [install rocprofiler-compute](rocm/install_rocprofiler-compute.sh) to install rocmProfiler-compute. See disscussion in https://github.com/ROCm/ROCm/issues/4082.

Usage example :

<img width="700" alt="Image" src="https://github.com/user-attachments/assets/c4cc406d-36d0-4b4e-9608-c56c4a02469a" />

If you setup machines in the following mananers

> local -> remote_head_node -> slurm_job_node -> docker/podman instance

I recommend you setup ssh reverse proxy to access rocProfiler-compute GUI client in a three easy steps:

###### Generate a profile

```
PROFILE_NAME=moe_align_16384x256
/opt/rocm-6.3.3/bin/rocprof-compute profile -p $PROFILE_NAME
```

###### Access GUI in local browser

You need to prepare three ttys

```
ROC_PROFILER_PORT=8085
LOCAL_GUI_HTTP_SERVICE_PORT=9001

# tty1
# ssh remote_head_node to listen to slurm job services
ssh -o ExitOnForwardFailure=yes -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -NTf -L 0.0.0.0:$LOCAL_GUI_HTTP_SERVICE_PORT:localhost:$ROC_PROFILER_PORT $slurm_job_host_name

# tty2
# open a new local tty
ssh -L $LOCAL_GUI_HTTP_SERVICE_PORT:localhost:$LOCAL_GUI_HTTP_SERVICE_PORT $remote_head_node

# tty3
# start rocProfiler-compute servcie
# ssh -j $remote_head_node $slurm_job_host_name
PROFILE_NAME=moe_align_16384x256 /opt/rocm-6.3.3/bin/rocprof-compute analyze -p workloads/$PROFILE_NAME/MI300X_A1/ --gui
```

## CUDA

pending...
