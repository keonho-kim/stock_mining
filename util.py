def clean_setup(stock_list):
	"""
	The function returns 4 list and 1 dict
	- tickers (list) : tickers
	- dollar_tickers (list) : $ + ticker(upper)
	- dollar_tickers_lower (list) : $+ticker(lower)
	- stock_name (list) : full text of comany name
	- company_dict (dict) : dictionary with full text of company name : tickers
	"""

	import pandas as pd
	pd.set_option('mode.chained_assignment',  None)

	import nltk
	from nltk.corpus import stopwords
	import string
	import re

	nltk.download('stopwords')
	li_stopwords = [word.upper() for word in list(stopwords.words('english'))]
	stopword = set(li_stopwords)

	alphabets = list(string.ascii_uppercase)
	eliminated_equities = ['CEO', 'USD', 'USA', 'LOVE', 'HOPE', 'YOLO']

	eliminated_equities = eliminated_equities + alphabets
	eliminated_equities = set(eliminated_equities)

	symbols = set(stock_list['Symbol'])
	adjusted_symbols = symbols.difference(stopword)
	adjusted_symbols = adjusted_symbols.difference(eliminated_equities)

	tickers = adjusted_symbols
	dollar_tickers = set(['$' + ticker for ticker in adjusted_symbols])
	dollar_tickers_lower = set(['$' + ticker.lower()
	                           for ticker in adjusted_symbols])

	stock_name = stock_list[stock_list['Market'].isin(['NYSE', 'NASDAQ'])]
	stock_name = list(stock_name['Name'])
	stock_name = [name.split(' ')[0]
	                         for name in stock_name if 'Acquisition' not in name.split(' ')]
	stock_name = set(stock_name).difference(alphabets)

	removed_company_name = ['Walt', 'United', 'Sea', 'General', 'S&P', 'British', 'U.S.', 'Southern', 'Global', 'Palo', 'American', 'MSCI', 'VF', 'Zimmer', 'Kinder', 'American', 'Southwest', 'Ball', 'Sun', 'Arthur', 'Edison', 'Kansas', 'Invitation', 'China', 'Boston', 'Korea', 'W.', 'Universal', 'Advanced', 'Lincoln', 'Globel', 'First', 'West', 'Shaw', 'Texas', 'Ralph', 'Churchill',
                        'US', 'Western', 'Host', 'Federal', 'National', 'Bloom', 'Affiliated', 'Life', 'Tim', 'Inspire', 'Apartment', 'Choice', 'New', 'Innovative', 'Clean', 'Switch', 'Bank', 'Canada',
                        'Healthcare', 'John', 'Agree', 'Ryman', 'Spirit', 'Black', 'Portland', 'Physicians', 'Hawaiian', 'Select', 'International', 'Armstrong', 'John', 'World', 'Data', 'Micro', 'Stewart',
                        'Exponent', 'Stealth', 'Liberty', 'Sigma', 'Arena', 'Level', 'Park', 'Thomson', 'Strategic', 'Medical', 'So-Young', 'News', 'BBQ', 'Berry', 'Wisdom', 'Capital', 'Comfort', 'Graphic',
                        'T.', 'Security', 'Optical', 'Homology', 'Coherent', 'Daily', 'East', 'Code', 'Range', 'Cumulus', 'PDF', 'At', 'Dime', 'Gemini', '908', 'Beyond', 'Boot', 'Helen', 'JD.com', 'Digital',
                        'Pivotal', 'one', 'Universal', 'Vale', 'Albany', 'Communications', 'Sprout', 'Driven', 'Santander', 'Consumers', 'Spark', 'Tutor', 'County', 'Diana', 'Lithium', 'Check', 'Just',
                        'Intrusion', 'Predictive', 'Amazon.com', 'STORE', 'Gold', 'Verb', 'Watford', 'Root', 'Surgery', 'Assured', 'CC', 'Progress', 'Construction', 'Rafael', 'Iridium', 'Japan', 'Malibu',
                        'Phoenix', 'Purple', 'Marin', 'High', 'Tower', 'Achieve', 'Equity', 'Sportsmans', 'Waters', 'Frontline', 'Scholar', 'Live', 'Laboratory', 'Bio', 'Science', 'Neuronetics', 'Edawards',
                        'Simmons', 'Assembly', 'Turning', 'Joint', 'Utah', 'Community', 'Kentucky', 'Baker', 'Trillium', 'Delaware', 'Site', 'Campbell', 'Quest', 'Soughside', 'Gravity', 'Newmont', 'Century',
                        'Foreign', 'Home', 'Wrap', 'Lee', 'Yum!', 'Cushman', 'Core', 'Vail', 'Five', 'Fortune', 'Educational', 'Renewable', 'Prospect', 'USA', 'Health', 'Noble', 'Rush', 'Planet', 'Discovery',
                        'Commercial', 'Box', 'Motive', 'Regional', 'Ajax', 'Pennsylvania', 'Patrick', 'Magic', 'Patria', 'Burning', 'Sleep', 'Bicycle', 'Revolve', 'Infinity', 'Passage', 'Ethan', 'Alto', 'Granite',
                        'Rio', 'Simpston', 'Tortoise', 'Shoe', 'Marsh', 'Enterprise', 'Bright', 'Model', 'Buckle', 'Ark', 'Stitch', 'Partner', 'Ultra', 'Nano', 'Brown', 'Viper', 'Arlington', 'Container', 'Natures',
                        'James', 'Citizens', 'Option', 'Academy', 'York', 'Red', 'Tyler', 'Canadian', 'Premier', 'Thrid', 'Chart', 'Waste', 'Charter', 'Center', 'Aqua', 'Takeda', 'Leo', 'Shell', 'Cable', 'Arrow',
                        'Open', 'Myriad', 'Cambridge', 'Minerva', 'Aluminum', 'Drive', 'NOW', 'Group', 'Social', 'Gulf', 'Agile', 'Plus', 'Elastic', 'Spire', 'Eastern', 'State', 'Oriental', 'Urban', 'Scotts', 'E.',
                        'Nomad', 'Innate', 'Sensei', 'Watts', 'Ross', 'Under', 'Natural', 'Sally', 'Workhorse', 'Atlantic', 'Mason', '890', 'Republic', 'Rise', 'Clip', 'Tuscan', 'Oaktree', 'Hill', 'Duke', 'Guild',
                        'Gray', 'Velocity', 'Harvest', 'Mr.', 'Nice', 'Image', 'Crawford', 'Old', 'Element', 'Aspire', 'Fair', '17', 'Onto', 'Vision', 'USD', 'Carter', 'Generation', 'Second', 'Owl', 'Pure', 'Taiwan',
                        'Team', 'Northern', 'Canterbutty', ' Bug', 'Pros', 'Whole', 'Enable', 'Artisan', 'Iron', 'Insight', 'Harbor', 'Carnival', 'Camping', 'Regions', 'Norfolk', 'Genesis', ' Solaris', 'Kernel', 'Plug',
                        'Phantom', 'Oxford', 'Energy', 'Matthews', 'Nine', 'Tattooed', 'NCS', 'Inspired', 'Navigator', 'Advanced', 'Safe', 'Smart', 'Sphere', 'Protective', 'My', 'Population', 'A.', 'Forum', 'Polar',
                        'Glory', 'Moody\'s', 'California', 'Diamond', 'Foresight', 'Moog', 'Cooper', 'Cowen', 'Allstate', 'Air', 'Concord', 'Rogers', 'Kelly', 'Quotient', 'MTBC', 'Summit', 'Heico', 'Acadia', 'Vector',
                        'Central', 'Fox', 'Unilever', 'Cogent', 'HEICO', 'Juniper', 'Asia', 'Delta']

	stock_name = stock_name.difference(set(removed_company_name))

	stock_list['company_name'] = None

	for i in range(len(stock_list)):
 	   stock_list['company_name'][i] = stock_list['Name'][i].split(' ')[0]

	company_dict = dict()

	for name in stock_name:
		subset = stock_list[stock_list['company_name'] == name]
		if len(subset)>1:
			continue
		else:
			company_dict[name] = subset['Symbol'].iloc[0]

	company_dict['Amazon'] = 'AMZN'
	company_dict['Yum'] = 'YUM'

	stock_name = list(company_dict.keys())

	return tickers, dollar_tickers, dollar_tickers_lower, stock_name, company_dict


