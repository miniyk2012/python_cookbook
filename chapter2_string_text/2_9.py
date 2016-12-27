# -*- coding:utf-8 -*-
import logging

_logger = logging.getLogger(__name__)

# 你正在处理Unicode字符串，需要确保所有字符串在底层有相同的表示。
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
print(s2)

# 关于unicode的东东是一个很大的主题,不再仔细考虑了
