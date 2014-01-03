import matplotlib.pyplot as plt
import csv
import numpy as np

REQRATE = 8
RAMSIZE = 1
THRUPUT = 9
NUMUSERS = 2

RAM = "104856"
data = csv.reader(open("/Users/Dale/jp1/beaglecache/RamCacheFixed.csv"), delimiter=',')

data.next()

x = []
y = []

for row in data:
	if row[RAMSIZE] == RAM:
		x.append(float(row[NUMUSERS]))
		y.append(float(row[REQRATE]))


plt.title("Req/s of " + RAM + "KB RAM-only cache with varying concurrent users")
plt.xlabel("Concurrent Users")
plt.ylabel("Requests/sec")
plt.scatter(x,y)
#plt.show()
plt.savefig('/Users/Dale/jp1/beaglecache/graphs/RAMOnly ' + RAM + ' KBReqrate')
