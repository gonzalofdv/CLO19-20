#!/usr/bin/python
#Gonzalo Figueroa del Val

from pyspark import SparkConf, SparkContext
import string
import sys

conf = SparkConf().setMaster('local').setAppName('MediaPrecios')
sc = SparkContext(conf=conf)

textRDD = sc.textFile("GOOGLE.csv")

data = textRDD.filter(lambda line: "Date" not in line) #eliminar o ignorar primera linea
stock = data.map(lambda line: (int((line.split(',')[0]).split('-')[0]),float(line.split(',')[4]))) #map(ano, precio)
number = data.map(lambda line: (int((line.split(',')[0]).split('-')[0]),1))
aux1 = stock.reduceByKey(lambda a, b: a+b)
aux2 = number.reduceByKey(lambda a, b: a+b)
union = aux1.join(aux2)
result = union.map(lambda line: (line[0], line[1][0]/line[1][1]))

result.saveAsTextFile("media.txt")

