# -*- coding:utf-8 -*-
import logging

_logger = logging.getLogger(__name__)

# 你想排序类型相同的对象，但是他们不支持原生的比较操作。
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sort_notcompare():
    users = [User(23), User(3), User(99)]
    print(users)
    # print(sorted(users))  # unorderable types: User() < User()
    print(sorted(users, key=lambda u: u.user_id))
    from operator import attrgetter
    print(sorted(users, key=attrgetter('user_id')))

if __name__ == '__main__':
    sort_notcompare()
