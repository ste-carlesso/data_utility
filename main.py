# -*- coding: utf-8 -*-
"""
@author: Stefano Carlesso
<s.carlesso#fondazioneomd.it>
"""

import datetime as da # standard date functions
import pandas as pd
import os # misc
import time
import pytz # definitions for wall times
import glob # wildcard for filenames matching
import metadata
#import csv # read ean write csv files
#import xlsxwriter # write Excel files



# a list of tuples of period_label, start, end  
# in solar Tz
period_list = [
    ["2013-2014", da.datetime(2013,1,1,0,1), da.datetime(2015,1,1,0,0)],
    ["2015-2016", da.datetime(2015,1,1,0,1), da.datetime(2017,1,1,0,0)],
    ["2017-2018", da.datetime(2017,1,1,0,1), da.datetime(2019,1,1,0,0)],
]



def convert_temperature(raw_temp):
    try:
        temperature = round(float(raw_temp), ndigits=1)
    except: 
        temperature = -999.9
    return temperature

def str2naive(string):
    """return a naive datetime object from the corresponding time string"""
    # "2013-06-20 00:30:00" 
    # I know from other metadata that this is an Italian wall time
    dt = da.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
    return dt

def naive2ita(naive_dt):
    """convert a naive Italy wall time to timezone-aware dt,
    with variable offset from UTC, due to Daylight saving time"""
    aware_dt = pytz.timezone("Europe/Rome").localize(naive_dt)
    return aware_dt

def ita2utc(ita_dt):
    """?"""
    # ASTIMEZONE Return a datetime object with new tzinfo attribute tz, adjusting the date 
    # and time data so the result is the same UTC time as self, but in tz’s local time.
    utc_dt = ita_dt.astimezone(pytz.timezone("UTC"))
    return utc_dt

def utc2solar(utc_dt):
    # ASTIMEZONE Return a datetime object with new tzinfo attribute tz, adjusting the date 
    # and time data so the result is the same UTC time as self, but in tz’s local time.
    solar_tz = da.timezone(offset=da.timedelta(hours=1), name="SOLAR")
    solar_dt = utc_dt.astimezone(solar_tz)
    return solar_dt

def utc2naive(utc_dt):
    # trasform aware to naive for the benefit of poor xlsxwriter
    naive_dt = utc_dt.replace(tzinfo=None)
    return naive_dt
    
def str2solar(string):        
    # "2013-06-20 00:30:00"
    naive_dt = da.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
    ita_dt = pytz.timezone("Europe/Rome").localize(naive_dt)
    utc_dt = ita_dt.astimezone(pytz.utc)
    solar_dt = utc_dt + da.timedelta(hours=1)
    solar_dt = solar_dt.replace(tzinfo=None)
    return solar_dt

def interesting(dt, start, end):
    """Return True if datetime is between start and end, otherwise return False."""
    return dt >= start and dt <= end

#def narrow_period():

def process_station(filepath):
    """all things to do with a single station
    and return a tuple  (station_label, DataFrame)
    """
    print("processing {} please wait".format(filepath))
    # from csv to DataFrame
    df1 = pd.read_csv(filepath_or_buffer=filepath, sep=";", decimal = ".")
    #add derived colums
    # df1["naive_it_dt"] = df1["datetime"].apply(str2naive)
    # df1["aware_it_dt"] = df1["naive_it_dt"].apply(naive2ita)
    # df1["utc_dt"] = df1["aware_it_dt"].apply(ita2utc)
    # df1["solar_dt"] = df1["aware_it_dt"].apply(utc2solar)
    df1["solar"] = df1["datetime"].apply(str2solar)
    # get station code from the fist field
    station_code = df1["code"][1]
    station_label = metadata.label_dict[station_code]
    df1[station_label] = df1["temperature"] 
    return (station_label, df1)

def simple_test():
    """print datetime objects and timezone for poor man checking"""
    test_list =  ["2013-12-25 00:30:00", "2013-06-2 00:30:00", ]
    for timestring in test_list:
        naive = str2naive(timestring)
        ita = naive2ita(naive)
        utc = ita2utc(ita)
        solar = utc2solar(utc)
        print("naive", naive, naive.tzinfo)
        print("ita", ita, ita.tzinfo)
        print("utc", utc, utc.tzinfo)
        print("solar", solar, solar.tzinfo)


#SETTINGS

debug = False
if debug:
    input_list = glob.glob("input/lmb080.csv")
else:
    input_list = glob.glob("input/[a-z][a-z][a-z][0-9][0-9][0-9].csv")

for station in input_list:
    # unpacking the tuple
    label, df2 = process_station(station)
    #print(df.dtypes)
    #print(df.head)
    df3 = df2[["code","datetime","solar", label]]
    creation_timestamp = str(round(time.time()))
    directory = creation_timestamp
    os.mkdir(directory)
    for timeframe in period_list:
        out_path = "{}/{}_{}.xlsx".format(directory, label, timeframe[0])
        bool_array = df3["solar"].between(timeframe[1], timeframe[2])
        df4 = df3.loc[bool_array]
        # todo use comma or float in excel
        # with pd.ExcelWriter(out_path, engine="openpyxl" datetime_format="YYYY-MM-DD HH:MM:SS") as writer:
        #     df4.to_excel(excel_writer=writer)
        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter(out_path, engine='xlsxwriter')
        # Convert the dataframe to an XlsxWriter Excel object.
        df4.to_excel(writer, sheet_name='Sheet1')
        # Get the xlsxwriter workbook and worksheet objects.
        workbook  = writer.book
        worksheet = writer.sheets['Sheet1']
        # Add some cell formats.
        format1 = workbook.add_format({'num_format': '0,0'})
        # Set the column width (and maybe the format).
        worksheet.set_column(0,0, 4)
        worksheet.set_column(1,1, 6)
        worksheet.set_column(2,2, 17)
        worksheet.set_column(1,1, 17)
        worksheet.set_column(3,3, 28)
        # Close the Pandas Excel writer and output the Excel file.
        writer.save()


