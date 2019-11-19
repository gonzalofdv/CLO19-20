#!/usr/bin/python

import sys

previous = None
pelis = ""
rank1 = []
rank2 = []
rank3 = []
rank4 = []
rank5 = []

for line in sys.stdin:
	key, value = line.split('\t')
	indice = float(value)

	if indice < 1.0:
		rank1.append(key)
	elif indice < 2.0:
		rank2.append(key)
	elif indice < 3.0:
		rank3.append(key)
	elif indice < 4.0:
		rank4.append(key)
	elif indice < 5.0:
		rank5.append(key)

print("Range 1: 1 or lower")
for i in rank1:
	print(i)
print("")

print("Range 2: 2 or lower (but higher than 1)")
for i in rank2:
	print(i)
print("")

print("Range 3: 3 or lower (but higher than 2)")
for i in rank3:
	print(i)
print("")

print("Range 4: 4 or lower (but higher than 3)")
for i in rank4:
	print(i)
print("")

print("Range 5: 5 or lower (but higher than 4)")
for i in rank5:
	print(i)
print("")