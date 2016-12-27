# -*- coding:utf-8 -*-
import logging

_logger = logging.getLogger(__name__)

# 你想遍历一个可迭代对象中的所有元素，但是却不想使用for循环。
def manual_iter():
    with open('4_1.py') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass

manual_iter()

with open('4_1.py') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')
print()
# 大多数情况下，我们会使用 for 循环语句用来遍历一个可迭代对象。
#  但是，偶尔也需要对迭代做更加精确的控制，这时候了解底层迭代机制就显得尤为重要了。
items = [1, 2, 3]
# it = items.__iter__()
it = iter(items)
print(it.__next__())
print(next(it))
print(next(it))
print(next(it))