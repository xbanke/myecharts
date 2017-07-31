#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""

@version: 0.1??
@author:  quantpy
@email:   quantpy@qq.com
@file:    test_add.py
@time:    2017-07-31 13:43
"""


from __future__ import division, print_function
import numpy as np
import pandas as pd
import myecharts.myecharts as me


def test_add(*args, **kwargs):
    line = me.Line('Test Line add '+kwargs.get('data_type', ''))
    line.add(*args)
    line.show_config()
    line.render('./test_line_add_{}.html'.format(kwargs.get('data_type', '')))

    bar = me.Bar('Test Bar add '+kwargs.get('data_type', ''))
    bar.add(*args)
    bar.show_config()
    bar.render('./test_bar_add_{}.html'.format(kwargs.get('data_type', '')))


def test_add_df(df):
    line = me.Line('Test Line add_df')
    line.add_df(df)
    line.show_config()
    line.render('./test_line_add_df.html')

    bar = me.Bar('Test Bar add_df')
    bar.add_df(df)
    bar.show_config()
    bar.render('./test_bar_add_df.html')


def main():
    n = 100
    ss = pd.Series(np.random.randn(n).cumsum(), index=pd.date_range('20150101', periods=n), name='SeriesData')
    test_add(ss, data_type='series')

    dict_data = dict(ss)
    test_add('dict_data', dict_data, data_type='dict')

    list_tuple = [(k, v) for k, v in dict_data.items()]
    test_add('list_tuple', list_tuple, data_type='list_tuple')

    df = pd.DataFrame(np.random.randn(50, 5), index=pd.date_range('20150101', periods=50), columns=list('ABCDE'))
    test_add_df(df)
    

if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        print(repr(err))

