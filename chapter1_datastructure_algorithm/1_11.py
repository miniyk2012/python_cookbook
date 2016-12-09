import logging

_logger = logging.getLogger(__name__)

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 6, 1)
print(items[a])

items[a] = [10,11,12]
print(items)

del items[a]
print(items)

b = slice(5, 50, 2)
print(b.start)
print(b.stop)
print(b.step)
print('*'*10)
s = 'HelloWorld'
print(b.indices(len(s)))
for i in range(*b.indices(len(s))):
    print(s[i])