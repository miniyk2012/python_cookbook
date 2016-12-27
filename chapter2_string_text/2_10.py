# -*- coding:utf-8 -*-
import logging, re

_logger = logging.getLogger(__name__)

# 你正在使用正则表达式处理文本，但是关注的是Unicode字符处理。 不去关注这些
num = re.compile('\d+')
mobj = num.match('123')
print(mobj)

print(num.match('\u0661\u0662\u0663'))

arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')