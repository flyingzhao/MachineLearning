from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt

def createDataSet():
	group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels=['A','A','B','B']
	return group,labels

def classify0(inX,dataSet,labels,k):
	dataSetSize=dataSet.shape[0]#get the number of rows
	diffMat=tile(inX,(dataSetSize,1))-dataSet
	sqDiffMat=diffMat**2
	sqDistances=sqDiffMat.sum(axis=1)
	distances=sqDistances**0.5
	sortedDistIndicies=distances.argsort()
	classCount={}
	for i in range(k):
		voteIlabel=labels[sortedDistIndicies[i]]
		classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
	x=classCount.iteritems()
	sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
	return sortedClassCount[0][0]

# group,labels=createDataSet()
# a=classify0([0,0],group,labels,3)		
# print a

def file2matrix(filename):
	fr=open(filename)
	numberOfLines=len(fr.readlines())
	returnMat=zeros([numberOfLines,3])
	classLabelVector=[]
	fr=open(filename)
	index=0
	for line in fr.readlines():
		line=line.strip()
		listFromLine=line.split('\t')
		returnMat[index,0:3]=listFromLine[0:3]
		classLabelVector.append(int(listFromLine[-1]))
		index+=1
	return returnMat,classLabelVector
				
# returnMat,classLabelVector=file2matrix('datingTestSet2.txt')
# print returnMat,classLabelVector

# fig=plt.figure()
# ax=fig.add_subplot(111)
# ax.scatter(returnMat[:,0],returnMat[:,1],15.0*array(classLabelVector),15.0*array(classLabelVector))
# plt.show()

def autoNorm(dataSet):
	minVals=dataSet.min(0)
	maxVals=dataSet.max(0)
	ranges=maxVals-minVals
	normDataSet=zeros(shape(dataSet))
	m=dataSet.shape[0]
	normDataSet=dataSet-tile(minVals,(m,1))
	normDataSet=normDataSet/tile(ranges,(m,1))
	return normDataSet,ranges,minVals
# normMat,ranges,minVals=autoNorm(returnMat)
# print normMat,ranges

def datingClassTest():
	hoRatio=0.10
	datingDataMat,datingLabels=file2matrix('datingTestSet2.txt')
	normMat,ranges,minVals=autoNorm(datingDataMat)
	m=normMat.shape[0]
	numTestVecs=int(m*hoRatio)
	errorCount=0.0
	for i in range(numTestVecs):
		classifierResult=classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],5)
		# print "the classifier came back with:%d,the real answer is: %d"%(classifierResult,datingLabels[i])
		if classifierResult!=datingLabels[i]:
			errorCount+=1.0
			print "the classifier came back with:%d,the real answer is: %d"%(classifierResult,datingLabels[i])
	print "Total error is:%f"%(errorCount/float(numTestVecs))

# datingClassTest()

def classifyPerson():
	resultList=['Not at all','in small doses','in large doses']
	percentTats=float(raw_input("percent of time spent playing video game?"))
	ffMiles=float(raw_input("frequent flier miles earned per year?"))
	iceCream=float(raw_input("liters of ice cream consumed per year?"))
	datingDataMat,datingLabels=file2matrix('datingTestSet2.txt')
	normMat,ranges,minVals=autoNorm(datingDataMat)
	inArr=array([ffMiles,percentTats,iceCream])
	normInArr=(inArr-minVals)/ranges
	classifierResult=classify0(normInArr,normMat,datingLabels,3)
	print "You will probably like this person:",resultList[classifierResult-1]
# classifyPerson()	