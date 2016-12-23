# -*- coding:utf-8 -*-
import logging

_logger = logging.getLogger(__name__)

# 现在有多个字典或者映射，你想将它们从逻辑上合并为一个单一的映射后执行某些操作， 比如查找值或者检查某些键是否存在。

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
from collections import ChainMap
# 一个 ChainMap 接受多个字典并将它们在逻辑上变为一个字典。 然后，这些字典并不是真的合并在一起了， ChainMap 类只是在内部创建了一个容纳这些字典的列表
c = ChainMap(a,b)
print(c['x'])  # Outputs 1 (from a)
print(c['y'])  # Outputs 2 (from b)
# 如果出现重复键，那么第一次出现的映射值会被返回。 因此，例子程序中的 c['z'] 总是会返回字典 a 中对应的值，而不是 b 中对应的值。
print(c['z'])  # Outputs 3 (from a)

print(list(c.values()))
print(list(c.keys()))
a['y'] = 10
for x, y in c.items():
    print(x, y)

values = ChainMap()
values['x'] = 5
print(values)
values = values.new_child()
values['x'] = 4
print(values)
values = values.parents
print(values)
values = values.parents
print(values)
values = values.parents
print(values)
values = values.parents
print(values)


