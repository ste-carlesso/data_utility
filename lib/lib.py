# -*- coding: utf-8 -*-
"""
@author: Stefano Carlesso
<s.carlesso#fondazioneomd.it>
"""
import os # misc
import squint # tabular data
from datetime import datetime, timedelta # standard date functions and 
import pytz # definitions for wall times
import glob # wildcard for filenames matching
import csv # read ean write csv files
import xlsxwriter # write Excel files


def associate(station_code):
    """read a station code (str) and returns a station name (str)"""
    select = squint.Select("stations.csv")
    label = select(["code", "label"], code = station_code)
    return label


def convert_temperature():
    try:
        temperature = round(float(row["temperature"]), ndigits=1)
    except: 
        temperature = -999.9


def wall2utc(foo):
    """foo is a string representing an Italy wall time"""
    utc = pytz.timezone("UTC")
    # "2013-06-20 00:30:00"
    naive_italy_dt = datetime.strptime(foo, "%Y-%m-%d %H:%M:%S")
    # utc
    aware_utc_dt = naive_italy_dt.astimezone(utc)
    # trasform aware to naive for the benefit of poor xlsxwriter
    naive_utc_dt = aware_utc_dt.replace(tzinfo=None)
    return naive_utc_dt

def utc2solar(naive_utc_dt):
    naive_solar_dt = naive_utc_dt + timedelta(hours=1)
    return 

def make_dataset(csv_file):
    """take a csv and read data"""
    select = squint.Select(csv_file, delimiter=";")
    query1 = select(["code", "datetime", "temperature"])
    query2 = select(["code", "datetime", "temperature",])
    return 1

def create_excel(dataset, output_file):
    """create a excel file with the correct content"""
    # create an Excel Workbook for any station
    wb = xlsxwriter.Workbook(output_file)
    ws0 = wb.add_worksheet("metadata")
    metadata_text = ["Questo file Excel riporta le temperature di alcune stazioni MeteoNetwork.",
    "italy_dt è la marca temporale presente nei dati forniti da MeteoNetwork, che interpretiamo come riferita all'ora Italiana;",
    "solar_dt è invece riferita a UTC+1 (CET), quindi indipendente dai periodi in cui vige l'ora legale.",
    "L'orario in vigore in Italia si discosta di 0 o 1 ore dall'ora in UTC, a seconda della stagione.",]
    for index, value in enumerate(metadata_text):
        # row, col, data
        ws0.write(index,0, value)
    # create a sheet for the station
    ws = wb.add_worksheet(station_label)
    # write the column header to sheet
    header = ["italy_dt", "utc_dt", "solar_dt", station_label]
    for n,h in enumerate(header):
        ws.write(0, n, h)
    excel_date_format = wb.add_format({"num_format": "yyyy-mm-dd hh:mm"})
    #excel_float_format = wb.add_format({"num_format": "0,0"})
    # append single cells
    ws.write_dt(row_counter + 1, 0, naive_italy_dt, excel_date_format)
    ws.write_dt(row_counter + 1, 1, naive_utc_dt, excel_date_format)
    ws.write_dt(row_counter + 1, 2, naive_solar_dt, excel_date_format)
    ws.write(row_counter + 1, 3, temperature)
    wb.close()


debug = True

if debug:
    input_list = glob.glob("input/lmb080.csv")
else:
    # TODO check for errors
    input_list = glob.glob("input/[a-z][a-z][a-z][0-9][0-9][0-9].csv")

#for station in input_list:
#    drill(station)
    

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

