import requests
import csv
import json
import sqlite3
import os
import time
from datetime import date, timedelta



def sampleAPI(locID, year, month, day, cur, conn):
    url = 'https://www.metaweather.com/api/location/' + str(locID) + '/' + str(year) + '/' + str(month) + '/' + str(day) + '/' #input as year month day
    r = requests.get(url)

    j = (r.json())
    #print("API response: ")
    #print(j[0]) #use this to get full list of variables api gets 
    maxtemp = (j[0].get('max_temp'))
    mintemp = (j[0].get('min_temp'))
    humidity = (j[0].get('humidity'))
    airpressure = (j[0].get('air_pressure'))
    windespeed = (j[0].get('wind_speed'))
    weatherstate = (j[0].get('weather_state_name'))
    date = (j[0].get('applicable_date'))

    print("Date: " + str(date) + ", MaxTemp: " + str(maxtemp))
    #cur.execute("DROP TABLE IF EXISTS Weather")
    #cur.execute("CREATE TABLE Weather (Date TEXT PRIMARY KEY, MaxTemp INTEGER, MinTemp INTEGER, Humidity INTEGER, AirPressure INTEGER, WindSpeed INTEGER, WeatherState TEXT)")
    print("Adding information to database")
    cur.execute("INSERT INTO Weather (Date, MaxTemp, MinTemp, Humidity, AirPressure, WindSpeed, WeatherState) VALUES (?,?,?,?,?,?,?)",(date, maxtemp, mintemp, humidity, airpressure,windespeed,weatherstate))
    conn.commit()

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn


cur, conn = setUpDatabase('final_project.db')

for i in range(1,729):
    #time.sleep(3)
    daysbefore = date.today() - timedelta(days=i)
    daysbefore.strftime('%m%d%y')
    daysbefore = str(daysbefore)
    locID = 2459115 #NYC
    year = daysbefore[:4]
    month = daysbefore[5:7]
    day = daysbefore[8:]
    print("Uploading weather info for " + month + "-" + day + "-" + year)
    sampleAPI(locID, year, month, day, cur, conn)
    



    

