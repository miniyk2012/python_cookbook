# -*- coding:utf-8 -*-
import logging

_logger = logging.getLogger(__name__)

# 你想构建一个能支持迭代操作的自定义对象，并希望找到一个能实现迭代协议的简单方法。
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


# Python的迭代协议要求一个 __iter__() 方法返回一个特殊的迭代器对象，
# 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。
class Node2:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        return DepthFirstIterator(self)


class DepthFirstIterator(object):
    '''
    Depth-first traversal
    '''

    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        # Return myself if just started; create an iterator for children
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node
        # If processing a child, return its next item
        elif self._child_iter:
            try:
                nextchild = next(self._child_iter)
                return nextchild
            except StopIteration:
                self._child_iter = None
                return next(self)
        # Advance to the next child and start its iteration
        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)

def test1():
    print('test1'.center(100, '-'))
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)

def test2():
    print('test2'.center(100, '-'))
    root = Node2(0)
    child1 = Node2(1)
    child2 = Node2(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node2(3))
    child1.add_child(Node2(4))
    child2.add_child(Node2(5))
    for ch in root.depth_first():
        print(ch)
# Example
if __name__ == '__main__':
    test1()
    test2()