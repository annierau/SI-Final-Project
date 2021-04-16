from datetime import datetime, date, timedelta
import requests
import json
from polygon import RESTClient

key = "OO6kdLUPSMrVQMTjxBODpM92v244QDai"

def get_stock_date():
    stock_date_list = []
    start_date = date(2019, 3, 2)
    end_date = date(2019, 3, 3)
    delta = timedelta(days=1)
    while start_date <= end_date:
        stock_date = start_date.strftime("%Y-%m-%d")
        stock_date_list.append(stock_date)
        start_date += delta
    return stock_date_list


def main():
    stock_date_list = get_stock_date()

    stock = 'AAPL'
    

    base_url = "https://api.polygon.io/v1/open-close/{}/{}?unadjusted=true&apiKey={}"
    request_url = base_url.format(stock, '2020-11-27', key)
    r = requests.get(request_url)
    data = r.text
    dict_list = json.loads(data)
    open = dict_list['open']
    close = dict_list['close']
    print(float(close)-float(open))



if __name__ == '__main__':
    main()

