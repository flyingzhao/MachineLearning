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
	return sqrt(sum(power(vecA-vecB,2)))

def randCent(dataSet,k):
	dataSet=mat(dataSet)
	n=shape(dataSet)[1]
	centroids=mat(zeros((k,n)))
	for j in range(n):
		minJ=min(dataSet[:,j])
		rangeJ=float(max(dataSet[:,j])-minJ)
		centroids[:,j]=minJ+rangeJ*random.rand(k,1)
		# print centroids
	return centroids

def kMeans(dataSet,k,distMeans=distEclud,createCent=randCent):
	m=shape(dataSet)[0]
	clusterAssment=mat(zeros((m,2)))
	centroids=createCent(dataSet,k)
	clusterChanged=True
	while clusterChanged:
		clusterChanged=False
		for i in range(m):
			minDist=inf;minIndex=-1
			for j in range(k):
				distJI=distMeans(centroids[j,:],dataSet[i,:])
				if distJI<minDist:
					minDist=distJI
					minIndex=j
			if clusterAssment[i,0]!=minIndex:clusterChanged=True
			clusterAssment[i,:]=minIndex,minDist**2
		# print centroids
		for cent in range(k):
			ptsInClust=dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]
			centroids[cent,:]=mean(ptsInClust,axis=0)
	return centroids,clusterAssment
	
def biKmeans(dataSet,k,distMeans=distEclud):
	m=shape(dataSet)[0]
	clusterAssment=mat(zeros((m,2)))
	centroid0=mean(dataSet,axis=0).tolist()
	centList=[centroid0]
	for j in range(m):
		clusterAssment[j,1]=distMeans(mat(centroid0),dataSet[j,:])**2
	while (len(centList)<k):
		lowestSSE=inf
		for i in range(len(centList)):
			ptsInCurrCluster=dataSet[nonzero(clusterAssment[:,0].A==i)[0],:]
			centroidMat,splitClusterAss=kMeans(ptsInCurrCluster,2,distMeans)
			# print centroidMat,splitClusterAss
			sseSplit=sum(splitClusterAss[:,1])
			sseNotSplit=sum(clusterAssment[nonzero(clusterAssment[:,0].A!=i)[0],1])
			print 'ssesplit,and not split',sseSplit,sseNotSplit
	
			if (sseSplit+sseNotSplit)<lowestSSE:
				bestCentToSplit=i
				bestNewCents=centroidMat
				bestClustAss=splitClusterAss.copy()
				lowestSSE=sseSplit+sseNotSplit
		bestClustAss[nonzero(bestClustAss[:,0].A==1)[0],0]=len(centList)
		bestClustAss[nonzero(bestClustAss[:,0].A==0)[0],0]=bestCentToSplit
		print 'the bestCentToSplit is',bestCentToSplit
		print 'the len of bestClustAss is',len(bestClustAss)
		centList[bestCentToSplit]=bestNewCents[0,:]
		centList.append(bestNewCents[1,:])
		clusterAssment[nonzero(clusterAssment[:,0].A==bestCentToSplit)[0],:]=bestClustAss
	return centList,clusterAssment

			


def drawGraph(dataMat):
	import matplotlib.pyplot as plt
	fig=plt.figure()
	ax=fig.add_subplot(111)
	ax.scatter(dataMat[:,0],dataMat[:,1])
	plt.show()

def drawGraph1(dataMat,centroids,cluster):
	import matplotlib.pyplot as plt
	fig=plt.figure()
	ax=fig.add_subplot(111)

	ptsInClust=dataMat[nonzero(cluster[:,0].A==0)[0]]
	ax.scatter(ptsInClust[:,0],ptsInClust[:,1],color='blue')
	ax.scatter(centroids[0,0],centroids[0,1],color='blue',s=80,marker='+')

	ptsInClust=dataMat[nonzero(cluster[:,0].A==1)[0]]
	ax.scatter(ptsInClust[:,0],ptsInClust[:,1],color='green')
	ax.scatter(centroids[1,0],centroids[1,1],color='green',s=80,marker='+')
	
	ptsInClust=dataMat[nonzero(cluster[:,0].A==2)[0]]
	ax.scatter(ptsInClust[:,0],ptsInClust[:,1],color='yellow')
	ax.scatter(centroids[2,0],centroids[2,1],color='yellow',s=80,marker='+')

	ptsInClust=dataMat[nonzero(cluster[:,0].A==3)[0]]
	ax.scatter(ptsInClust[:,0],ptsInClust[:,1],color='black')
	ax.scatter(centroids[3,0],centroids[3,1],color='black',s=80,marker='+')
	plt.show()

# dataMat=loadData('testSet.txt')
# drawGraph(array(dataMat))
# print distEclud(array([1,2]),array([3,4]))
# print randCent(dataMat,4)

#kmeans
# cent,cluster=kMeans(array(dataMat),4)
# print cent,cluster
# drawGraph1(array(dataMat),cent,cluster)

#biKmeans
# dataMat=loadData('testSet.txt')
# cent,cluster=biKmeans(array(dataMat),4)
# cent=vstack((vstack((vstack((array(cent[0]),array(cent[1]))),array(cent[2]))),array(cent[3])))
# drawGraph1(array(dataMat),cent,cluster)
