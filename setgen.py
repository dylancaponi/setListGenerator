from mmap import mmap,ACCESS_READ
from xlrd import open_workbook
import random
from pandas import *

# generate random setlist size
setSize = random.randint(14,16)
print str(setSize) + ' songs'

# pull data from excel file
xlsx = ExcelFile('STS9.xlsx')
df = xlsx.parse(xlsx.sheet_names[2])
fullList = df.to_dict()

numSongType = []
setList = []
# count number of songs of each type
for i in range(1,4):
	count = 0
	for songNum in fullList['TYPE']:
		if fullList['TYPE'][songNum]==i:
			count +=1
	numSongType.append(count)

# iterate through set list
for i in range(setSize):
		# choose random type based on probability
		# position in setlist should affect chances
		randNum = random.randint(1,100)
		if randNum < 25 - i:
			typeSong = 1	# 25%
		elif randNum > 30 + i:
			typeSong = 2	# 70% meat of the sets
		else:
			typeSong = 3 	# 5% of sets and chance increases further down setlist
		# choose random song of type
		#print typeSong

		# choose a random # anywhere in the whole list and then move down looking for a match
		randNum = random.randint(0,len(fullList['NAME'])-1)
		#print randNum
		while fullList['TYPE'][randNum]!=typeSong or fullList['NAME'][randNum] in setList:
			#print randNum
			randNum +=1
			if randNum >= len(fullList['NAME']):
				randNum = 0
		print fullList['NAME'][randNum]
		setList.append(fullList['NAME'][randNum])

#print setList

# export to csv or xls, xlsx
