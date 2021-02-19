def Clean_List_in_DF(list_):
	list_ = list_.replace(', ', '","')
	list_ = list_.replace('[', '["')
	list_ = list_.replace(']', '"]')
	return list_
