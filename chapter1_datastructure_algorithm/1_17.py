# -*- coding:utf-8 -*-
import logging
from timer import BlockTimer

_logger = logging.getLogger(__name__)


# 你想构造一个字典，它是另外一个字典的子集。
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# Make a dictionary of all prices over 200
with BlockTimer('字典推导'):
    p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)
# Make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
with BlockTimer('字典/判断'):
    p2 = {key: value for key, value in prices.items() if key in tech_names}
print(p2)

with BlockTimer('元组序列'):
    p1 = dict((key, value) for key, value in prices.items() if value > 200)

tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
with BlockTimer('字典/集合'):
    p2 = {key: prices[key] for key in (prices.keys() & tech_names)}
print(p2)


