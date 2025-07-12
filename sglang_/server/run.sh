#!/bin/bash

mkdir -p sglang_/server

python3 -m sglang.launch_server --model-path /data/models/Qwen/Qwen2.5-32B-Instruct \
  --served-model-name qwen25-32b-instruct \
  --host 0.0.0.0 \
  --port 34952 \
  2>&1 | tee sglang_/server/run.log