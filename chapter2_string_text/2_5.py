# -*- coding:utf-8 -*-
import logging, re

_logger = logging.getLogger(__name__)

# 你想在字符串中搜索和匹配指定的文本模式
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# sub() 函数中的第一个参数是被匹配的模式，第二个参数是替换模式。反斜杠数字比如 \3 指向前面模式的捕获组号。
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))

# 对于更加复杂的替换，可以传递一个替换回调函数来代替
from calendar import month_abbr
def change_date(m):
    """
    一个替换回调函数的参数是一个 match 对象，也就是 match() 或者 find() 返回的对象。
    使用 group() 方法来提取特定的匹配部分。回调函数最后返回替换字符串。
    :param m:
    :return:
    """
    mon_name = month_abbr[int(m.group(1))]  # 将数字转换为月份
    ret = '{} {} {}'.format(m.group(2), mon_name, m.group(3))
    print('*', ret)
    return ret
print(datepat.sub(change_date, text))

# 如果除了替换后的结果外，你还想知道有多少替换发生了，可以使用 re.subn() 来代替。
newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext)
print(n)
print('*'.center(100, '-'))
newtext, n = datepat.subn(change_date, text)
print(newtext)
print(n)
