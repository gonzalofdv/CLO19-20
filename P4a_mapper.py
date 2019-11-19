#!/usr/bin/python

import sys
import re

numlinea = 0
basura = ""

for line in sys.stdin:
	if numlinea == 0:
		re.sub(r'^\W+|\W+$', '', basura)
		numlinea = numlinea + 1
	else:
		line = re.sub(r'^\W+|\W+$', '', line)
		datos = line.split(',', 4)
		print(datos[1] + "\t" + datos[2])