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