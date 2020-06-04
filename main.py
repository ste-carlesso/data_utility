from libreria import *

debug = False


good_stations = ["lmb080", "lmb136", "lmb167", "lmb168", "lmb170", "lmb175", "lmb179", "lmb191", "lmb220", "lmb238", "lmb254", "lmb267", "lmb286", "pmn047",]

# if debug:
#     input_list = glob.glob("fomd3/lmb080.csv")
# else:
#     input_list = glob.glob("fomd3/[a-z][a-z][a-z][0-9][0-9][0-9].csv")



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
directory = creation_timestamp
os.mkdir(directory)

for station in good_stations:
    df_list = []
    for directory in ["fomd1", "fomd2", "fomd3"]
        path = "fomd1/{}.csv".format(station)
        df = pd.read_csv(filepath_or_buffer=path, sep=";", decimal =".")
        df_list.append(df)  
    # unite csv from the tree input_dirs

    # unpacking the tuple
    label, df2 = process_station(station)
    #print(df.dtypes)
    #print(df.head)
    df3 = df2[["code","datetime","solar", label]]
    for timeframe in period_list:
        out_path = "{}/{}_{}.xlsx".format(directory, label, timeframe[0])
        bool_array = df3["solar"].between(timeframe[1], timeframe[2])
        df4 = df3.loc[bool_array]
        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter(out_path, engine='xlsxwriter')
        # Convert the dataframe to an XlsxWriter Excel object.
        df4.to_excel(writer, sheet_name='Sheet1')
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
    # start = df3["solar"].min()
    # end = df3["solar"].max()
    # print("{} {} {}".format(label, start, end))




