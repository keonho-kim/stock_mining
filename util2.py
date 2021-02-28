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
    nltk.download('stopwords')

    li_stopwords = [word.upper() for word in list(stopwords.words('english'))]
    stopword = set(li_stopwords)

    alphabets = list(string.ascii_uppercase)

    eliminated_equities = ['CEO', 'USD', 'USA', 'LOVE', 'HOPE', 'YOLO', 'DD']
    

    eliminated_equities = eliminated_equities + alphabets
    eliminated_equities = set(eliminated_equities)

    symbols = set(stock_list['Symbol'])
    adjusted_symbols = symbols.difference(stopword)
    adjusted_symbols = adjusted_symbols.difference(eliminated_equities)

    tickers = adjusted_symbols
    dollar_tickers = set(['$' + ticker for ticker in adjusted_symbols])
    dollar_tickers_lower = set(['$' + ticker.lower()
                                for ticker in adjusted_symbols])

    stock_list = stock_list[stock_list['Symbol'].isin(
        list(tickers))].reset_index(drop=True)
    stock_name = list(stock_list['Name'])
    stock_name = [name.split(' ')[0]
                  for name in stock_name if 'Acquisition' not in name.split(' ')]

    stock_name = set(stock_name).difference(alphabets)

    removed_company_name = ['Walt', 'United', 'Sea', 'General', 'S&P', 'British', 'U.S.', 'Southern', 'Global', 'Palo', 'American', 'MSCI', 'VF', 'Zimmer', 'Kinder', 'American', 'Southwest', 'Ball', 'Sun', 'Arthur', 'Edison', 'Kansas', 'Invitation', 'China', 'Boston', 'Korea', 'W.', 'Universal', 'Advanced', 'Lincoln', 'Globel', 'First', 'West', 'Shaw', 'Texas', 'Ralph', 'Churchill', 'US', 'Western', 'Host', 'Federal', 'National', 'Bloom', 'Affiliated', 'Life', 'Tim', 'Inspire', 'Apartment', 'Choice', 'New', 'Innovative', 'Clean', 'Switch', 'Bank', 'Canada',
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
                                    'Central', 'Fox', 'Unilever', 'Cogent', 'HEICO', 'Juniper', 'Asia', 'Delta', 'Hope', 'Stock', 'Life', 'Can', 'ONE', 'Origin', 'Genetic', 'Taylor', 'Cheetah', 'Deluxe', 'Diversified', 'Cheesecake',
                                    'Reading', 'Peoples', 'Travelers', 'Nuance', 'Align', 'Color', 'Virgin', 'Cross', 'Performed', 'Murphy', 'Business', 'Stanley', 'Northwest', 'Unique', 'Tennessee', 'Big', 'Church', 'Noodles', 'Intersect',
                                    'Preferred', 'Collectors', 'People\'s', 'Mid', 'UP', 'Wireless', 'Huntsman', 'Research', 'Pool', 'Dave', 'Ohio', 'Hub', 'Direxion', 'ishares', 'Platinum', 'Retail', 'Liquidity', 'Sound', 'Benchmark',
                                    'RealReal', 'Cohen', 'Midland', 'Butterfly', 'Viking', 'Coffee', 'Barron\'s', 'Richmond', 'Glob', 'Glacier', 'Desktop', 'Wells', 'Dolphin', 'Pacific', 'Hawkins', 'Philip', 'Darling', 'Children\'s',
                                    'Thunder', 'Hooker', 'Managed', 'Chico\'s', 'BEST', 'Medalist', 'Net', 'Union', 'Source', '1847', 'Bain', 'Simpson', 'Fulgent', 'Merit', 'Brady', 'Goldman', 'FAT', 'Protagonist', 'Smith', 'Fossil',
                                    'Corporacion', 'Lattice', 'Opera', 'Changed', 'Powered', 'Automatic', 'Heat', 'Interpace', 'Jazz', 'Clever', 'Intercorp', 'Illinois', 'Two', 'FLY', 'CTO', 'Blueprint', 'Herman', '111', 'Blink', 'Hanover',
                                    'Banner', 'Income', 'FB', 'Howard', 'Triumph', 'db', 'DB', 'Match', 'Turtle', 'Infastructure', 'Booking', 'Catcha', 'Flushing', 'Good', 'Koppers', 'Brooks', 'Albertsons', 'Pearson', 'Aware', 'Emerald', 'Adamas',
                                    'Four', 'Asure', 'Pioneer', 'German', 'Carter\'s', 'Evolving', 'Ashford', 'Best', 'Lion', 'Applied', 'Dream', 'Customers', '22nd', 'Gaming', 'St.', 'Johnson', 'Industria', 'UnitedStates', 'Safeguard',
                                    'Schlumberger', 'Reynolds', 'Sterling', 'Territorial', 'Ruth\'s', 'Trade', 'Cleveland', 'Provident', 'Structured', 'Goal', 'Merrill', 'Profound', 'Pinnacle', 'Heritage', 'Six', 'Sumo', 'Array', 'Sharps',
                                    'Multiplan', 'Lake', 'Sos', 'Simply', 'Goodyear', 'Tian', 'Saul', 'Penn', 'Alabama', 'Mercury', 'Easterly', 'Aikido', 'F5', 'Energizer', 'Wolverine', 'Parts', 'Solid', 'Alliance', 'Builders', '9F',
                                    'Orchid', 'Switchback', 'Alexander\'s', 'Retractable', 'Norwegian', 'Accuray', 'Innovator', 'Barnes', 'Noah', 'Green', 'Williams', 'Extended', 'Frequency', 'Financial', 'Uranium', 'Floor', 'Mustang',
                                    'IF', 'Lindsay', 'Rollins', 'Alpha', 'Lightspeed', 'Horizon', 'Queens', 'Bar', 'Relay', 'Franchise', 'Indonesia', 'Investors', 'Knowledge', 'Selective', 'Empire', 'Grocery', 'Arbor', 'Trinity', 'Dover',
                                    'Bowl', 'Express', 'Formula', 'Value', 'Independence', 'NorthWestern', 'Lawson', 'bluebird', 'Sixth', 'Americas', 'Compass', 'Westwood', 'Tyson', 'Proto', 'MIX', 'Discover', 'Carriage', 'Independent',
                                    'GreenPower', '9', 'Chicago', 'Twin', 'Legacy', 'Score', 'Evans', 'Flexible', 'Shift', 'Integrated', 'Partners', 'Mid-America', 'Mind', 'Huron', 'Liquid', 'Third', 'Lexington', 'Tennant', 'Columbia',
                                    'Frontdoor', 'Equitable', 'Aurora', 'Aesthetic', 'Victory', 'Fluor', 'Progressive', 'Fusion', 'Installed', 'Porch', 'Morgan', 'Full', 'Scholastic', 'Flux', 'Pilgrims', 'Nordic', 'CSI', 'Federated',
                                    'Allegiant', 'Fate', 'Nicholas', 'Gates', 'Jack', 'Phathom', 'Cincinnati', 'Colony', 'Flex', 'Flowers', 'Establishment', 'Consolidated', 'Chase', 'Special', 'Limestone', 'Oil', 'Merchants', 'Manchester',
                                    'Advent', 'Surface', 'Simon', 'Charles', 'Information', 'Village', 'Artesian', 'Intuit', 'Forward', 'Signature', 'Patriot', 'Precision', 'Ivy', 'Steven', 'Leap', 'Total', 'Fuel', 'Credit', 'Middlesex',
                                    'Harrow', 'Clear', 'Radius', 'Lantern', 'Capstone', 'Rocket', ' Points', 'Standard', 'Stepan', 'Build', 'Aethlon', 'Sandy']

    removed_company_name = set(removed_company_name)
    stock_name = stock_name.difference(removed_company_name)

    stock_list['company_name'] = None

    for i in range(len(stock_list)):
        stock_list['company_name'][i] = stock_list['Name'][i].split(' ')[0]

    company_dict = dict()

    for name in stock_name:
        subset = stock_list[stock_list['company_name'] == name]
        if len(subset) > 1:
            continue
        else:
            company_dict[name] = subset['Symbol'].iloc[0]

    company_dict['Amazon'] = 'AMZN'
    company_dict['Yum'] = 'YUM'
    company_dict['Disney'] = 'DIS'
    company_dict['Blink Charging'] = 'BLNK'

    stock_name = list(company_dict.keys())

    return tickers, dollar_tickers, dollar_tickers_lower, stock_name, company_dict


