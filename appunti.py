


"""
PANDAS TIPS

To apply your own or another library’s functions to pandas objects, you should be aware of the three methods below. The appropriate method to use depends on whether your function expects to operate on an entire DataFrame or Series, row- or column-wise, or elementwise.

    Tablewise Function Application: pipe()

    Row or Column-wise Function Application: apply()

    Aggregation API: agg() and transform()

    Applying Elementwise Functions: applymap()

Tablewise function application¶
"""

"""
    A very powerful method on time series data with a datetime index, is the ability to resample() time series to another frequency (e.g., converting secondly data into 5-minutely data).

The resample() method is similar to a groupby operation:

    it provides a time-based grouping, by using a string (e.g. M, 5H,…) that defines the target frequency

    it requires an aggregation function such as mean, max,…
"""

"""
# Excel outut tips
import xlsxwriter

# create an Excel Workbook for any station
wb = xlsxwriter.Workbook(file_path)
# create a sheet for the station
ws = wb.add_worksheet(station_label)
# write the column header to sheet
header = ["italy_datetime", "utc_datetime", "solar_datetime", station_label]
for n,h in enumerate(header):
    ws.write(0, n, h)
    excel_date_format = wb.add_format({"num_format": "yyyy-mm-dd hh:mm"})
    excel_float_format = wb.add_format({"num_format": "0,0"})
    # append single cells
    ws.write_datetime(row_counter + 1, 0, naive_italy_datetime, excel_date_format)
    ws.write_datetime(row_counter + 1, 1, naive_utc_datetime, excel_date_format)
    ws.write_datetime(row_counter + 1, 2, naive_solar_datetime, excel_date_format)
    ws.write(row_counter + 1, 3, temperature)    
wb.close()
"""
def create_excel(dataframe, file_path, last_fieldname):
    # create an Excel Workbook for any station
    wb = xlsxwriter.Workbook(file_path)
    # create a sheet for the station
    ws = wb.active
    # write the column header to sheet
    header = ["code","datetime","solar", last_fieldname]
    for col,item in enumerate(header):
        #row, col, content
        ws.write(0, col, item)
    format1 = wb.add_format({"num_format": "yyyy-mm-dd hh:mm"})
    format2 = wb.add_format({"num_format": "0,0"})
    # Set the column width and format.
    ws.set_column(first_col=3, last_col=3, 18, format2)

    # Set the format but not the column width.
    worksheet.set_column('C:C', None, format2)
    # append single cells
    for row_counter in my_iterator:
        ws.write_datetime(row_counter + 1, 0, dataframe["code"], format1)
            ws.write_datetime(row_counter + 1, 1, dataframe["datetime"], format1)
            ws.write_datetime(row_counter + 1, 2, dataframe["solar"], format1)
            ws.write(row_counter + 1, 3, last_fieldname, format2)    
        wb.close()

