# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 12:34:49 2020

@author: Stefano Carlesso

simple: solo Lombardia
"""
import glob
import pandas as pd

# this file was manually checked
metadata_file = "./stazioni_good.csv"
subset = "Lombardia"
parameter_list = ["t_min", "t_med", "t_max"]
station_file_list = glob.glob("dati/lmb[0-9][0-9][0-9].csv")
#station_file_list = glob.glob("dati/lmb00[2-5].csv")
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
df2_list = []

for parameter in parameter_list:
    """iterate to obtain tmin tmed tmax"""
    df1_list = []
    # summary_dict = {
    #     "station": [], 
    #     "first_day": [], 
    #     "last_day": [],
    #     }
    for station_file in station_file_list:
        station_id = station_file[5:11]
        station_label = metadata_series[station_id]
        df1 = pd.read_csv(
            filepath_or_buffer = station_file,
            sep = ";",
            decimal = ".",
            header =  0,
            usecols = ["datetime", parameter],
            index_col = 0,
        )
        # summary_dict["station"].append(station_label)
        # summary_dict["first_day"].append(min(df1.index)) 
        # summary_dict["last_day"].append(max(df1.index))
        df1 = df1.rename(columns = {parameter: station_label})
        df1_list.append(df1)
    df2 = pd.concat(
        objs = df1_list,
        axis = "index",
        join = "outer",
        verify_integrity = False,    
    )
    df2_list.append(df2)
    