def extract_tickers(text, stock_file):
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

    tickers, dollar_tickers, dollar_tickers_lower, stock_name, company_dict = clean_setup(stock_file)

    if type(text) != float:
        # Extract mentioned tickers in title
        # Eliminate speical letters in title
        text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#%&\\\=\(\'\"]', ' ', text)
        text = set(text.split())
        # Extract mentioned tickers in title
        tickers_intersec = text.intersection(tickers)
        tickers_intersec = list(tickers_intersec)

        dollar_tickers_intersec = text.intersection(dollar_tickers)
        dollar_tickers_intersec = list(dollar_tickers_intersec)

        dollar_tickers_lower_intersec = text.intersection(dollar_tickers_lower)
        dollar_tickers_lower_intersec = list(dollar_tickers_lower_intersec)

        mentioned_companies = list(text.intersection(stock_name))

        mentioned_tickers = list(set(tickers_intersec +
                                            [item.replace('$', '') for item in dollar_tickers_intersec] +
                                            [item.upper().replace('$', '') for item in dollar_tickers_lower_intersec] +
                                            [company_dict[c] for c in mentioned_companies]))

        if len(mentioned_tickers) != 0:
            result = mentioned_tickers
        else:
            result = None

    else:
        result = None

    return result

    
def convert_time(str_time):
    import datetime

    converted_time = datetime.datetime.fromtimestamp(
        str_time).strftime('%Y-%m-%d-%H-%M')

    return converted_time


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

def extract_num_word(word):
    import re
    from contextlib import redirect_stdout
    import os
    
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize  
 
    with redirect_stdout(open(os.devnull, "w")):
        nltk.download('punkt')
        nltk.download('stopwords')
 
    nonPunct = re.compile('.*[A-Za-z0-9].*')
    stop_words = set(stopwords.words('english'))

    if type(word) != float and word != '[removed]':
        word = word.lower()
        word = re.sub('\'', ' ', word)
        word = re.sub('\n', ' ', word, 0, re.I|re.S)
        word = word_tokenize(word)
        word_filtered= [w for w in word if not w in stop_words]
        word_filtered = [w for w in word_filtered if nonPunct.match(w)]
    
    else:
        word_filtered = []

    return len(word_filtered)