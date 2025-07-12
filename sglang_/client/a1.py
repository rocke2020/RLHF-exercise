import requests
from sglang.utils import print_highlight


port = 34952
url = f"http://localhost:{port}/v1/chat/completions"

data = {
    "model": "qwen25-32b-instruct",
    "messages": [{"role": "user", "content": "What is the capital of France?"}],
}

response = requests.post(url, json=data)
print_highlight(response.json())