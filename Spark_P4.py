#!/usr/bin/python
#Gonzalo Figueroa del Val

from pyspark import SparkConf, SparkContext
import string
import sys

conf = SparkConf().setMaster('local').setAppName('Movies')
sc = SparkContext(conf=conf)

RDDtext = sc.textFile("ratings.csv")

rang1 = 1.0
rang2 = 2.0
rang3 = 3.0
rang4 = 4.0
rang5 = 5.0

ratingsData = RDDtext.filter(lambda line: "userId" not in line).map(lambda line: (int(line.split(',')[1]), float(line.split(',')[2]))) #mapa(pelicula, valoracion)
numPelis = RDDtext.filter(lambda line: "userId" not in line).map(lambda line: (int(line.split(',')[1]), 1)) #mapa (pelicula, 1)
agregadoRating = ratingsData.reduceByKey(lambda a, b: a+b) #mapa(pelicula, sumaValoraciones)
agregadoNum = numPelis.reduceByKey(lambda a, b: a+b) #mapa(pelicula, numVeces)
union = agregadoRating.join(agregadoNum) #mapa(pelicula, (sumaValoraciones, numVeces))

media = union.map(lambda line: (line[0], line[1][0]/line[1][1])) #mapa(pelicula, notaMedia)

rango1 = media.filter(lambda line: line[1] <= rang1).filter(lambda line: line[1] >= 0.0)
rango2 = media.filter(lambda line: line[1] <= rang2).filter(lambda line: line[1] > 1.0)
rango3 = media.filter(lambda line: line[1] <= rang3).filter(lambda line: line[1] > 2.0)
rango4 = media.filter(lambda line: line[1] <= rang4).filter(lambda line: line[1] > 3.0)
rango5 = media.filter(lambda line: line[1] <= rang5).filter(lambda line: line[1] > 4.0)

rango1.saveAsTextFile("ratings1.txt")
rango2.saveAsTextFile("ratings2.txt")
rango3.saveAsTextFile("ratings3.txt")
rango4.saveAsTextFile("ratings4.txt")
rango5.saveAsTextFile("ratings5.txt") #Cada rango en un fichero distinto
