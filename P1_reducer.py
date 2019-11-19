#!/usr/bin/python

import sys

previous = None

result = ""
word = ""
numlinea = 0
for line in sys.stdin:
	word, numlinea = line.split('\t')
	result = result + numlinea
	
print(result)