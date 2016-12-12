# -*- coding:utf-8 -*-
import logging

_logger = logging.getLogger(__name__)

# 你有一个字典列表，你想根据某个或某几个字典字段来排序这个列表。

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)


#  After f = itemgetter(2), the call f(r) returns r[2].
#  After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3])
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

max_by_uid = max(rows, key=itemgetter('uid'))
print(max_by_uid)