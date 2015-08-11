from apriori import *

mushDataSet=[line.split() for line in open('mushroom.dat').readlines()]
L,suppData=apriori(mushDataSet,0.3)

for item in L[3]:
	if item.intersection('2'):
		print item

