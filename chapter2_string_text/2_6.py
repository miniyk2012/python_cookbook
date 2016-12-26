# -*- coding:utf-8 -*-
import logging, re

_logger = logging.getLogger(__name__)

# 你需要以忽略大小写的方式搜索与替换文本字符串
text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags=re.IGNORECASE))
print(re.sub('python', 'snake', text, flags=re.IGNORECASE))

def change_python(m):
    return 'snake'
print(re.sub('python', change_python, text, flags=re.IGNORECASE))

def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))


