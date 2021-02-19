def to_1D(series):
	import pandas as pd
	"""
	variable should be Pandas Series
	"""
	return pd.Series([x for _list in series for x in _list])
