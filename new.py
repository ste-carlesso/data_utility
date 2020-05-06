# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:10:54 2020

@author: Carlesso
"""
import glob
import csv
import pandas as pd
from datetime import datetime, timedelta
import pytz

one_hour = timedelta(hours=1)

italy = pytz.timezone("Europe/Rome")
utc = pytz.timezone("UTC")
naive_dt = datetime.fromisoformat('2017-05-30 14:00:00')
italy_dt = italy.localize(naive_dt)
utc_dt = italy_dt.astimezone(utc)
solar_dt = utc_dt + one_hour


# this file was manually checked
metadata_file = "./stazioni_good.csv"

metadata_df = pd.read_csv(
    filepath_or_buffer = metadata_file, 
    sep=";",
    decimal = ".",
    header =  0,
    usecols = ["code", "regione", "label_good"],
    index_col = 0,
    )

metadata_series = pd.Series(metadata_df["label_good"])

#input_timezone
#output_timezone

#datetime_obj = datetime.fromisoformat('2017-11-30 14:00:00')

#filename_list = glob.glob("/lmb[0-9][0-9][0-9].csv")
filename_list = glob.glob("input/lmb080.csv")
   
stations_dict = dict()

for filename in filename_list:
    station_id = filename[6:12]
    station_label = metadata_series[station_id]
    print(station_id, station_label)
    with open(filename) as file:
        # csv header is 
        # code;datetime;temperature
        reader = csv.DictReader(file, delimiter=";", )
        for row in reader:
            try:
                d = datetime.fromisoformat((row["datetime"]))
            except:
                print("not a valid ISO string ", row)
                break
            try:
                t = float(row["temperature"])
            except: 
                t = -999
        #stations_dict[station_id] = (station_code, row)