import csv
metadata_file = "./stazioni_good.csv"
metadata_dict = dict()
with open(metadata_file) as a_file:
    # csv header is 
    # code;datetime;temperature
    metadata_reader = csv.DictReader(a_file, delimiter=";", )
    for mrow in metadata_reader:
        metadata_dict[mrow["code"]] = mrow["label_good"] 