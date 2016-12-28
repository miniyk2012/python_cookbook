# -*- coding:utf-8 -*-
import logging

_logger = logging.getLogger(__name__)

# 你想实现一个自定义迭代模式，跟普通的内置函数比如 range() , reversed() 不一样。

# 如果你想实现一种新的迭代模式，使用一个生成器函数来定义它。

def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

for n in frange(0, 4, 0.5):
    print(n)


# 跟普通函数不同的是，生成器只能用于迭代操作
def countdown(n):
     print('Starting to count from', n)
     while n > 0:
         yield n
         n -= 1
     print('Done!')

# Create the generator, notice no output appears
c = countdown(3)
print(c)
print(next(c))
print(next(c))
print(next(c))
print(next(c))

for x in c:
    print('这里永远不会运行,因为c已经迭代结束了')
    print(x)

