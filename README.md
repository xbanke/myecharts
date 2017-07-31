# myecharts
This lib is built on pyehcarts which make the method 'add' can handle np.ndarray and pd.Series. If the index is datetime, the value will be converted to '%Y-%m-%d'. Specially for pd.DataFrame, there is add_df that see the every column as a pd.Series, and draw them together.

在pyecharts基础上重载方法add，add可以识别pd.Series，将pd.Series.name, pd.Series.index, pd.Series.values 转为name attr data。
对于dict 和 二维list， 也可以自动匹配，但需额外给定name参数。
针对pd.DataFrame, 添加了方法add_df, 将每列看做pd.Series 绘制在一张图中。

另外，对于Iterable也会自动转为list

用法：

add(name, *iterables, **kwargs)

add(pd.Series, **kwargs)

add(name, dict, **kwargs)

add(name, list_tuple, **kwargs)

add_df(pd.DataFrame, **kwargs)
