#!/usr/bin/python

import sys
import re

numlinea = 0
patron = sys.argv[1]

for line in sys.stdin:
	numlinea = numlinea + 1

	line = re.sub(r'^\W+|\W+$', '', line)
	palabras = re.split(r"\W+", line)

	for palabra in palabras:
		if patron == palabra:
			print(palabra.lower() + "\t" + str(numlinea))