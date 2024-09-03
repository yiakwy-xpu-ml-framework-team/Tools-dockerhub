import os
import logging
from setuptools import find_packages, setup
import subprocess
from typing import List

try:
    import torch
    from torch.utils.cpp_extension import ROCM_HOME

    WITH_TORCH=True
    HIP_SDK_ROOT = ROCM_HOME
except:
    WITH_TORCH=False
    HIP_SDK_ROOT = "/opt/rocm"
    print("base env does not provide torch distribution")

## Constant
HIP_VERSION_PAT = r'HIP version: (\S+)'
# currently only support MI30X (MI308X, MI300XA) datacenter intelligent computing accelerator
ALLOWED_AMDGPU_ARCHS = ["gfx942"]

ROOT_DIR = os.path.dirname(__file__)

logger = logging.getLogger(__name__)

## ROCM helper
def _is_hip() -> bool:
    SDK_ROOT=f"{HIP_SDK_ROOT}"
    def _check_sdk_installed() -> bool:
        # return True if this dir points to a directory or symbolic link
        if not os.path.isdir(SDK_ROOT):
            return False

        result = subprocess.run([f"{SDK_ROOT}/bin/rocminfo", " | grep -o -m1 'gfx.*'"],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT,
                                text=True)
        
        if result.returncode != 0:
            print("Use AMD pytorch, but no devices found!")
            return False

        return True

    if not _check_sdk_installed():
        return False
    
    return True
    
def get_hipcc_rocm_version():
    assert _is_hip()

    result = subprocess.run(['hipcc', '--version'],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT,
                            text=True)

    # Check if the command was executed successfully
    if result.returncode != 0:
        print("Error running 'hipcc --version'")
        return None

    # Extract the version using a regular expression
    match = re.search(HIP_VERSION_PAT, result.stdout)
    if match:
        # Return the version string
        return match.group(1)
    else:
        print("Could not find HIP version in the output")
        return None

def get_path(*filepath) -> str:
    return os.path.join(ROOT_DIR, *filepath)

def get_requirements() -> List[str]:
    """Get Python package dependencies from requirements.txt."""

    def _read_requirements(prefix: str, filename: str) -> List[str]:
        with open(get_path(prefix + "/" + filename)) as f:
            requirements = f.read().strip().split("\n")
        resolved_requirements = []
        for line in requirements:
            if line.startswith("#"):
                continue
            if line.startswith("-r "):
                resolved_requirements += _read_requirements(prefix, line.split()[1])
            else:
                resolved_requirements.append(line)
                print(f"line : {line}")
        print(f"reqs : {resolved_requirements}")
        return resolved_requirements

    if _is_hip():
        requirements = _read_requirements("rocm", "requirements.txt")
    else:
        raise ValueError(
            "Unsupported platform, please use CUDA, ROCm")
    return requirements

if __name__ == "__main__":
    with open("README.md", "r") as f:
        long_description = f.read()
    fp = open("version.py", "r").read()
    version = eval(fp.strip().split()[-1])

    setup(
        name="dockerhub",
        author="yiakwy-xpu-framework-team",
        author_email="yiak.wy@gmail.com",
        packages=find_packages(),
        install_requires=get_requirements(),
        url="https://github.com/yiakwy-xpu-ml-framework-team/Tools-dockerhub.",
        description="onestop : heterogeneous computing dependencies",
        long_description=long_description,
        long_description_content_type="text/markdown",
        version=version,
        classifiers=[
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
        ],
        include_package_data=True,
        python_requires=">=3.10",
    )