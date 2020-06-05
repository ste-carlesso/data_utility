"""Elaborazione H, non divisi, ma effettuata la media oraria


"""
from libreria import *


def create_excel(df, out_path):
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(out_path, engine='xlsxwriter')
    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Sheet1')
    # Get the xlsxwriter workbook and worksheet objects.
    workbook  = writer.book
    worksheet = writer.sheets['Sheet1']
    # Add some cell formats
    format1 = workbook.add_format({'num_format': '0,0'})
    # Set the column width (and maybe the format).
    worksheet.set_column(0,0, 4)
    worksheet.set_column(1,1, 6)
    worksheet.set_column(2,2, 17)
    worksheet.set_column(1,1, 17)
    worksheet.set_column(3,3, 28)
    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
    # start = df["solar"].min()
    # end = df["solar"].max()
    # print("{} {} {}".format(label, start, end)) 


debug = True

if debug:
    good_stations = ["lmb080",]

# a list of tuples of period_label, start, end  
# in solar Tz
# period_list = [
#     ["2013-2014", da.datetime(2013,1,1,0,1), da.datetime(2015,1,1,0,0)],
#     ["2015-2016", da.datetime(2015,1,1,0,1), da.datetime(2017,1,1,0,0)],
#     ["2017-2018", da.datetime(2017,1,1,0,1), da.datetime(2019,1,1,0,0)],
# ]
period_list = [
    ["2018-2019", da.datetime(2018,1,1,0,1), da.datetime(2020,1,1,0,0)],
]

creation_timestamp = str(round(time.time()))
output_dir = creation_timestamp
os.mkdir(output_dir)

for station in good_stations:
    df0_list = []
    for input_dir in ["fomd1", "fomd2", "fomd3"]:
        path = "{}/{}.csv".format(input_dir, station)
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
    df1 = pd.merge(df0_list[0], df0_list[1], how="outer", on="solar")
    # unite resulting dataframe to the third one
    df2 = pd.merge(df1, df0_list[2], how="outer", on="solar")
    # just the columns I want
    the_output_path = "{}/{}_orari.xlsx".format(output_dir, station_label)
    #create_excel(df4, the_output_path)




