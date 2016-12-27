
# -*- coding:utf-8 -*-
import logging

_logger = logging.getLogger(__name__)

# 你想去掉文本字符串开头，结尾或者中间不想要的字符，比如空白。
s = ' hello     world \n'
print(s.replace(' ', ''))
import re
print(re.sub('\s+', ' ', s))

with open('2_11.py') as f:
    lines = (line.strip() for line in f)
    for line in lines:
        if line != '':
            print(line)
