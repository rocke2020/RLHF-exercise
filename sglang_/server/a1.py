from sglang.test.test_utils import is_in_ci
from sglang.utils import wait_for_server, print_highlight, terminate_process

if is_in_ci():
    from patch import launch_server_cmd
else:
    from sglang.utils import launch_server_cmd

# This is equivalent to running the following command in your terminal

# python3 -m sglang.launch_server --model-path /data/models/Qwen/Qwen2.5-32B-Instruct --host 0.0.0.0 --served-model-name qwen25-32b-instruct

server_process, port = launch_server_cmd(
    """
python3 -m sglang.launch_server --model-path /data/models/Qwen/Qwen2.5-32B-Instruct \
  --served-model-name qwen25-32b-instruct \
  --host 0.0.0.0 \
  --port 34952 \
"""
)

wait_for_server(f"http://localhost:{port}")