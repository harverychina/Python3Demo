# -*- coding:utf8 -*-
# @Time：2022/1/6 10:44 AM
# @Author： Huang Jeff
import json
import requests

# https://www.futunn.com/quote-api/get-rank-list?market_type=1&type=1&num=6
# gemini_ticker = 'https://api.gemini.com/v1/pubticker/{}'

gemini_ticker = 'https://www.futunn.com/quote-api/{}'
symbol = 'get-rank-list?market_type=1&type=1&num=6'


btc_data = requests.get(gemini_ticker.format(symbol)).json()
print(json.dumps(btc_data, indent=4))