def clean_submssion(submissions, tickers, dollar_tickers, dollar_tickers_lower, stock_name, company_dict):
	"""
	The function will extract tiem and mentioned companies from submission dataset
	Three columns will be created in original pandas dataframe:
	- time: exact time an article is created
	- title_mentione_tickers: companies mentioned in title text
	- body_mentioned_tickers: companies mentioned in body text
	"""
	import datetime
	import pandas as pd
	import string
	import re
	import numpy as np
	import os
	import time
	os.environ['TZ'] = 'America/New_York'
	time.tzset()

	submissions['time'] = None
	submissions['title_mentioned_tickers'] = None
	submissions['body_mentioned_tickers'] = None
	
	for idx in range(len(submissions)):
		submissions['time'][idx] = datetime.datetime.fromtimestamp(submissions['created_utc'][idx]).strftime('%Y-%m-%d-%H-%M')

		if type(submissions['title'][idx]) != float:
			# Extract mentioned tickers in title 
				# Eliminate speical letters in title
			title_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#%&\\\=\(\'\"]', ' ', submissions['title'][idx])
			title_text = set(title_text.split())
				# Extract mentioned tickers in title 
			title_tickers_intersec = title_text.intersection(tickers)
			title_tickers_intersec = list(title_tickers_intersec)
			
			title_dollar_tickers_intersec = title_text.intersection(dollar_tickers)
			title_dollar_tickers_intersec = list(title_dollar_tickers_intersec)

			title_dollar_tickers_lower_intersec = title_text.intersection(dollar_tickers_lower)
			title_dollar_tickers_lower_intersec = list(title_dollar_tickers_lower_intersec)
			
			title_mentioned_companies = list(title_text.intersection(stock_name))

			title_mentioned_tickers = list(set(title_tickers_intersec + 
											[item.replace('$', '') for item in title_dollar_tickers_intersec] + 
											[item.upper().replace('$', '') for item in title_dollar_tickers_lower_intersec] +
											[company_dict[c] for c in title_mentioned_companies]))

			submissions['title_mentioned_tickers'][idx] = title_mentioned_tickers

		else:
			submissions['title_mentioned_tickers'][idx] = np.nan

		if type(submissions['selftext'][idx]) != float:
			# Extract mentioned tickers in body (selftext)
				# Eliminate speical letters in body
			body_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#%&\\\=\(\'\"]', '', str(submissions['selftext'][idx]))
			body_text = re.sub('\n', '', body_text)
			body_text = set(body_text.split())
				# Extract mentioned tickers in body 
			body_tickers_intersec = list(body_text.intersection(tickers))
			body_dollar_tickers_intersec = list(body_text.intersection(dollar_tickers))
			body_dollar_tickers_lower_intersec = list(body_text.intersection(dollar_tickers_lower))
			body_mentioned_companies = list(body_text.intersection(stock_name))

			body_mentioned_tickers = list(set(body_tickers_intersec +
											[item.replace('$', '') for item in body_dollar_tickers_intersec] + 
											[item.upper().replace('$', '') for item in body_dollar_tickers_lower_intersec] +
											[company_dict[c] for c in body_mentioned_companies]))
			
			submissions['body_mentioned_tickers'][idx] = body_mentioned_tickers
			
		else:
			submissions['body_mentioned_tickers'][idx] = np.nan

	return submissions

