# -*- coding: utf-8 -*-
"""
@author: Stefano Carlesso
<s.carlesso#fondazioneomd.it>
"""

import datetime as da # standard date functions
import pandas as pd
import os # misc
import time
import pytz # definitions for wall times
import glob # wildcard for filenames matching

"""
label_file = "stations.csv"

def create_label(station_id):
    #read a station code (str) and returns a station name (str)
    df0 = pd.read_csv(label_file, sep=";")
    # loc has rows as first arg, columns as second
    #label = df0.loc(df0["code"] == station_id , "label")
    label = df0.where(df0["code"] == station_id)
    return label

"""

# these are the stations our Scientist selected as good for ClimaMI Elaborations
good_stations = ["lmb080", "lmb136", "lmb167", "lmb168", "lmb170", "lmb175", "lmb179", "lmb191", "lmb220", "lmb238", "lmb254", "lmb267", "lmb286", "pmn047",]

bad_stations = ["lmb168", "lmb267", "pmn047"] # they have duplicate index


label_dict = {
    "lmb242": "Abbadia Lariana",
    "lmb275": "Albese con Cassano",
    "lmb165": "Albino-- Fiobbio",
    "lmb257": "Albino--Fiobbio Monte Misma",
    "lmb345": "Almenno San Bartolomeo--località carosso - atterraggio parapendio",
    "lmb315": "Almenno San Bartolomeo--Scuole Medie",
    "lmb223": "Almenno San Salvatore",
    "lmb240": "Alzate Brianza",
    "lmb372": "Arcore",
    "lmb010": "Barlassina",
    "lmb002": "Barzio",
    "lmb302": "Berbenno-- centro",
    "lmb166": "Besana in Brianza--Naresso",
    "lmb123": "Besana in Brianza--Villa Raverio",
    "lmb339": "Bovisio Masciago",
    "lmb094": "Brignano Gera d'Adda",
    "lmb225": "Calco",
    "lmb236": "Calolziocorte--Sopracornola ",
    "lmb319": "Calvenzano",
    "lmb333": "Cantù--Fecchio",
    "lmb230": "Capiago Intimiano--Via Degli Arconi",
    "lmb267": "Carpiano--centro",
    "lmb005": "Casalpusterlengo (prima)",
    "lmb310": "Casalpusterlengo (seconda)",
    "lmb253": "Casargo--Località Piazzo",
    "lmb046": "Cassano d'Adda",
    "lmb314": "Castano Primo",
    "lmb323": "Castellanza--centro",
    "lmb006": "Castelli Calepio",
    "lmb235": "Cesano Maderno",
    "lmb334": "Civenna--Piano Rancio",
    "lmb039": "Codogno",
    "lmb313": "Colere--Colere ",
    "lmb370": "Costa Volpino--fraz. Volpino",
    "lmb292": "Cuasso al Monte--Cavagnano",
    "lmb375": "Dorno-- Via Canevari",
    "lmb277": "Fenegrò",
    "lmb352": "Gaggiano--centro",
    "lmb368": "Gazzaniga",
    "lmb136": "Giussano",
    "lmb331": "Gromo--Rifugio Vodala",
    "lmb207": "Lazzate",
    "lmb325": "Lentate sul Seveso--Copreno",
    "lmb238": "Lesmo--via Po",
    "lmb174": "Lipomo",
    "lmb287": "Lissone",
    "lmb096": "Lodi--v.le Europa (prima)",
    "lmb168": "Lodi--San Bernardo",
    "lmb191": "Lodi--v.le Europa (seconda)",
    "lmb369": "Magnago--Farè Spagarino",
    "lmb300": "Malnate--loc. San Salvatore",
    "lmb338": "Meda--Via Como",
    "lmb175": "Mezzana Bigli",
    "lmb208": "Milano",
    "lmb298": "Milano--Bicocca",
    "lmb289": "Milano--Lambrate",
    "lmb254": "Milano--Maxwell",
    "lmb206": "Milano--via Noto",
    "lmb326": "Milano--Lorenteggio/Primaticcio",
    "lmb322": "Miradolo Terme--via Marconi 29",
    "lmb259": "Monza",
    "lmb286": "Monza--Parco",
    "lmb171": "Monza--Via Della Robbia",
    "lmb224": "Monza--Via Monti e Tognetti",
    "lmb173": "Monza--Via S. Martino",
    "lmb170": "Monza--Via Sgambati",
    "lmb135": "Muggiò",
    "lmb201": "Orsenigo--Via Cascina Foppa 25",
    "lmb320": "Paderno Dugnano",
    "lmb079": "Paladina",
    "lmb213": "Peschiera Borromeo--Bellaria (Mi)",
    "lmb366": "Retorbido--Via Staffora",
    "lmb228": "Robecco sul Naviglio--castellazzo",
    "lmb371": "Rodano--Trenzanesio",
    "lmb087": "Rogeno--Casletto di Rogeno",
    "lmb265": "San Donato Milanese--via primo maggio",
    "lmb241": "San Giovanni Bianco",
    "lmb377": "San Giovanni Bianco--Frazione Cornalita ",
    "lmb189": "Sangiano",
    "lmb220": "Saronno",
    "lmb361": "Senago",
    "lmb362": "Senago--Senago Nord ovest",
    "lmb103": "Seregno--nord",
    "lmb080": "Seregno--ovest",
    "lmb021": "Seregno--Seregno Centro",
    "lmb167": "Sesto San Giovanni--Parco Nord",
    "lmb179": "Treviglio",
    "lmb359": "Triuggio--Canonica",
    "lmb353": "Uboldo",
    "lmb294": "Valbrona--Visino",
    "lmb109": "Valmadrera",
    "lmb358": "Vigano San Martino",
    "lmb335": "Villa d'Ogna--via piave",
    "lmb346": "Zinasco",
    "pmn033": "Vicolungo-Borgo di Zuxiana",
    "pmn047": "Trecate-S. Maria",
    "pmn076": "Novara-sant'Antonio",
    "pmn101": "Cavallirio",
    "pmn105": "Soriso",
    "pmn109": "Sozzago",
    "pmn125": "Arona-Parco della Rocca Borromeo",
    "pmn147": "Galliate",
}


