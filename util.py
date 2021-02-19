def to_list(series):
	"""
	variable is a list stored as string in DataFrame
	"""		
	from ast import literal_eval
	series = series.apply(literal_eval)
	return series

def to_1D(series):
	"""
	variable should be Pandas Series
	"""
	import pandas as pd 
	return pd.Series([x for _list in series for x in _list])
