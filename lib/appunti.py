# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 11:02:05 2020

@author: Carlesso
"""
import numpy as np
import pandas as pd

regione = "Lombardia"

metadata_file = "./dati/stazioni.csv"
metadata_df = pd.read_csv(
    filepath_or_buffer =metadata_file, 
    sep=";",
    decimal = ".",
    header =  0,
    usecols = ["code", "regione", "comune", "area", "provincia"],
    index_col = 0,
    )

df = metadata_df[metadata_df["regione"] == "Lombardia"]



lombardia1 = metadata_df[pd.notna(df["area"])]
lombardia1 = metadata_df[["comune", "area"]]
lombardia_labels 

    
def get_data():
    station_file = "dati/lmb002.csv"
    station_id = station_file[5:11]
    parameter = "t_min"
    field_label = str(station_id + "_"+  parameter)
    station_t_min = pd.read_csv(
        filepath_or_buffer = station_file,
        sep = ";",
        decimal = ".",
        header =  0,
        usecols = [1,2],
        index_col = 0,
        #names = [field_label],
    )
    # copy old column to new one
    station_t_min[field_label] = station_t_min["t_min"]
    # Delete old column
    station_t_min.pop("t_min")

metadata_df = get_metadata()


#station_label = lombardia_metadata_df["comune" "area"]