# a list of tuples of period_label, start, end  (solar Timezone)
# period_list = [
#     ["2013-2014", da.datetime(2013,1,1,0,1), da.datetime(2015,1,1,0,0)],
#     ["2015-2016", da.datetime(2015,1,1,0,1), da.datetime(2017,1,1,0,0)],
#     ["2017-2018", da.datetime(2017,1,1,0,1), da.datetime(2019,1,1,0,0)],
# ]
period_list = [
    ["2018-2019", da.datetime(2018,1,1,0,1), da.datetime(2020,1,1,0,0)],
]


def convert_temperature(raw_temp):
    try:
        temperature = round(float(raw_temp), ndigits=1)
    except: 
        temperature = -999.9
    return temperature

def str2naive(string):
    """return a naive datetime object from the corresponding time string"""
    # "2013-06-20 00:30:00" 
    # I know from other metadata that this is an Italian wall time
    dt = da.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
    return dt

def naive2ita(naive_dt):
    """convert a naive Italy wall time to timezone-aware dt,
    with variable offset from UTC, due to Daylight saving time"""
    aware_dt = pytz.timezone("Europe/Rome").localize(naive_dt)
    return aware_dt

def ita2utc(ita_dt):
    """?"""
    # ASTIMEZONE Return a datetime object with new tzinfo attribute tz, adjusting the date 
    # and time data so the result is the same UTC time as self, but in tz’s local time.
    utc_dt = ita_dt.astimezone(pytz.timezone("UTC"))
    return utc_dt

def utc2solar(utc_dt):
    # ASTIMEZONE Return a datetime object with new tzinfo attribute tz, adjusting the date 
    # and time data so the result is the same UTC time as self, but in tz’s local time.
    solar_tz = da.timezone(offset=da.timedelta(hours=1), name="SOLAR")
    solar_dt = utc_dt.astimezone(solar_tz)
    return solar_dt

def utc2naive(utc_dt):
    # trasform aware to naive for the benefit of poor xlsxwriter
    naive_dt = utc_dt.replace(tzinfo=None)
    return naive_dt
    
def str2solar(string):        
    # "2013-06-20 00:30:00"
    naive_dt = da.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
    ita_dt = pytz.timezone("Europe/Rome").localize(naive_dt)
    utc_dt = ita_dt.astimezone(pytz.utc)
    solar_dt = utc_dt + da.timedelta(hours=1)
    solar_dt = solar_dt.replace(tzinfo=None)
    return solar_dt

def interesting(dt, start, end):
    """Return True if datetime is between start and end, 
    otherwise return False."""
    return dt >= start and dt <= end


def process_df(df):
    """all things to do with a single station
    and return a tuple  (station_label, DataFrame)
    """
    # from csv to DataFrame
    #df = pd.read_csv(filepath_or_buffer=filepath, sep=";", decimal = ".")
    #add derived colums
    # df["naive_it_dt"] = df["datetime"].apply(str2naive)
    # df["aware_it_dt"] = df["naive_it_dt"].apply(naive2ita)
    # df["utc_dt"] = df["aware_it_dt"].apply(ita2utc)
    # df["solar_dt"] = df["aware_it_dt"].apply(utc2solar)
    df["solar"] = df["datetime"].apply(str2solar)
    # get station code from the fist field
    station_code = df["code"][1]
    station_label = label_dict[station_code]
    df[station_label] = df["temperature"] 
    return (station_label, df)

def simple_test():
    """print datetime objects and timezone for poor man checking"""
    test_list =  ["2013-12-25 00:30:00", "2013-06-2 00:30:00", ]
    for timestring in test_list:
        naive = str2naive(timestring)
        ita = naive2ita(naive)
        utc = ita2utc(ita)
        solar = utc2solar(utc)
        print("naive", naive, naive.tzinfo)
        print("ita", ita, ita.tzinfo)
        print("utc", utc, utc.tzinfo)
        print("solar", solar, solar.tzinfo)



def hour_mean(df):
    """create a mean of all values I have in the delta of time of 1 hour
    I assign the result to the last possible value

    Si prendono i dati di temperatura di [fomd1, fomd2, fomd3] (tar.gz), 
    per 14 stazioni, e si calcolerà la media oraria.
    Il dato delle ore 8:00 (fine misura) sarà prodotto in base ai record del 
    periodo dalle 07:00:01 alle 08:00:00 ().
    Non ci devono essere buchi, ovvero tutte le ore devono essere presenti, con 
    un valore che indichi dato mancante, ossia o -999 oppure cella vuota.
    """


def create_excel(df, out_path):
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(out_path, engine='xlsxwriter')
    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Sheet1')
    # Get the xlsxwriter workbook and worksheet objects.
    workbook  = writer.book
    worksheet = writer.sheets['Sheet1']
    # Add some cell formats
    #format1 = workbook.add_format({'num_format': '0,0'})
    # Set the column width (and maybe the format).
    worksheet.set_column(0,0, 4)
    worksheet.set_column(1,1, 6)
    worksheet.set_column(2,2, 17)
    worksheet.set_column(1,1, 17)
    worksheet.set_column(3,3, 28)
    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
    # start = df["solar"].min()
    # end = df["solar"].max()
    # print("{} {} {}".format(label, start, end)) 