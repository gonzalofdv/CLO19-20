#!/usr/bin/python

import sys

previous = None
suma = 0.0
num = 0

for line in sys.stdin:
	key, value = line.split('\t')

	if key != previous:
		if previous is not None:
			media = suma / num
			num = 0
			print(previous + "\t" + str(media))
		previous = key
		suma = 0.0

	suma = suma + float(value)
	num = num + 1
media = suma / num
print(previous + "\t" + str(media))