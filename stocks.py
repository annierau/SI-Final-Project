
from datetime import datetime, date, timedelta
import requests
import json
from polygon import RESTClient
import os
import csv
import sqlite3


key = "OO6kdLUPSMrVQMTjxBODpM92v244QDai"

def get_stock_date():
    stock_date_list = []
    start_date = date(2020, 11, 27)
    end_date = date(2020, 11, 29)
    delta = timedelta(days=1)
    while start_date <= end_date:
        stock_date = start_date.strftime("%Y-%m-%d")
        stock_date_list.append(stock_date)
        start_date += delta
    return stock_date_list

def get_data(stock, date):
        request_url = 'https://api.polygon.io/v1/open-close/' + stock + '/' + date + '?unadjusted=true&apiKey=' + key
        r = requests.get(request_url)
        j = (r.json)
        data = r.text
        dict_list = json.loads(data)

        open = dict_list['open']
        close = dict_list['close']
        change = (float(close)-float(open))
        return change

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def add_to_db(date, change, stock, cur, conn):
    cur.execute("DROP TABLE IF EXISTS Stocks")
    cur.execute("CREATE TABLE Stocks (date TEXT PRIMARY KEY, change INTEGER, stock TEXT)")
    print("Adding information to database")
    cur.execute("INSERT INTO Stocks (date, change, stock) VALUES (?,?,?)",(date, change, stock))
    conn.commit()

def main():
    stock_date_list = get_stock_date()
    date = stock_date_list[0]
    stock = 'AAPL'
    change = get_data(stock, date)
    cur, conn = setUpDatabase('final_project.db')
    add_to_db(date, change, stock, cur, conn)
    print("done! date is: " + str(date) + " and change is: " + str(change) )


# this doesn't work and I don't know why!
    # for i in range(2):
    #     date = stock_date_list[i]
    #     change = get_data(stock, date)
    #     cur, conn = setUpDatabase('final_project.db')
    #     add_to_db(date, change, stock, cur, conn)
    #     print("done! date is: " + str(date) + "and change is: " + str(change) )









if __name__ == '__main__':
    main()

