# Dockerhub

Containts one stop of common environment prepareation for CUDA/ROCM by composing necessary dockerfiles with software SDK (CUDA/CUDNN/CuOpt/ROCM)

# Install

> pip install --verbose -e .

# Usage

## ROCM

To update SDK (defaults to /opt/rocm) to a specific version, execute the following scripts:

> ROCM_VERSION=6.3 bash rocm/update_sdk.sh

## CUDA

pending...