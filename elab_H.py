"""Elaborazione H, non divisi, ma effettuata la media oraria


"""
from libreria import (good_stations, good_stations, pd, str2solar, os, time, label_dict)


debug = True

if debug:
    good_stations = ["lmb080",]

creation_timestamp = str(round(time.time()))
output_dir = creation_timestamp
os.mkdir(output_dir)

for station in good_stations:
    df0_list = []
    for input_dir in ["fomd1", "fomd2", "fomd3"]:
        path = "../input/{}/{}.csv".format(input_dir, station)
        df0 = pd.read_csv(filepath_or_buffer=path, sep=";", decimal =".")
        df0["solar"] = df0["datetime"].apply(str2solar)
        # get station code from the fist field
        station_code = df0["code"][1]
        station_label = label_dict[station_code]
        # rename column header
        df0[station_label] = df0["temperature"] 
        # only the field I need
        df0 = df0[["solar", station_label]]
        df0_list.append(df0)
    # unite the first two dataframes
    # df1 = pd.merge(df0_list[0], df0_list[1], how="outer", on="solar")
    # unite resulting dataframe to the third one
    # df2 = pd.merge(df1, df0_list[2], how="outer", on="solar")
    df3 = pd.concat(df0_list)
    # just the columns I want
    the_output_path = "{}/{}_orari.xlsx".format(output_dir, station_label)
    #create_excel(df4, the_output_path)
print(df3)




