gpu=$1
if [ -z $gpu ]; then
    gpu=1,2,3,4,5,6,7
fi
export CUDA_VISIBLE_DEVICES=$gpu

# launch the master node of ray in container
ray start --head --node-ip-address 0.0.0.0 --num-gpus 7