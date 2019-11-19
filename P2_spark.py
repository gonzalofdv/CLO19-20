#!/usr/bin/python
#Gonzalo Figueroa del Val

from pyspark import SparkConf, SparkContext
import string
import sys
import re

#configuraciones
conf = SparkConf().setMaster('local').setAppName('URLaccess')
sc = SparkContext(conf=conf)

RDDarch = sc.textFile("access_log")

palabras = RDDarch.map(lambda line: (line.split('"')[1]))

aux = palabras.map(lambda line: line.split('/')).filter(lambda line: len(line) > 1).map(lambda line: (str(line[1]), 1))
sol = aux.reduceByKey(lambda a, b: a+b)

sol.saveAsTextFile("access.txt")
