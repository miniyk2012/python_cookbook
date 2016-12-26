# -*- coding:utf-8 -*-
import logging

_logger = logging.getLogger(__name__)

# 你想匹配或者搜索特定模式的文本
text = 'yeah, but no, but yeah, but no, but yeah'
# Exact match
text == 'yeah'
# Match at start or end
print(text.startswith('yeah'))
print(text.endswith('no'))
# Search for the location of the first occurrence
print(text.find('no'))

# 正则表达式
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
import re
# Simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')
# 想使用同一个模式去做多次匹配，应该先将模式字符串预编译为模式对象
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text2):
    print('yes')
else:
    print('no')

# match() 总是从字符串开始去匹配，如果你想查找字符串任意部分的模式出现位置， 使用 findall() 方法去代替
text = 'Today is 11/27/2012. PyCon starts 03/13/2013.'
print(datepat.findall(text))


# 在定义正则式的时候，通常会利用括号去捕获分组。比如：
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())
month, day, year = m.groups()
print("# text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'")
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# findall() 方法会搜索文本并以列表形式返回所有的匹配。
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(type(datepat.findall(text)))
print(datepat.findall(text))
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))

# 如果你想以迭代方式返回匹配，可以使用 finditer() 方法来代替
print(type(datepat.finditer(text)))
for m in datepat.finditer(text):
    print(m.groups())
