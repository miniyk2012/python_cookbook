# -*- coding:utf-8 -*-
import logging

_logger = logging.getLogger(__name__)

# 你构建了一个自定义容器对象，里面包含有列表、元组或其他可迭代对象。
# 你想直接在你的这个新容器对象上执行迭代操作。

# 实际上你只需要定义一个 __iter__() 方法，将迭代操作代理到容器内部的对象上去。比如：

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        """__iter__() 方法只是简单的将迭代请求传递给内部的 _children 属性。
        Python的迭代器协议需要 __iter__() 方法返回一个实现了 __next__() 方法的迭代器对象"""
        return iter(self._children)

# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    # Outputs Node(1), Node(2)
    # 下面三种形式是等价的
    print('1')
    for ch in root:
        print(ch)

    print('2')
    r = iter(root)
    print(next(r))
    print(next(r))


    print('3')
    r = root.__iter__()
    print(r.__next__())
    print(r.__next__())
