#!/usr/bin/python
#Gonzalo Figueroa del Val

from pyspark import SparkConf, SparkContext
from pyspark import SQLContext
import string
import sys
from pyspark.sql import*
from pyspark.sql.types import*

conf = SparkConf().setMaster('local').setAppName('Meteoritos')
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

RDDtext = sc.textFile("Meteorite_Landings.csv") #cargar csv

mapa = RDDtext.flatMap(lambda line: line.split("\n")) #creacion de un flatmap
mapa2 = mapa.map(lambda line: Row(tipo=line.split(",")[3], masa=line.split(",")[4])) #map(tipo, masa)

datFram = sqlContext.createDataFrame(mapa2) #convertimos el mapa en dataframe

media = datFram.groupby('tipo').agg({'masa': 'mean'}) #mean hace la media
media.orderBy("tipo").write.csv('solucion') #exportar solucion
