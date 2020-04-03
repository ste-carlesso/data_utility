"""
read station index from data_folder/stazioni.csv into a stations_df

read files from "data_folder/" + codice_stazione + ".csv" into 


"""
input_csv_dialect =  {
    "field separator" : ";", 
    "decimal separator" : ".", 
    "quoted fields" : "no", 
    "newline" : ""
}

# stazioni.csv: UTF-8 Unicode text
stations_metadata_file = "./dati/stazioni.csv"
# single station data files are ASCII text
#station_science_data_files = 
import csv 


# create reader object
with open(stations_metadata_file) as my_file:
    reader = csv.reader(my_file, dialect="unix")
    for row in reader:
        print(row)

