#!/usr/bin/python

import sys
import re

numlinea = 0
basura = ""

for line in sys.stdin:
	line = re.sub(r'^\W+|\W+$', '', line)
	valores = line.split('\t', 2)
	print(valores[0] + "\t" + valores[1])