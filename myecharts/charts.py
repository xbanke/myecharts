#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""

@version: 0.1??
@author:  quantpy
@email:   quantpy@qq.com
@file:    charts.py
@time:    2017-07-25 12:59
"""


from __future__ import division, print_function
import numpy as np
import pandas as pd


def formatter(t):
    if isinstance(t, pd.Timestamp):
        return t.strftime('%Y-%m-%d')
    try:
        t = float(t)
    except:
        try:
           t = str(t)
        except:
            raise
    return t


def tolist(*args):
    if len(args) == 1 and isinstance(args[0], pd.Series):
        ss = args[0]
        args = [ss.name, ss.index, ss.values]

    if len(args) == 2:
        arg1 = args[1]
        args = [args[0]]
        try:
            if isinstance(arg1, dict):
                args.extend([list(arg1.keys()), list(arg1.values())])
            else:
                args.extend([[k[0] for k in arg1], [k[1] for k in arg1]])
        except:
            raise

    try:
        name = str(args[0])
    except UnicodeEncodeError:
        name = args[0]
    args_ = [name]
    for arg in args[1:]:
        if isinstance(arg, np.ndarray):
            try:
                arg = arg.astype(float).tolist()
            except:
                arg = arg.astype(str).tolist()
        else:
            arg = list(map(formatter, arg))
        args_.append(arg)
    return args_


def add(self, *args, **kwargs):
    args = tolist(*args)
    super(self.__class__, self).add(*args, **kwargs)
    return


def add_df(self, df, **kwargs):
    for col in df.columns:
        self.add(df[col], **kwargs)

