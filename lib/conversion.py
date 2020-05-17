import pandas as pd
my_string = "2020-03-04"
my_timestamp = pd.to_datetime(arg = my_string, format = "%Y-%m-%d")
my_date = my_timestamp.date()
print(my_timestamp)
print(type(my_timestamp))
print(my_date)
print(type(my_date))
