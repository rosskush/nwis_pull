__author__ = 'rosskush'


import pandas as pd
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen


def read_url_file(url,line_break):
	url_file = urlopen(url).readlines()
	file = []
	i = 0
	for line in url_file:
	    file.append(line.decode("utf-8"))
	    i+=1
	    if i > line_break: break # assuming the data starts before line 60
	skip = next(filter(lambda x: x[1].startswith('5s'), enumerate(file))) # find the line that starts with 5s
	names = file[skip[0]-1].split()
	df = pd.read_table(url, skiprows=skip[0]+1,names=names)
	return df


class pull_data:
	def realtime(siteid,start_date,end_date,param_code,line_break=60):
	    url = f'https://nwis.waterdata.usgs.gov/nwis/uv?cb_{param_code}=on&format=rdb&site_no={siteid}&period=&begin_date={start_date}&end_date={end_date}'
	    print(url)

	    # url_file = urlopen(url).readlines()
	    # file = []
	    # i = 0
	    # for line in url_file:
	    #     file.append(line.decode("utf-8"))
	    #     i+=1
	    #     if i > line_break: break # assuming the data starts before line 60
	    # skip = next(filter(lambda x: x[1].startswith('5s'), enumerate(file))) # find the line that starts with 5s
	    # names = file[skip[0]-1].split()
	    # df = pd.read_table(url, skiprows=skip[0]+1,names=names)
	    df = read_url_file(url,line_break)
	    param_col = [item for item in df.columns if (param_code in item)&('cd' not in item)][0]
	    df[param_code] = df[param_col]
	    df.index = pd.to_datetime(df['datetime'])
	    df = df[[param_code]]
	    return df

	def field_measurments(siteid,line_break=120):
		url = f'https://nwis.waterdata.usgs.gov/nwis/gwlevels?site_no={siteid}&agency_cd=USGS&format=rdb'
		df = read_url_file(url,line_break)

		param_col = [item for item in df.columns if ('cd' not in item)][0]

		df['lev_tm'].loc[pd.isnull(df['lev_tm'])] = '00:00' # defualt to 00:00
		df.index = df.apply(lambda x: pd.to_datetime(x['lev_dt']+' '+x['lev_tm']),axis=1)

		return df




