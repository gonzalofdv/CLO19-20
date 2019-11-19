#!/usr/bin/python

import sys
import re

siguiente = False

for line in sys.stdin:

	line = re.sub(r'^\W+|\W+$', '', line)
	words = re.split(r"\W+", line)

	for word in words:
		if siguiente:
			print(word.lower() + "\t1")
			siguiente = False
		if word == "GET" or word == "POST":
			siguiente = True