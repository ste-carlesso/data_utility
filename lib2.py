def create_excel(dataset, output_file):
    """create a excel file with the correct content"""
    # create an Excel Workbook for any station
    wb = xlsxwriter.Workbook(output_file)
    ws0 = wb.add_worksheet("metadata")
    metadata_text = ["Questo file Excel riporta le temperature di alcune stazioni MeteoNetwork.",
    "italy_dt è la marca temporale presente nei dati forniti da MeteoNetwork, che interpretiamo come riferita all'ora Italiana;",
    "solar_dt è invece riferita a UTC+1 (CET), quindi indipendente dai periodi in cui vige l'ora legale.",
    "L'orario in vigore in Italia si discosta di 0 o 1 ore dall'ora in UTC, a seconda della stagione.",]
    for index, value in enumerate(metadata_text):
        # row, col, data
        ws0.write(index,0, value)
    # create a sheet for the station
    ws = wb.add_worksheet(station_label)
    # write the column header to sheet
    header = ["italy_dt", "utc_dt", "solar_dt", station_label]
    for n,h in enumerate(header):
        ws.write(0, n, h)
    excel_date_format = wb.add_format({"num_format": "yyyy-mm-dd hh:mm"})
    #excel_float_format = wb.add_format({"num_format": "0,0"})
    # append single cells
    ws.write_dt(row_counter + 1, 0, naive_italy_dt, excel_date_format)
    ws.write_dt(row_counter + 1, 1, naive_utc_dt, excel_date_format)
    ws.write_dt(row_counter + 1, 2, naive_solar_dt, excel_date_format)
    ws.write(row_counter + 1, 3, temperature)
    wb.close()
    
    #df1["datetime_it"] = naive2aware(df1["datetime"])
    #df1["naive_it_dt"] = pd.to_datetime(df1["datetime"])    