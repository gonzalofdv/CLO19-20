#!/usr/bin/python
#Gonzalo Figueroa del Val

from pyspark import SparkConf, SparkContext
import string
import sys

#configuration
conf = SparkConf().setMaster('local').setAppName('WordCount')
sc = SparkContext(conf=conf)

RDDtext = sc.textFile("input.txt")
palabra = sys.argv[1]

palabras = RDDtext.flatMap(lambda line: line.split())

resultado = palabras.map(lambda word: (str(word.lower()), 1))

agregado = resultado.reduceByKey(lambda a, b: a+b)
result = agregado.filter(lambda line: palabra in line)

result.saveAsTextFile("output.txt")
