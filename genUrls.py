SLEEP_TIME = "30"
TEST_TIME = "5M"
BYTES_IN_KB = 1024
BYTES_IN_GB = 1074000000
BYTES_IN_MB = 1049000
CLIENT_INCREMENTS = 20
MAX_CLIENTS = 121
RAM = 512 * BYTES_IN_MB
DISK = 2048 * BYTES_IN_MB
PAGE = 10 * BYTES_IN_KB
OBJRAMSIZE = 20488
increments = [1, 2, 4, 6]
URLPATH = 'urls/'
url = 'http://192.168.2.11:3000/'
print map(lambda x: OBJRAMSIZE*x*PAGE/BYTES_IN_MB, increments)

numUrls = map(lambda x: OBJRAMSIZE*x, increments)

for i in range(0, len(numUrls)):
	f = open(URLPATH + str(numUrls[i]), 'w')
	if i == 0:
		startVal = 0
	else:
		startVal = numUrls[i-1]
	print str(startVal) + " to " + str(numUrls[i])
	for d in range(startVal, numUrls[i]):
		f.write(url + str(d) + '\n')
	f.close()



