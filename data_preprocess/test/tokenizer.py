import os
import psutil
import timeit
from datasets import load_dataset
import logging
from transformers import AutoTokenizer
from icecream import ic
import platform


ic.configureOutput(includeContext=True, argToStringFunction=str)
ic.lineWrapWidth = 120

REPO_ID = "Qwen/Qwen2.5-0.5B-Instruct"

if platform.system() == "Windows":
    SAVE_DIR = f"D:/models/{REPO_ID}"
else:
    SAVE_DIR = f"/data/model/{REPO_ID}"

tokenizer = AutoTokenizer.from_pretrained(SAVE_DIR)

content = 'I want to book a flight from New York to Shanghai.'
chat = [{"role": "system", "content": "你是智能助手"}, {"role": "user", "content": content}]
# If no system, use the default system role from model inside.
prompt = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)
ic(prompt)