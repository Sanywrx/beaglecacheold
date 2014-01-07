import matplotlib.pyplot as plt
import csv
import numpy as np
import re 

def find_nearest(arr,value):
	return min(arr, key=lambda x:abs(x-value))

RESTIME = 5
KEY = 1
querySpace = '17476'

data = csv.reader(open("/Users/Dale/jp1/beaglecache/logs/verbose/81952"), delimiter=',')

resTime = []

numUrls = []
thisUrl = 0
numClients = []
thisClients = 0
hundredtimes = [42543, 43382, 44220]
times = [100, 120, 140]

for row in data:
	if len(row) > RESTIME:
		resTime.append(float(row[RESTIME]))
		thisNumClient = re.findall(r'\s[0-9]+\s',row[KEY])
		if len(thisNumClient) < 1:
			continue
		thisNumClient = int(thisNumClient[0])

		if thisNumClient == 100:
			timestamp = re.findall(r'[0-9]+[:][0-9]+[:][0-9]', row[KEY])[0]
			if len(re.findall(r'[0-9]+', timestamp)) != 3:
				print timestamp
			(h,m,s) = map(lambda x: int(x), re.findall(r'[0-9]+', timestamp))
			timestampSec = 60*60*h + 60*m + s
			nearestTime = find_nearest(hundredtimes, timestampSec)
			thisNumClient = times[hundredtimes.index(nearestTime)]
		
		numClients.append(thisNumClient)


clientNum = 160
x = [resTime[d] for d in range(1, len(resTime)) if resTime[d] < 10 and numClients[d] == clientNum]
hist, bins = np.histogram(x, bins=60)
width = 0.8 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, hist, align='center', width=width)
#plt.plot(bins, hist)
#plt.bar(center, hist, align='center')
plt.title("Varying Response Time Distribution with Disk and RAM Cache, " + str(clientNum) + " Clients")
plt.xlabel("Response Time (seconds)")
plt.ylabel("Number of Requests")
#plt.show()
plt.savefig('/Users/Dale/jp1/beaglecache/graphs/ResponseBar81952urls' + str(clientNum) + "clients")
