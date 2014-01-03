import matplotlib.pyplot as plt
import csv
import numpy as np

QUERYSPACE = "26214"
NUMCLIENTS = "120"
'''
CONUSERS = 6
REQRATE = 7
RAMSIZE = 
THRUPUT = 
'''
data = csv.reader(open("/Users/Dale/Downloads/Disk2.csv"), delimiter=',')

#data.next()

'''
x = []
y = []

for row in data:
	x.append(float(row[CONUSERS]))
	y.append(float(row[REQRATE]))
'''
x = []
for row in data:
	if row[0] == QUERYSPACE and row[1] == NUMCLIENTS:
		x.append(float(row[2]))

hist, bins = np.histogram(x, bins=70)
center = (bins[:-1] + bins[1:]) / 2
width = 0.9 * (bins[1] - bins[0])
plt.bar(center, hist, align='center', width=width)
plt.title(NUMCLIENTS + " Clients Query " + QUERYSPACE + " 12K objects, max 8738 objects in RAM")
plt.xlabel("Response Time (seconds)")
plt.ylabel("Number of requests")
#p1 = plt.scatter(x,y)
#plt.show()
plt.savefig('/Users/Dale/jp1/beaglecache/graphs/' + QUERYSPACE + 'users' + NUMCLIENTS + 'clients')
