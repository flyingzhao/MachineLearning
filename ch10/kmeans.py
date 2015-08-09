from numpy import *

def loadData(filename):
	dataMat=[]
	fr=open(filename)
	for line in fr.readlines():
		curline=line.strip().split('\t')
		fltLine=map(float,curline)
		dataMat.append(fltLine)
	return dataMat

def distEclud(vecA,vecB):
	return sqrt(sum((vecA-vecB)**2))

def randCent(dataSet,k):
	dataSet=mat(dataSet)
	n=shape(dataSet)[1]
	centroids=mat(zeros((k,n)))
	for j in range(n):
		minJ=min(dataSet[:,j])
		rangeJ=float(max(dataSet[:,j])-minJ)
		print random.rand(k,1)
		centroids[:,j]=minJ+rangeJ*random.rand(k,1)
		# print centroids
	return centroids




def drawGraph(dataMat):
	import matplotlib.pyplot as plt
	fig=plt.figure()
	ax=fig.add_subplot(111)
	ax.scatter(dataMat[:,0],dataMat[:,1])
	plt.show()

dataMat=loadData('testSet.txt')
# drawGraph(array(dataMat))
# print distEclud(array([1,2]),array([3,4]))
print randCent(dataMat,4)