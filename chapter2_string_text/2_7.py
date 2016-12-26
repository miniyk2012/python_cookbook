# -*- coding:utf-8 -*-
import logging, re

_logger = logging.getLogger(__name__)


str_pat = re.compile(r'\"(.*)\"')  # 点(.)匹配除了换行外的任何字符
text1 = 'Computer says "no."'
print(str_pat.findall(text1))
text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))  # findall匹配分组中的数据

print('非贪婪模式')  #  通过在 * 或者 + 这样的操作符后面添加一个 ? 可以强制匹配算法改成寻找最短的可能匹配。
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))