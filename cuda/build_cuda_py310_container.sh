#! /bin/bash
IMG=docker.io/library/qwen-dev
tag=py310-cuda-dev-v1

docker_args=$(echo -it --privileged \
 --name $tag \
 --ulimit memlock=-1:-1 --net=host --cap-add=IPC_LOCK \
 --device=/dev/infiniband \
 --ipc=host \
 -v $(readlink -f `pwd`):/workspace \
 -v /data:/data \
 --workdir /workspace \
 --cpus=128 \
 $IMG
)

docker_args=($docker_args)

docker container create --gpus 4 "${docker_args[@]}"
