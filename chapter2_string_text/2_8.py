# -*- coding:utf-8 -*-
import logging, re

_logger = logging.getLogger(__name__)

# 你正在试着使用正则表达式去匹配一大块的文本，而你需要跨越多行去匹配。
# 这个问题很典型的出现在当你用点(.)去匹配任意字符的时候，忘记了点(.)不能匹配换行符的事实。
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
multiline a comment */
'''
print(comment.findall(text1))
print(comment.findall(text2))

# 可以修改模式字符串，增加对换行的支持
comment = re.compile(r'/\*((?:.|\n)*?)\*/')  # (?:.|\n) 指定了一个非捕获组 (也就是它定义了一个仅仅用来做匹配，而不能通过单独捕获或者编号的组)
print(comment.findall(text2))

# re.compile() 函数接受一个标志参数叫 re.DOTALL ，在这里非常有用。 它可以让正则表达式中的点(.)匹配包括换行符在内的任意字符。
print('re.DOTALL')
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2))


