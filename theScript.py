#!/usr/bin/python
# ram god only 373860 KB max 

import sys
import os
import math
import re

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
baseURL = "http://192.168.2.11:3000/"
URLSPATH = "urls/"
LOGPATH = "logs/"
VERBOSEPATH = "logs/verbose/"
incrementsRAM = []
#incrementsRAM = [RAM*.2, RAM*.4, RAM*.6, RAM*.8]
#incrementsDisk = [DISK*.2, DISK*.4]
incrementsDisk = [DISK*.2, DISK*.4, DISK*.6, DISK*.8]
incrementsRAM = []
#incrementsDisk = [502*BYTES_IN_MB]
conglomerate = incrementsRAM + incrementsDisk

def main():
	congObjs = map(bytesToPages, conglomerate)
	if len(sys.argv) < 2:
		print "Use --ram or --disk or --ramdisk or --genurls"
		return
	elif sys.argv[1] == "--clean":
		logs = os.listdir(LOGPATH)
		for entry in logs:
			os.remove(LOGPATH + entry)
		if len(os.listdir(LOGPATH)) == 0:
			print "All clean"
		else:
			print "An error occured in cleaning up"
	elif sys.argv[1] == "--genurls":
		genUrls(congObjs, URLSPATH)
	elif sys.argv[1] == "--ram":
		ramObjs = congObjs[0:len(incrementsRAM)]
		map(lambda numObjs: fillCache(numObjs) and runTestOpts(URLSPATH + str(numObjs), timet= TEST_TIME, logfile = LOGPATH + "ramonly"), ramObjs)
	elif sys.argv[1] == "--disk":
		diskObjs = congObjs[len(incrementsRAM):]
		map(lambda numObjs: fillCache(numObjs) and runTestOpts(URLSPATH + str(numObjs), timet= TEST_TIME, logfile = LOGPATH + "diskonly" ), diskObjs)
	elif sys.argv[1] == "--ramdisk":
		map(lambda numObjs: fillCache(numObjs) and runTestOpts(URLSPATH + str(numObjs), timet= TEST_TIME, logfile = LOGPATH + "ramanddisk"), congObjs)


def bytesToPages(byteVal):
	return int(math.ceil(byteVal / PAGE))

def genUrls(fileNameDict, directoryName):
	urlsDir = os.listdir(directoryName)
	for entry in fileNameDict:
		if not str(entry) in urlsDir:
			f = open(URLSPATH + str(entry), 'w')
			i = 0
			while i < entry:
				thisUrl = baseURL + str(i) + '\n'
				f.write(thisUrl)
				i = i + 1
			f.close()
	print "Wrote the files"

# [,)
def fillCache(numUrls):
	filePath = URLSPATH + str(numUrls)
	commandString = "siege --quiet -f " + filePath + " -r" + str(numUrls)
	print commandString
	os.system(commandString)
	return True

def runTestOpts(urlFile, timet, logfile):
	maxClients = MAX_CLIENTS
	messageString = "**file" + str(urlFile) + "clients"
	commandString = "siege --internet --verbose -f " + urlFile + " -t" + timet + " -l" + logfile
	clientTrials = range(0, maxClients, CLIENT_INCREMENTS)
	clientTrials[0] = 1
	for clientNum in clientTrials:
		os.system("echo " + messageString + str(clientNum) + " >> " + VERBOSEPATH + re.findall(r'[0-9]+',urlFile)[0])
		thisCommand = commandString + " -c" + str(clientNum) + " -m " + messageString + str(clientNum) + " >> " + VERBOSEPATH + re.findall(r'[0-9]+',urlFile)[0]
		print "Command was " + thisCommand
		os.system(thisCommand)
		os.system("sleep " + str(SLEEP_TIME))

# Takes a file oldFile and creates a new file, newFile, that consists of all entries in oldFile
# starting at line startLine
def makeTempFile(oldFile, newFile, startLine):
	oldf = open(oldFile, 'r')
	newf = open(newFile, 'w')

	i = 0
	while i < startLine:
		oldf.next()
		i = i + 1

	newf.writelines(oldf)
	newf.close()
	oldf.close()


if __name__ == '__main__':
	main()