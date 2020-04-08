# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 12:34:49 2020
@author: Stefano Carlesso
simple: solo Lombardia solo Tmed
"""

import glob
import pandas as pd
import numpy as np

# this file was manually checked
metadata_file = "./stazioni_good.csv"
subset = "Lombardia"
parameter_list = ["t_min", "t_med", "t_max"]

station_file_list = glob.glob("dati/lmb[0-9][0-9][0-9].csv")

metadata_df = pd.read_csv(
    filepath_or_buffer = metadata_file,
    sep=";",
    decimal = ".",
    header =  0,
    usecols = ["code", "regione", "label_good"],
    index_col = 0,
    )
metadata_df = metadata_df[metadata_df["regione"] == subset]
metadata_series = pd.Series(metadata_df["label_good"])


parameter = "t_med"

df1_list = []
datetime_list = []

for station_file in station_file_list:
    station_id = station_file[5:11]
    station_label = metadata_series[station_id]
    df1 = pd.read_csv(
        filepath_or_buffer = station_file,
        sep = ";",  
        decimal = ".",
        header =  0,
        usecols = ["datetime", parameter],
        #index_col = 0,
    )
    df1 = df1.rename(columns = {parameter: station_label})
    df1_list.append(df1)
    datetime_list.append(max(df1["datetime"]))
    datetime_list.append(min(df1["datetime"]))


first_day = min(datetime_list)
last_day = max(datetime_list)
datetime_index = pd.date_range(start=first_day, end=last_day, freq="D")
datetime_list =[]

for i in datetime_index:
    datetime_list.append(str(i))

# datetime_series = pd.Series(datetime_list)
# df0 = pd.DataFrame(data = datetime_series,columns=["datetime"])


# start = 0
# stop = len(df1_list) - 1
# df_tot = df0

# for i in range(start,stop):
#     df_tot = pd.merge(left=df_tot,right=df1_list[i],how="left",on= "datetime")

df_tot =pd.concat(df1_list )
#output format is an excel spreadsheet xlsx, with three tabs
#tabs = {"t_min":"minima", "t_med":"media", "t_max":"massima"}
#output_file = "temperature.xlsx"
# with pd.ExcelWriter(output_file) as writer:
      
# df_tot.to_excel(
#     excel_writer = writer,
#     sheet_name = tabs[parameter],
# )
# output_file = tabs[parameter] + ".csv"
# df_tot.to_csv(
#     output_file,
#     sep= ";",
#     )
