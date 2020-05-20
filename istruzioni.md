#Inserimento dei dati di meteonetwork.

# dati giornalieri

comune e area

destinazione virgola.
temp min med max t

un unico file 
colonna a date 1-11-12 al 18
foglio per ognuno dei tre parametri
nomi

data
nome stazione (= solo nome comune OR comune e area)

i dati non sono continuativi in input
devono essere continui in output
separatore virgola
1 decimale solo

ordine delle stazionu.xls

xlsx



## dati orari meteonetwork di 14 stazioni

https://drive.google.com/open?id=1zBK_zvfdrLXY5QmZT2bCBWkRd8jwR2_b



da punto a virgola

unire i due file della stessa stazione

un file 
un foglio per ognui stazione
seregno, codogno, 

nome della stazione anche come nome della colonna.

sono in ora locale. 
sarebbe da trasformarli in ora solare UTC+1

Al poste delle 00:00 . mettere 24:00 del giorno precedente


    Many progresses
    
    + Read csv files using csv.DictReader.
    + Convert date string to datetime object.
    + Convert temperature from string to float.
    + Find a way to deal with local time to solar time.
    + Use Station name (label) instead of Station id.
    
    TODO
    
    + Only one decimal in temperature.
    + Write results to Excel file.
    + convert 24:00 to 00:00.
    
    Ciao Stefano,
non uccidermi ma ho ancora un problema con Meteonetwork suborario: in pratica i dati di Mezzana Bigli e di Treviglio sono talmente tanti
(hanno il dettaglio al minuto) che non ci stanno tutti sul file excel! Mezzana mi si ferma al 2015...
Credo che per almeno queste due stazioni bisogna prevedere tre file (2013-2014, 2015-2016,2017-2018).
Se farlo solo per due è un problema, possiamo valutare di farlo per tutte le stazioni lo spezzettamento in tre.

Facciamolo per tutte.
aggiungere alla fine le annate a cui si riferiscono.
orari di fine misura.


Ciao
Samantha


# -*- coding: utf-8 -*-
"""
Created on Fri May 15 10:40:40 2020

@author: Carlesso


lmb179;45,5100361481069;9,5751686085714;125;Davis Vantage Pro Plus 2;Lombardia;Treviglio;;BG;Treviglio;Treviglio
lmb175;45,07;8,85;76;Davis Vantage Pro 2;Lombardia;Mezzana Bigli;;PV;Mezzana Bigli;Mezzana Bigli
"""


aggregare al dato orario

sono orari di fine misura
con ora solare
da 00:01 --01:00 fa dato orario 
