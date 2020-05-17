# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 12:34:49 2020

@author: Carlesso
"""


# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 11:02:05 2020

@author: Carlesso
"""
import numpy as np
import pandas as pd

subset = "Lombardia"

metadata_file = "./stazioni_good.csv"
metadata_df = pd.read_csv(
    filepath_or_buffer =metadata_file, 
    sep=";",
    decimal = ".",
    header =  0,
    usecols = ["code", "regione", "label_good"],
    index_col = 0,
    )

df = metadata_df[metadata_df["regione"] == subset]

df2 = df.rename(
    columns = {"label_good": "stazione"}
    )



