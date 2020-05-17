# -*- coding: utf-8 -*-
"""
Created on Thu May  7 17:07:54 2020

@author: Carlesso
"""


import email.utils as eutils
import time
import datetime


def standardize_date(date_str):
    ntuple=eutils.parsedate(date_str)
    timestamp=time.mktime(ntuple)
    date=datetime.datetime.fromtimestamp(timestamp)
    #return date.strftime('%a, %d %b %Y %H:%M:%S')
    return date

print(standardize_date('Mon, 16 Aug 2010 24:00:00'))
# Tue, 17 Aug 2010 00:00:00