def clean_comments(comments, tickers, dollar_tickers, dollar_tickers_lower, stock_name, company_dict):
	"""
	The function will extract tiem and mentioned companies from submission dataset
	Two columns will be created in original pandas dataframe:
	- time: exact time an article is created
	- body_mentioned_tickers: companies mentioned in body text
	"""
	import datetime
	import pandas as pd
	import string
	import re
	import numpy as np
	import os
	import time
	os.environ['TZ'] = 'America/New_York'
	time.tzset()	


	comments['time'] = None
	comments['body_mentioned_tickers'] = None
        
	for idx in range(len(comments)):

		comments['time'][idx] = datetime.datetime.fromtimestamp(comments['created_utc'][idx]).strftime('%Y-%m-%d-%H-%M')
		

		if type(comments['body'][idx]) != float:
			# Extract mentioned tickers in body (body)
				# Eliminate speical letters in body
			body_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#%&\\\=\(\'\"]', '', str(comments['body'][idx]))
			body_text = re.sub('\n', '', body_text)
			body_text = set(body_text.split())
				# Extract mentioned tickers in body 
			body_tickers_intersec = list(body_text.intersection(tickers))
			body_dollar_tickers_intersec = list(body_text.intersection(dollar_tickers))
			body_mentioned_companies = list(body_text.intersection(stock_name))

			body_mentioned_tickers = list(set(body_tickers_intersec + 
												[item.replace('$', '') for item in body_dollar_tickers_intersec] + 
												[company_dict[c] for c in body_mentioned_companies]))

			comments['body_mentioned_tickers'][idx] = body_mentioned_tickers
			
		else:
			comments['body_mentioned_tickers'][idx] = np.nan

	return comments
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
