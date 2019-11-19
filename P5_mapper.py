#!/usr/bin/python

import sys
import re

for line in sys.stdin:
	line = re.sub(r'^W+|\W+$', '', line)
	datos = line.split(',')
	print(datos[3] + "\t" + datos[4])