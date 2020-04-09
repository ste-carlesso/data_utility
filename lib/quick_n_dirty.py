"""
read station index from data_folder/stazioni.csv into a stations_df

read files from "data_folder/" + codice_stazione + ".csv" into 
"""
import glob
import numpy as np
import pandas as pd
#input csv format
#     "field separator" : ";", 
#     "decimal separator" : ".", 
#     "quoted fields" : "no", 
#     "newline" : ""
# stazioni.csv: UTF-8 Unicode text
# single station data files are ASCII text

metadata_file = "./dati/stazioni.csv"

metadata_df = pd.read_csv(metadata_file, sep=";")

lombardia_files = glob.glob("dati/lmb[0-9][0-9][0-9].csv")
lombardia_list = []

#dateparse = lambda x: pd.datetime.strptime(x, "%Y-%m-%d")
dateparse = lambda x: pd.to_datetime(arg = x, format = "%Y-%m-%d")

# TODO use Timezone pd.Timestamp(tz=)
first_day = pd.Timestamp(ts_input = "2020-01-01", freq="D")
last_day = pd.Timestamp(ts_input= "1990-01-01", freq="D")
    
for station_file in lombardia_files:
    station_id = station_file[5:11]
    
    station_df = pd.read_csv(
        filepath_or_buffer = station_file,
        sep=";",
        decimal = ".",
        header = 0,
        usecols = [2,3,4],
        index_col = 1,
        names = [
            station_id + "_t_min",
            station_id + "_t_med",
            station_id + "_t_max",
        ],
        parse_dates = [1],
        #date_parser = dateparse,
        )

    station_min_day = station_df.index.min()
    if station_min_day < first_day:
        first_day = station_min_day
    else:
        pass
    station_max_day = station_df.index.max()
    if station_max_day > last_day:
        last_day = station_max_day
    else:
        pass
    lombardia_list.append(station_df)

dates = pd.date_range(
    start = first_day,
    end = last_day,
    freq = "D",
)
lombardia_df = pd.DataFrame(
    # must put datetime label on index columns
    data = pd.ones(),
    index = dates,
    columns = ["ones"],
)

lombardia_df = pd.concat(lombardia_list)

#output format
#An excel spreadsheet xlsx, with three tabs
#tabs = {"t_min":"minima", "t_med":"media", "t_max":"massima"}
#output_file = "temperature.xlsx"
#with pd.ExcelWriter(output_file) as writer:
#    lombardia_df.to_excel(
#        excel_writer = writer, 
#        sheet_name = "minima",
#    )
# TODO: datetime column format is "AAAA-MM-DD hh:mm" instead of "AAAA-MM-DD" 
# station_df.index


