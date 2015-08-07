from logRegres import *

def classifyVector(inX,weights):
	prob=sigmoid(sum(inX*weights))
	if prob>0.5:
		return 1.0
	else:return 0.0

def colicTest():
	frTrain=open('horseColicTraining.txt')
	frTest=open('horseColicTest.txt')
	trainingSet=[];trainingLabels=[]
	for line in frTrain.readlines():
		currLine=line.strip().split('\t')
		lineArr=[]
		for i in range(21):
			lineArr.append(float(currLine[i]))
		trainingSet.append(lineArr)
		trainingLabels.append(float(currLine[21]))
	trainWeight=stocGradAscent1(array(trainingSet),trainingLabels,500)
	erroCount=0.0;numTestVec=0.0
	for line in frTest.readlines():
		numTestVec+=1.0
		currLine=line.strip().split('\t')
		lineArr=[]
		for i in range(21):
			lineArr.append(float(currLine[i]))
		if int(classifyVector(array(lineArr),trainWeight))!=int(currLine[21]):
			erroCount+=1
	erroRate=float(erroCount)/numTestVec
	print 'the error rate is :',erroRate
	return erroRate

def multiTest():
	numTests=10;errorSum=0.0
	for k in range(numTests):
		errorSum+=colicTest()
	print 'after %d iterations the average erro rate is :%f'%(numTests,errorSum/float(numTests))

multiTest()


