# -*- coding: utf-8 -*-
"""
@author: Stefano Carlesso
<s.carlesso#fondazioneomd.it>
"""
"""
To apply your own or another library’s functions to pandas objects, you should be aware of the three methods below. The appropriate method to use depends on whether your function expects to operate on an entire DataFrame or Series, row- or column-wise, or elementwise.

    Tablewise Function Application: pipe()

    Row or Column-wise Function Application: apply()

    Aggregation API: agg() and transform()

    Applying Elementwise Functions: applymap()

Tablewise function application¶
"""
import os # misc
from datetime import datetime, timedelta # standard date functions
import pytz # definitions for wall times
import glob # wildcard for filenames matching
#import csv # read and write csv files
#import xlsxwriter # write Excel files
import pandas as pd
import math


def convert_temperature(raw_temp):
    try:
        temperature = round(float(raw_temp), ndigits=1)
    except: 
        temperature = -999.9
    return temperature

def str2dt(string):
    """return a datetime object from the corresponding time string"""
    # "2013-06-20 00:30:00" 
    dt = datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
    return dt

def naive2aware(naive_dt):
    """convert a naive Italy wall time to timezone-aware dt,
    with variable offset from UTC"""
    aware_dt = pytz.timezone("Europe/Rome").localize(naive_dt)
    return aware_dt

def ita2utc(ita_dt):
    """?"""
    #Return a datetime object with new tzinfo attribute tz, adjusting the date 
    # and time data so the result is the same UTC time as self, but in tz’s local time.
    utc_dt = ita_dt.astimezone(pytz.timezone("UTC"))
    return utc_dt

def utc2solar(utc_dt):
    """from UTC datetime to UTC+1 (fixed offset)"""
    #Return a datetime object with new tzinfo attribute tz, adjusting the date 
    # and time data so the result is the same UTC time as self, but in tz’s local time.
    solar_dt = utc_dt.astimezone(pytz.timezone("CET"))
    return solar_dt

def interesting(dt, start, end):
    """Return True if datetime is between start and end, otherwise return False."""
    return dt >= start and dt <= end

#def narrow_period():

def create_label(station_code):
    """read a station code (str) and returns a station name (str)"""
    df0 = pd.read_csv(label_file, sep=";")
    label = df.loc[
        # rows I want
        df["code"] == station_code ,
        # columns I want
        "label"
        ]
    return label

def process_station(file):
    """all things to do with a single station"""
    # from csv to DataFrame
    df1 = pd.read_csv(filepath_or_buffer = file, sep=";", decimal = ".")
    # add derived colums
    df1["naive_it_dt"] = df1["datetime"].apply(str2dt)
    df1["aware_it_dt"] = df1["naive_it_dt"].apply(naive2aware)
    df1["utc_dt"] = df1["aware_it_dt"].apply(ita2utc)
    df1["solar_dt"] = df1["utc_dt"].apply(utc2solar)
    return df1



# SETTINGS
label_file = "stations.csv"
debug = True

if debug:
    input_list = glob.glob("input/lmb080.csv")
else:
    input_list = glob.glob("input/[a-z][a-z][a-z][0-9][0-9][0-9].csv")


for station in input_list:
    print(station)
    df = process_station(station)
    print(df.dtypes)
    #print(df[["aware_it_dt","utc_dt"]].head)
    
#creation_timestamp = str(int(datetime.timestamp(datetime.now())))
#output_file = "suborari{}/Temp_{}.xlsx".format(creation_timestamp, station_label)
"""
for filename in filename_list:
    # get station_id from filename todo: read from csv content instead
    station_id = filename[6:12]
    # convert it to a pretty label
    station_label = 
    print(station_id, station_label)
    # output to ever new dir

    # TODO create folder if not exists

        
    with open(filename) as file:
        # csv header is 
        # code;datetime;temperature
        reader = csv.DictReader(file, delimiter=";", )
        for row_counter, row in enumerate(reader):

                        



if naive_solar_datetime >= tup[1] and naive_solar_datetime <= tup[2]:  
# a list of tuples of period_label, start, end  
period_list = [
    ["2013-2014", datetime(2013,1,1,0,1), datetime(2015,1,1,0,0)],
    ["2015-2016", datetime(2015,1,1,0,1), datetime(2017,1,1,0,0)],
    ["2017-2018", datetime(2017,1,1,0,1), datetime(2019,1,1,0,0)],
    ]
#Excel Workbook for any combination of station and period
for tup in period_list:
"""

"""
    A very powerful method on time series data with a datetime index, is the ability to resample() time series to another frequency (e.g., converting secondly data into 5-minutely data).

The resample() method is similar to a groupby operation:

    it provides a time-based grouping, by using a string (e.g. M, 5H,…) that defines the target frequency

    it requires an aggregation function such as mean, max,…
"""