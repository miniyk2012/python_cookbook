# -*- coding:utf-8 -*-
import logging

_logger = logging.getLogger(__name__)

line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
print(re.split(r'[;,\s]\s*', line))
print(re.split(r'(?:,|;|\s)\s*', line))
