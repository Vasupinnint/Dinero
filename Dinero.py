import requests

# Paths
endpoint = "http://api.marketstack.com/v1/eod/{}"

# Secrets
access_key = "d2f6235ac39c5e90926f6c12ac5d9209"

# Symbols
INDEX_SYM = "NSEI.INDX" 
ETF_SYM = "SETFNN50.XNSE"

# Dates
curr_year_date = "2021-09-14"
past_year_date = "2021-03-15"


def get_EOD(day, symbol):
	ep = endpoint.format(day)
	params = {
		"access_key" : access_key, 
		"symbols" :  symbol
	}
	resp = requests.get(ep, params).json()
	# print(resp)
	data = None
	
	if resp['data'] and len(resp['data'])>0:
		data = resp['data'][0]
	if data and data['close']:
		return data['close']
	return None

def main():
	curr_etf_eod = get_EOD(curr_year_date, ETF_SYM)
	if not curr_etf_eod:
		print("Cannot Access Current ETF EOD or Data Not Available")
		return

	past_etf_eod = get_EOD(past_year_date, ETF_SYM)
	if not past_etf_eod:
		print("Cannot Access Past ETF EOD or Data Not Available")
		return

	curr_index_eod = get_EOD(curr_year_date, INDEX_SYM)
	if not curr_index_eod:
		print("Cannot Access Current Index EOD or Data Not Available")
		return

	past_index_eod = get_EOD(past_year_date, INDEX_SYM)
	if not past_index_eod:
		print("Cannot Access Past Index EOD or Data Not Available")
		return
	

	etf_diff = (curr_etf_eod/past_etf_eod) - 1
	underlying_index_diff = (curr_index_eod/past_index_eod) - 1

	tracking_error = abs(etf_diff - underlying_index_diff)
	print("Tracking Error :", str(round(tracking_error, 2)) + "%")

main()


# Remove this Later

# SAMPLE OUTPUT
"""
{
	'pagination': {
		'limit': 100, 
		'offset': 0, 
		'count': 1, 
		'total': 1
	}, 
	'data': [
		{
			'open': 445.0, 
			'high': 446.49, 
			'low': 442.49, 
			'close': 444.33, 
			'volume': 26366.0, 
			'adj_high': None, 
			'adj_low': None, 
			'adj_close': 444.33, 
			'adj_open': None, 
			'adj_volume': None, 
			'split_factor': 1.0, 
			'symbol': 'SETFNN50.XNSE', 
			'exchange': 'XNSE', 
			'date': '2021-09-14T00:00:00+0000'
		}
	]
}
"""