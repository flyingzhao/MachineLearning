from numpy import *

def loadDataSet():
	postingList=[['my','dog','has','flea','problem','help','please'],
	['maybe','not','take','him','to','dog','park','stupid'],
	['my','dalmation','is','so','cute','I','love','him'],
	['stop','posting','stupid','worthless','garbage'],
	['mr','licks','ate','my','steak','how','to','stop','him'],
	['quit','buying','worthless','dog','food','stupid']]
	classVec=[0,1,0,1,0,1]
	return postingList,classVec

def createVocabList(dataSet):
	vocabSet=set([])
	for document in dataSet:
		vocabSet=vocabSet|set(document)
	return list(vocabSet)

def setOfWords2Vec(vocabList,inputSet):
	returnVec=[0]*len(vocabList)
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)]=1
		else:print "the word: %s is not in my vocabulary!"%word
	return returnVec


def bagOfWords2Vec(vocabList,inputSet):
	returnVec=[0]*len(vocabList)
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)]+=1
		# else:print "the word: %s is not in my vocabulary!"%word
	return returnVec

def trainNB0(trainMatrix,trainCategory):
	numTrainDocs=len(trainMatrix)
	numWords=len(trainMatrix[0])
	pAbusive=sum(trainCategory)/float(numTrainDocs)
	p0Num=ones(numWords);p1Num=ones(numWords)
	p0Denom=2.0;p1Denom=2.0
	for i in range(numTrainDocs):
		if trainCategory[i]==1:
			p1Num+=trainMatrix[i]
			p1Denom+=sum(trainMatrix[i])
		else:
			p0Num+=trainMatrix[i]
			p0Denom+=sum(trainMatrix[i])
	p1Vect=log(p1Num/p1Denom)
	p0Vect=log(p0Num/p0Denom)
	# p1Vect=p1Num/p1Denom
	# p0Vect=p0Num/p0Denom
	return p0Vect,p1Vect,pAbusive

def classifyNB(vec2Classify,p0Vec,p1Vec,pClass1):
	p1=sum(vec2Classify*p1Vec)+log(pClass1)
	p0=sum(vec2Classify*p0Vec)+log(1.0-pClass1)
	if p1>p0:
		return 1
	else:
		return 0

def testingNB():
	listPosts,listClass=loadDataSet()
	myVoacbList=createVocabList(listPosts)
	trainMat=[]
	for postinDoc in listPosts:
		trainMat.append(setOfWords2Vec(myVoacbList,postinDoc))
	p0v,p1v,pAb=trainNB0(trainMat,listClass)
	testEntry=['love','my','dalmation']
	print setOfWords2Vec(myVoacbList,testEntry)
	thisDoc=array(setOfWords2Vec(myVoacbList,testEntry))
	print thisDoc
	print testEntry,'classified as:',classifyNB(thisDoc,p0v,p1v,pAb)
	testEntry=['stupid','garbage']
	thisDoc=array(setOfWords2Vec(myVoacbList,testEntry))
	print testEntry,'classified as:',classifyNB(thisDoc,p0v,p1v,pAb)




# listPosts,listClass=loadDataSet()
# print listPosts,listClass
# myVoacbList=createVocabList(listPosts)
# print myVoacbList
# print listPosts[0]
# print setOfWords2Vec(myVoacbList,listPosts[0])
# print vec


# listPosts,listClass=loadDataSet()
# myVoacbList=createVocabList(listPosts)
# print myVoacbList
# trainMat=[]
# for postinDoc in listPosts:
# 	trainMat.append(setOfWords2Vec(myVoacbList,postinDoc))
# print trainMat
# print listClass
# p0v,p1v,pAb=trainNB0(trainMat,listClass)
# print p0v
# print p1v
# print pAb
# testingNB()