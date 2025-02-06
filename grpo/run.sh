export CUDA_VISIBLE_DEVICES=2
export HF_ENDPOINT=https://hf-mirror.com
# 
file=grpo/train.py
echo CUDA_VISIBLE_DEVICES=$CUDA_VISIBLE_DEVICES > $file-nohup.log
nohup python $file \
    >> $file-nohup.log 2>&1 &