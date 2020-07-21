"""Elaborazione Q, non divisi, effettuata la media oraria
per le bad_stations
"""
from libreria import good_stations, label_dict, create_excel
import pandas as pd
import numpy as np
import pytz, os, time


bad_stations = ["lmb168", "lmb267", "pmn047"] # they have duplicate index

bad_stations = ["pmn047"]

output_dir = "../orari" + str(round(time.time()))

os.mkdir(output_dir)
ita = pytz.timezone("Europe/Rome")
utc = pytz.timezone("UTC")
sol = pytz.timezone("Etc/GMT-1")


def strip_tz(bad_time):
    # oldtime is a string
    # remove the timezone part for the benefit of poor excel writer
    good_time = str(bad_time)
    good_time = good_time[:19]
    return good_time

for station in bad_stations:
    s0_list = []
    for input_dir in ["fomd1", "fomd2", "fomd3", "fomd4"]:
        path = "../input/{}/{}.csv".format(input_dir, station)
        s_wall = pd.read_csv( filepath_or_buffer=path, sep=";", header=0, 
            usecols=["datetime", "temperature"], index_col="datetime", 
            squeeze=True, parse_dates=True, )
        #all_true= np.full(shape=s_wall.shape, fill_value=True)
        # print(station, input_dir, "original records", s_wall.shape)
        # s_stone = s_wall.drop_duplicates()
        # print(station, input_dir, "unique_v records", s_wall.shape)
        # convert index of Series between Timezones
        #s_ita = s_wall.tz_localize(ita, ambiguous=all_true, nonexistent="shift_forward" )
        s_ita = s_wall.tz_localize(ita, ambiguous="NaT", nonexistent="NaT")
        # print(station, input_dir, "original records", s_ita.shape)
        # s_stone = s_wall.drop_duplicates()
        # print(station, input_dir, "unique_v records", s_stone.shape)
        s_utc = s_ita.tz_convert(utc)
        s_sol = s_ita.tz_convert(sol)
        s0_list.append(s_sol)

    # ELABORATE ANY SINGLE STATION 
    station_label = label_dict[station]
    # unite the series into one
    s1 = pd.concat(s0_list)
    s2 = s1.resample(rule="1h", closed="right", label="right").mean()
    out_csv1 = "{}/{}_suborari.csv".format(output_dir, station_label)
    #out_csv2 = "{}/{}_orari.csv".format(output_dir, station_label)
    out_xlsx = "{}/{}_orari.xlsx".format(output_dir, station_label)
    s1.to_csv(path_or_buf=out_csv1, sep=";", header=[ station_label,],
                index_label=["solar",])
    #s2.to_csv(path_or_buf=out_csv2, sep=";", header=[ station_label,], index_label=["solar",])


    # Naive Series for poor Excel
    df = pd.DataFrame(data=s2)
    df["sol"] = df.index.array
    df["solare"] = df["sol"].apply(strip_tz)
    df[station_label] = df["temperature"]
    df1 = df.drop(labels=["sol", "temperature"], axis=1)
    df1.to_excel(excel_writer=out_xlsx, 
        sheet_name=station_label, 
        #float_format="%.1f",
        header=True, 
        index=False)

