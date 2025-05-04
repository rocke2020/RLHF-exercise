gpu=$1
if [ -z $gpu ]; then
    gpu=3,4,5,6
fi
export CUDA_VISIBLE_DEVICES=$gpu

# launch the master node of ray in container
# If you start a ray cluster with ray.init, the cluster should be killed when your 
# python program exists. If you start it with ray start, you can use the ray stop 
# command to shutdown the cluster. You can also use ray stop --force to forcefully 
# kill all processes left.
# ray start --head --node-ip-address 0.0.0.0 --num-gpus 4