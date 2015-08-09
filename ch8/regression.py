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

def ridgeRegres(xMat,yMat,lam=0.2):
	# xMat=mat(xArr);yMat=mat(yArr).T
	xTx=xMat.T*xMat
	denom=xTx+eye(shape(xMat)[1])*lam
	if linalg.det(denom)==0:
		print "The matrix can not inverse"
		return
	ws=denom.I*(xMat.T*yMat)
	return ws

def ridgeTest(xArr,yArr):
	xMat=mat(xArr);yMat=mat(yArr).T
	yMean=mean(yMat,0)
	yMat=yMat-yMean
	xMeans=mean(xMat,0)
	xVar=var(xMat,0)
	xMat=(xMat-xMeans)/xVar
	numTestPts=30
	wMat=zeros((numTestPts,shape(xMat)[1]))
	for i in range(numTestPts):
		ws=ridgeRegres(xMat,yMat,exp(i-10))
		wMat[i,:]=ws.T
	return wMat

def stageWise(xArr,yArr,eps=0.01,numIt=100):
	xMat=mat(xArr);yMat=mat(yArr).T
	yMean=mean(yMat,0)
	yMat=yMat-yMean
	#xMat=regularize(xMat)
	xMeans=mean(xMat,0)
	xVar=var(xMat,0)
	xMat=(xMat-xMeans)/xVar
	m,n=shape(xMat)
	returnMat=zeros((numIt,n))
	ws=zeros((n,1));wsTest=ws.copy();wsMax=ws.copy
	for i in range(numIt):
		print ws.T
		lowestError=inf
		for j in range(n):
			for sign in [-1,1]:
				wsTest=ws.copy()
				wsTest[j]+=eps*sign
				yTest=xMat*wsTest
				rssE=rssError(yMat.A,yTest.A)
				# print rssE,lowestError,wsTest.T
				if rssE<lowestError:
					lowestError=rssE
					wsMax=wsTest
				# print wsMax.T
		ws=wsMax.copy()
		returnMat[i,:]=ws.T
	return returnMat


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

##ridge regression 
# data,label=loadDataSet('abalone.txt')
# ridgeWeights=ridgeTest(data,label)
# print ridgeWeights
# fig=plt.figure()
# ax=fig.add_subplot(111)
# ax.plot(ridgeWeights)
# plt.show()

##stagewise
# data,label=loadDataSet('abalone.txt')
# a=stageWise(data,label,0.001,5000)
# fig=plt.figure()
# ax=fig.add_subplot(111)
# ax.plot(a)
# plt.show()

# xMat=mat(data);yMat=mat(label).T
# yMean=mean(yMat,0)
# yMat=yMat-yMean
# xMeans=mean(xMat,0)
# xVar=var(xMat,0)
# xMat=(xMat-xMeans)/xVar
# weights=standRegres(xMat,yMat.T)
# print weights