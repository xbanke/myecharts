#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""

@version: 0.1??
@author:  quantpy
@email:   quantpy@qq.com
@file:    __init__.py.py
@time:    2017-07-25 13:24
"""

import pyecharts as pe
from .charts import add, add_df


for __name in dir(pe):
    if __name[0].isupper():
        locals()[__name] = type(__name, (getattr(pe, __name), ), {'add': add, 'add_df': add_df})

