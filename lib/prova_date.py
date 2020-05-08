# -*- coding: utf-8 -*-
"""
Created on Thu May  7 00:05:11 2020

@author: Carlesso
"""




from datetime import datetime, timedelta
import pytz

one_hour = timedelta(hours=1)

italy = pytz.timezone("Europe/Rome")
utc = pytz.timezone("UTC")
naive_dt = datetime.fromisoformat('2017-05-30 14:00:00')
italy_dt = italy.localize(naive_dt)
utc_dt = italy_dt.astimezone(utc)
solar_dt = utc_dt + one_hour