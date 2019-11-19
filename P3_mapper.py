#!/usr/bin/python

import sys
import re

linea = 0
basura = ""

for line in sys.stdin:
	if linea == 0:
		re.sub(r'^\W+|W+$', '', basura)
		linea = linea + 1
	else:
		line = re.sub(r'^\W+|\W+$', '', line)
		words = line.split(',', 7)
		valor = (float(words[4]) + float(words[1]))/2
		print(words[0][0:4] + "\t1" + words[4])

