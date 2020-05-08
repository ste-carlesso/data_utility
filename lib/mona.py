# -*- coding: utf-8 -*-
"""
MeteoNetwork Hourly data  using Pandas
"""
import glob
import pandas as pd
debug = False

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

df2_list = []

if debug:
    station_file_list = glob.glob("input/lmb080.csv")
else:
    filename_list = glob.glob("input/lmb[0-9][0-9][0-9].csv")

output_file = "output/temperatureOrarieMN.xlsx"

for station_file in station_file_list:
    # get station code aka id from filename
    station_id = station_file[6:12]
    # convert it to a pretty name
    station_label = metadata_series[station_id]
    # these are the first two lines of a csv to be processed 
    #code;datetime;temperature
    #lmb080;2013-06-20 00:30:00;25.20
    df1 = pd.read_csv(
        filepath_or_buffer = station_file,
        sep = ";",
        decimal = ".",
        header =  0,
        usecols = ["datetime", parameter],
        index_col = 0,
    )
    df1 = df1.rename(columns = {parameter: station_label})
    df1_list.append(df1)

# df2 is 
df2 = pd.concat(
    objs = df1_list,
    axis = 1,
    #join = "left",
)

df2.fillna(-999)
#df2["data_italiana"] = df2["datetime"]

df2_list.append(df2)
output_file = "output/" + tabs[parameter] + ".csv"
df2.to_csv(
    output_file,
    sep= ";",
    decimal=","
    )
#output format is an excel spreadsheet xlsx, with three tabs

output_file = "output/" + tabs[parameter] + ".xlsx"
with pd.ExcelWriter(output_file) as writer:
    df2.to_excel(excel_writer = writer,sheet_name = tabs[parameter],)

"""