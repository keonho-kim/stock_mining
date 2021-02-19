def to_1D(series):
	"""
	variable should be Pandas Series
	"""
	return pd.Series([x for _list in series for x in _list])
