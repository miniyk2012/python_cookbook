# -*- coding:utf-8 -*-
import logging

_logger = logging.getLogger(__name__)


url = 'http://www.python.org'
print(url.startswith('http:'))

import os
filenames = os.listdir('../')
print(filenames)
print([name for name in filenames if name.endswith(('algorithm', '.md'))])
print(any(name.endswith('.idea') for name in filenames))

choices = ['http:', 'ftp:']
url = 'http://www.python.org'
print(url.startswith(tuple(choices)))

import re
url = 'http://www.python.org'
print(bool(re.match('http:|https:|ftp:', url)))
print(url.startswith(('http:', 'https:', 'ftp:')))
