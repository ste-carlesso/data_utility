"""Elaborazione Q, non divisi, effettuata la media oraria
sia bad che good stations
"""
from libreria import good_stations, label_dict, create_excel
import pandas as pd
import numpy as np
import pytz, os, time

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

for station in good_stations:
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

    # # sub-hour data
    # for s0 in s0_list:
    #     for year in range(20)
    #     xlsx_subhour = "{}/{}_{}_suborari.xlsx".format(output_dir, station_label, s0.index.min().year)
    #     df1 = pd.DataFrame(data=s0)
    #     df1["sol"] = df1.index.array
    #     df1["solare"] = df1["sol"].apply(strip_tz)
    #     df1[station_label] = df1["temperature"]
    #     df1 = df1.drop(labels=["sol", "temperature"], axis=1)
    #     df1.to_excel(excel_writer=xlsx_subhour, 
    #         sheet_name=station_label, 
    #         #float_format="%.1f",
    #         header=True, 
    #         index=False)

    # unite the series into one
    s1 = pd.concat(s0_list)
    #resample to 1 hour
    s2 = s1.resample(rule="1h", closed="right", label="right").mean()




    # Naive Series for poor Excel
    # hour data
    xlsx_hour = "{}/{}_orari.xlsx".format(output_dir, station_label)
    df2 = pd.DataFrame(data=s2)
    df2["sol"] = df2.index.array
    df2["solare"] = df2["sol"].apply(strip_tz)
    df2[station_label] = df2["temperature"]
    df2 = df2.drop(labels=["sol", "temperature"], axis=1)
    df2.to_excel(excel_writer=xlsx_hour, 
        sheet_name=station_label, 
        #float_format="%.1f",
        header=True, 
        index=False)
