"""
read station index from data_folder/stazioni.csv into a stations_df

read files from "data_folder/" + codice_stazione + ".csv" into 


"""
import glob, os
import numpy as np
import pandas as pd

input_csv_dialect =  {
    "field separator" : ";", 
    "decimal separator" : ".", 
    "quoted fields" : "no", 
    "newline" : ""
}

# stazioni.csv: UTF-8 Unicode text
stations_metadata_file = "./dati/stazioni.csv"
# single station data files are ASCII text
metadata = pd.read_csv(stations_metadata_file, sep=";")

lombardia_files = glob.glob("dati/lmb[0-9][0-9][0-9].csv")
lombardia_df = pd.DataFrame()

for station_file in lombardia_files:
    
    station_df = pd.read_csv(station_file, sep=";")
    #print(station_df.shape)
    station_columns = station_df.columns
    if not (station_columns[1] == "datetime"):
        print(station_file)
        print("no datetime")
    #lombardia_df = pd.merge(lombardia_df, station_df, on="datetime")
    
