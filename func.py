def clean_alt_list(list_):
	list_ = list_.replace(', ', '","')
	list_ = list_.replace('[', '["')
	list_ = list_.replace(']', '"]')
	return list_
