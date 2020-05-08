# -*- coding: utf-8 -*-
"""
MeteoNetwork Hourly data  using Pandas
"""
import glob
import pandas as pd
debug = True

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

if debug:
    station_file_list = glob.glob("input/lmb080.csv")
else:
    station_file_list = glob.glob("input/lmb[0-9][0-9][0-9].csv")

#df_list = []

for station_file in station_file_list:
    # get station code aka id from filename
    station_id = station_file[6:12]
    # convert it to a pretty name
    station_label = metadata_series[station_id]
    # these are the first two lines of a csv to be processed 
    #code;datetime;temperature
    #lmb080;2013-06-20 00:30:00;25.20
    df = pd.read_csv(
        # input source
        filepath_or_buffer = station_file,
        # column separator
        sep = ";",
        # decimal separator
        decimal = ".",
        # row number(s) to interpret as header not as first record
        header =  0,
        # a list of names to use for columns instead of using the header
        names = ["code", "timestring", station_label],
        # just use theese columns, not all of them
        usecols = ["timestring", station_label],
        #index_col = 0,
    )

    #a_column = df["timestring"]
    # convert from string object to datetime object
    #pd.to_datetime(arg = a_column, format = "%Y-%m-%d %H:%M:%S")
    #convert a column from string to pd.Timestamp object
    # apply a function to every cell of a column
    df.assign(porco = df["station_label"] )
    
    # create a new column with a Timezone-aware timestamp
    #df["italy_timestamp"] = a_column.tz_localize(tz="Europe/Rome")
    #df["utc_timestamp"] = 
    # write to file
    if debug:
        output_file = "output/{}.csv".format(station_id)
        df.to_csv(output_file, sep= ";", decimal=","    )
    else:
        output_file = "output/temperatureOrarieMN.xlsx"
        with pd.ExcelWriter(output_file) as writer:
            df.to_excel(excel_writer = writer, sheet_name=station_label)


