#!/usr/bin/python

import sys

previous = None
suma = 0

for line in sys.stdin:
	key, value = line.split('\t')

	if key != previous:
		if previous is not None:
			print str(suma) + '\t' + previous
		previous = key
		suma = 0

	suma = suma + int(value)

print str(suma) + '\t' + previous