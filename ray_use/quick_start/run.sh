gpu=$1
if [ -z $gpu ]; then
    gpu=5,6,7
fi
export PYTHONPATH='.'
export CUDA_VISIBLE_DEVICES=$gpu
# 
file=ray/quick_start/basic_train.py
python $file \
    2>&1  </dev/null | tee $file-gpu$gpu.log