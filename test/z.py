import logging
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
import torch.optim as optim
from icecream import ic
from pandas import DataFrame
from torch import nn
from torch.utils import data
from tqdm import tqdm
from loguru import logger


SEED = 0
np.random.seed(SEED)
torch.manual_seed(SEED)
torch.cuda.manual_seed_all(SEED)

print("Hello, World!")
XML_COT_FORMAT = """\
<reasoning>
</reasoning>
<answer>
</answer>\
"""
r = XML_COT_FORMAT.split("\n</answer>")
print(r)