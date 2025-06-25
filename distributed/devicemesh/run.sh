export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7

root_dir=$(dirname $(realpath $0))
echo "Running device mesh script in $root_dir"
torchrun --nproc_per_node=8 $root_dir/devicemesh.py 2>&1 | tee $root_dir/2d_setup_with_device_mesh.log