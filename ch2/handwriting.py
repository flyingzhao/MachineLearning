from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt
from os import listdir


def img2vector(filename):
	returnVect=zeros((1,1024))
	fr=open(filename)
	for i in range(32):
		lineStr=fr.readline()
		for j in range(32):
			returnVect[0,32*i+j]=int(lineStr[j])
	return returnVect
# mat=img2vector('/home/zhao/trainingDigits/0_0.txt')
# print mat[0,0:30]

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

def handwritingClassTest():
	hwLabels=[]
	trainingFileList=listdir('/home/zhao/trainingDigits/')
	m=len(trainingFileList)
	traingMat=zeros((m,1024))
	for i in range(m):
		fileNameStr=trainingFileList[i]
		fileStr=fileNameStr.split('.')[0]
		classNumStr=int(fileStr.split('_')[0])
		hwLabels.append(classNumStr)
		traingMat[i,:]=img2vector('/home/zhao/trainingDigits/'+fileNameStr)
	testFileList=listdir('/home/zhao/testDigits/')
	mTest=len(testFileList)
	errorCount=0.0
	for i in range(mTest):
		fileNameStr=testFileList[i]
		fileStr=fileNameStr.split('.')[0]
		classNumStr=int(fileStr.split('_')[0])
		vectorUnderTest=img2vector('/home/zhao/testDigits/'+fileNameStr)
		classfileResult=classify0(vectorUnderTest,traingMat,hwLabels,3)
		if classfileResult!=classNumStr:
			errorCount+=1.0
			print "the classifer come back with %d,the real answer is:%d"%(classfileResult,classNumStr)
	print "total number of error is %d"%errorCount
	print "error rate is %f"%(errorCount/float(mTest))
handwritingClassTest()
