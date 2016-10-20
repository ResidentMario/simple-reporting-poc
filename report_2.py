import sqlite3
import math

conn = sqlite3.connect("mth4320.db")
c = conn.cursor()
results = []
for borough in ["MN", "BK", "QN", "BX", "SI"]:
	results += c.execute("SELECT NUMFLOORS FROM {0}".format(borough)).fetchall()

from collections import Counter
counts = Counter(results)
for tup in sorted(counts.items()):
	c = tup[0][0]
	n = tup[1]
	if c % 1 != 0:
		pass
	else:
		print("There are {0} buildings in New York City with {1} floors.".format(int(n), c))