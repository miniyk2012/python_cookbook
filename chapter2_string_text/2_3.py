# -*- coding:utf-8 -*-
import logging

_logger = logging.getLogger(__name__)


# 你想使用 Unix Shell 中常用的通配符(比如 *.py , Dat[0-9]*.csv 等)去匹配文本字符串

from fnmatch import fnmatch, fnmatchcase

names = ['Dat1.csv', 'Dat22.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat?.csv')])

print(fnmatchcase('foo.txt', '*.txt'))

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

print([addr for addr in addresses if fnmatchcase(addr, '* ST')])
print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])

# fnmatch() 函数匹配能力介于简单的字符串方法和强大的正则表达式之间。
# 如果在数据处理操作中只需要简单的通配符就能完成的时候，这通常是一个比较合理的方案。