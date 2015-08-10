from kmeans import *

def distSLC(vecA,vecB):
	a=sin(vecA[0,1]*pi/180)*sin(vecB[0,1]*pi/180)
	b=cos(vecA[0,1]*pi/180)*cos(vecB[0,1]*pi/180)*cos(pi*(vecB[0,0]-vecB[0,0])/180)
	return arccos(a+b)*6371.0

import matplotlib
import matplotlib.pyplot as pl
def clusterClub(numClust=9):
	datList=[]
	for line in open('places.txt').readlines():
		lineArr=line.split('\t')
		datList.append([float(lineArr[4]),float(lineArr[3])])
	datMat=mat(datList)
	myCentroids,clustAssing=biKmeans(datMat,numClust,distMeans=distSLC)
	print 'total error',sum(clustAssing[:,1])
	fig=pl.figure()
	rect=[0.1,0.1,0.8,0.8]
	scatterMarker=['s','o','^','8','p','d','v','h','>','<']
	axprops = dict(xticks=[], yticks=[])
   	ax0=fig.add_axes(rect, label='ax0', **axprops)
	imgP=pl.imread('Portland.png')
	ax0.imshow(imgP)
	ax1=fig.add_axes(rect,label='ax1', frameon=False)
	for i in range(numClust):
		ptsInCurrClusters=datMat[nonzero(clustAssing[:,0].A==i)[0],:]
		markerStyle=scatterMarker[i % len(scatterMarker)]
		ax1.scatter(ptsInCurrClusters[:,0].flatten().A[0],ptsInCurrClusters[:,1].flatten().A[0],marker=markerStyle,s=90)
	ax1.scatter(myCentroids[:,0].flatten().A[0],myCentroids[:,1].flatten().A[0],marker='+',s=300,color='red')
	pl.show()

clusterClub()
