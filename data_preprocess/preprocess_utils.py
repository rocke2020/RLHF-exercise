import json
import math
import os
import random
import re
import shutil
import sys
import time
from collections import defaultdict
from pathlib import Path
from datetime import datetime

from loguru import logger


def partition_list(lst, num_partitions):
    """
    Split a list into num_partitions roughly equal parts.

    e.g.
    partition_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
    returns [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]

    partition_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 3)
    returns [[1, 2, 3, 4], [5, 6, 7, 8], [8, 9, 10]]
    """
    k, m = divmod(len(lst), num_partitions)
    return [
        lst[i * k + min(i, m) : (i + 1) * k + min(i + 1, m)]
        for i in range(num_partitions)
    ]


def zipngram(text: str, ngram_size: int):
    """Easy to understand version of zipngram
    hello world this is a test
    n-gram为3，切分为
    [('hello', 'world', 'this'), ('world', 'this', 'is'), ('this', 'is', 'a'), ('is', 'a', 'test')]
    n-gram为4，切分为
    [('hello', 'world', 'this', 'is'), ('world', 'this', 'is', 'a'), ('this', 'is', 'a', 'test')]
    """
    words = text.lower().split()
    res = [(words[i : i + ngram_size]) for i in range(len(words) - ngram_size + 1)]
    return res


def zipngram_hard_to_read(text: str, ngram_size: int):
    """
    hello world this is a test
    n-gram为3，切分为
    [('hello', 'world', 'this'), ('world', 'this', 'is'), ('this', 'is', 'a'), ('is', 'a', 'test')]
    n-gram为4，切分为
    [('hello', 'world', 'this', 'is'), ('world', 'this', 'is', 'a'), ('this', 'is', 'a', 'test')]
    """
    words = text.lower().split()
    return zip(*[words[i:] for i in range(ngram_size)])


if __name__ == "__main__":
    logger.info("end")
