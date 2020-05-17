import datetime
import pytz

# source https://janakiev.com/blog/time-and-timezones-in-python/
timestring =  "2013-06-20 00:30:00"
naive_datetime = datetime.datetime.strptime(timestring, "%Y-%m-%d %H:%M:%S")
print(naive_datetime)
print(naive_datetime.tzinfo)
ita = pytz.timezone("Europe/Rome")
aware_datetime = ita.localize(naive_datetime)
print(aware_datetime)
print(aware_datetime.tzinfo)

#utc =pytz.utc

#utc_datetime = naive_datetime.astimezone(utc)
# solar_datetime is timezone-aware