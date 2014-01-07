import matplotlib.pyplot as plt
import csv
import numpy as np
import re
from mpl_toolkits.mplot3d import Axes3D
from pylab import *
import collections

'''
REQRATE = 8
RAMSIZE = 1
THRUPUT = 9
NUMUSERS = 2
RESTIME = 7
TRIALNUM = 0
CONCURRENCY = 10

RAM = "209712"
'''
CONCURRENCY = 7
THRUPUT = 6
ELAPSEDTIME = 2


data = csv.reader(open("/Users/Dale/jp1/beaglecache/logs/ramonly"), delimiter=',')

data.next()

numClients = []
numUrls = []
concurrency = []
thruput = []
elapsedTime = []
x = []
y = []
for row in data:
	if row[0][0] == '*':
		a = re.findall(r'[0-9]+', row[0])
		numUrls.append(int(a[0]))
		numClients.append(int(a[1]))
	else:
		concurrency.append(float(row[CONCURRENCY]))
		thruput.append(float(row[THRUPUT]))
		elapsedTime.append(float(row[ELAPSEDTIME]))
'''
	if row[RAMSIZE] == RAM and row[TRIALNUM] == '1':
		x.append(float(row[NUMUSERS]))
		y.append(float(row[RESTIME]))
		z.append(float(row[THRUPUT]))
		c.append(float(row[CONCURRENCY]))
'''

urlRange = set(numUrls)
urlRange2 = sorted([d for d in urlRange])
urlRange = urlRange2
manyY = []
manyX = []
labels = []

for entry in urlRange:
	manyY.append([thruput[d] for d in range(len(thruput)) if elapsedTime[d] > 200 and numUrls[d] == entry])
	manyX.append([concurrency[d] for d in range(len(thruput)) if elapsedTime[d] > 200 and numUrls[d] == entry])
	labels.append(entry)

colors=['r', 'g', 'b', 'm', 'y']

for i in range(0, len(manyX)):
	b = plt.plot(manyX[i], manyY[i], '-' + colors[i], label=str(labels[i]) + " KB" )
legend()
plt.xlabel("Concurrency")
plt.ylabel("Throughput (MB/sec)")
#plt.plot(manyX[0], manyY[0], '-m', manyX[1], manyY[1], '-b', manyX[2], manyY[2], '-g', manyX[3], manyY[3], '-r')
plt.show()
#plt.savefig('/Users/Dale/jp1/beaglecache/graphs/ConcurrencyVersusObjRamCacheSize')
