# myecharts
This lib is built on pyehcarts which make the method 'add' can handle np.ndarray and pd.Series. If the index is datetime, the value will be converted to '%Y-%m-%d'. Specially for pd.DataFrame, there is add_df that see the every column as a pd.Series, and draw them together.
