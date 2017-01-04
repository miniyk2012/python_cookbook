# -*- coding:utf-8 -*-
import logging

_logger = logging.getLogger(__name__)


import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('{}.{} : {}'.format(func.__module__, func.__name__, end - start))
        return r
    return wrapper

@timethis
def countdown(n):
    while n > 0:
        n -= 1

# countdown(10000000)

from timeit import timeit
print timeit('math.sqrt(2)', 'import math')  # default_number = 1000000