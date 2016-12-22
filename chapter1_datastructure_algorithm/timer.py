# -*- coding:utf-8 -*-

import contextlib, sys, time


@contextlib.contextmanager
def BlockTimer(label='Block'):
    """统计代码块运行时间
    用法：with BlockTimer('xxx'):
             code

    :param label:
    :return:
    """
    if sys.platform == "win32":
        timerFunc = time.clock
    else:
        timerFunc = time.time
    startTime = timerFunc()
    try:
        yield
    finally:
        endTime = timerFunc()
        print('%s =>' %label, end=' ')
        print('Time Elasped: %.3f msec.' % ((endTime-startTime)*1000.0))

