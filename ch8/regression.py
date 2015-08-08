from numpy import *
import matplotlib.pyplot as plt


def loadDataSet(filename):
	numFeat=len(open(filename).readline().split('\t'))-1
	dataMat=[];labelMat=[]
	fr=open(filename)
	for line in fr.readlines():
		lineArr=[]
		curLine=line.strip().split('\t')
		for i in range(numFeat):
			lineArr.append(float(curLine[i]))
		dataMat.append(lineArr)
		labelMat.append(float(curLine[-1]))
	return dataMat,labelMat

def standRegres(xArr,yArr):
	xMat=mat(xArr);yMat=mat(yArr).T
	xTx=xMat.T*xMat
	if linalg.det(xTx)==0:
		print "The matrix can not inverse"
		return
	ws=xTx.I*(xMat.T*yMat)
	return ws

def drawGrahp(xArr,yArr,ws):
	xMat=mat(xArr);yMat=mat(yArr)
	fig=plt.figure()
	ax=fig.add_subplot(111)
	ax.scatter(xMat[:,1].flatten().A[0],yMat.T[:,0].flatten().A[0])
	xCopy=xMat.copy()
	xCopy.sort(0)
	yHat=xCopy*ws
	ax.plot(xCopy[:,1],yHat)
	plt.show()

def lwlr(testPoint,xArr,yArr,k=1.0):
	xMat=mat(xArr);yMat=mat(yArr).T
	m=shape(xMat)[0]
	weights=mat(eye((m)))
	for j in range(m):
		diffMat=testPoint-xMat[j,:]
		weights[j,j]=exp(diffMat*diffMat.T/(-2.0*k**2))
	xTx=xMat.T*(weights*xMat)
	if linalg.det(xTx)==0:
		print "The matrix can not inverse"
		return
	ws=xTx.I*(xMat.T*(weights*yMat))
	return testPoint*ws

def lwlrTest(testArr,xArr,yArr,k=1.0):
	m=shape(testArr)[0]
	yHat=zeros(m)
	for i in range(m):
		yHat[i]=lwlr(testArr[i],xArr,yArr,k)
	return yHat

def drawLwlr(xArr,yArr,yHat):
	xMat=mat(xArr);yMat=mat(yArr)
	sortInd=xMat[:,1].argsort(0)
	xSort=xMat[sortInd][:,0,:]
	fig=plt.figure()
	ax=fig.add_subplot(111)
	ax.scatter(xMat[:,1].flatten().A[0],yMat.T[:,0].flatten().A[0],s=2)
	xCopy=xMat.copy()
	xCopy.sort(0)
	ax.plot(xCopy[:,1],yHat[sortInd],c='red')
	plt.show()

def rssError(yArr,yHatArr):
	return ((yArr-yHatArr)**2).sum()

##logistic regression
# data,label=loadDataSet('ex0.txt')
# print data
# print label
# ws=standRegres(data,label)
# print ws
# drawGrahp(data,label,ws)
# yHat=data*ws
# print corrcoef(yHat.T,label)


##locally weighted linear regression
# data,label=loadDataSet('ex0.txt')
# y=lwlr(data[0],data,label)

# yHat=lwlrTest(data,data,label,0.01)

# drawLwlr(data,label,yHat)