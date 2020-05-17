"""
read station index from data_folder/stazioni.csv into a stations_df

read files from "data_folder/" + codice_stazione + ".csv" into 
"""
import glob, os
import numpy as np
import pandas as pd
debug = False
# shorter experiments
parse_one_file = False
#input format
input_csv_dialect =  {
    "field separator" : ";", 
    "decimal separator" : ".", 
    "quoted fields" : "no", 
    "newline" : ""
}
# stazioni.csv: UTF-8 Unicode text
# single station data files are ASCII text

metadata_file = "./dati/stazioni.csv"

metadata_df = pd.read_csv(metadata_file, sep=";")

if parse_one_file:
    lombardia_files = glob.glob("dati/lmb002.csv")
else:
    lombardia_files = glob.glob("dati/lmb[0-9][0-9][0-9].csv")
lombardia_list = []

#dateparse = lambda x: pd.datetime.strptime(x, "%Y-%m-%d")
dateparse = lambda x: pd.to_datetime(arg = x, format = "%Y-%m-%d")

# TODO use Timezone pd.Timestamp(tz=)
first_day = pd.Timestamp(ts_input = "2020-01-01", freq="D")
last_day = pd.Timestamp(ts_input= "1990-01-01", freq="D")
print(first_day)
print(type(first_day))
    
for station_file in lombardia_files:
    station_df = pd.read_csv(
        filepath_or_buffer = station_file,
        usecols = [1,2,3,4],
        header = 0, 
        sep=";",
        decimal = ".",
        parse_dates = ["datetime"],
        date_parser = dateparse,
        )
    if debug == True:
        print("file-> ",  station_file)
        print("shape-> ",  station_df.shape)
        if ("datetime" not in station_df.columns):
            print("warning: no datetime field in ", station_file)
        print("col data type\n", station_df.dtypes)
    station_min_day = station_df["datetime"].min()
    if station_min_day < first_day:
        first_day = station_min_day
    else:
        pass
    station_max_day = station_df["datetime"].max()
    if station_max_day > last_day:
        last_day = station_max_day
    else:
        pass
    lombardia_list.append(station_df)
print("first_day-> ",first_day)   
print("last_day-> ",last_day)
print("Lombardia; number of dataframes created -> ",len(lombardia_list))
dates = pd.date_range(
    start = first_day,
    end = last_day,
    freq = "D",
)
# np.full(shape=(len(dates),5), fill_value= -999,)
lombardia_df = pd.DataFrame(
    # must put datetime label on index columns
    data = None,
    index = dates,
)
# This not works
#lombardia_df["only_date"] = lombardia_df["dates"].date()

#for station_df in lombardia_list:
#    #lombardia_df = pd.merge(lombardia_df, station_df, on="datetime")
#    #lombardia_df = pd.merge(lombardia_df, station_df)
#    pass
"""
output format
An excel spreadsheet xlsx, with three tabs
tabs = {"t_min":"minima", "t_med":"media", "t_max":"massima"}
"""
#output_file = "temperature.xlsx"
#with pd.ExcelWriter(output_file) as writer:
#    lombardia_df.to_excel(
#        excel_writer = writer, 
#        sheet_name = "minima",
#    )
# TODO: datetime column format is "AAAA-MM-DD hh:mm" instead of "AAAA-MM-DD" 
