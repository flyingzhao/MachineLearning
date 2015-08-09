from regression import *

def scrapePage(inFile,outFile,yr,numPce,origPrc):
	from BeautifulSoup import BeautifulSoup
	fr = open(inFile); fw=open(outFile,'a') #a is append mode writing
	soup = BeautifulSoup(fr.read())
	i=1
	currentRow = soup.findAll('table', r="%d" % i)
	while(len(currentRow)!=0):
		currentRow = soup.findAll('table', r="%d" % i)
		title = currentRow[0].findAll('a')[1].text
		lwrTitle = title.lower()
		if (lwrTitle.find('new') > -1) or (lwrTitle.find('nisb') > -1):
			newFlag = 1.0
		else:
			newFlag = 0.0
		soldUnicde = currentRow[0].findAll('td')[3].findAll('span')
		if len(soldUnicde)==0:
			print "item #%d did not sell" % i
		else:
			soldPrice = currentRow[0].findAll('td')[4]
			priceStr = soldPrice.text
			priceStr = priceStr.replace('$','') #strips out $
			priceStr = priceStr.replace(',','') #strips out ,
			if len(soldPrice)>1:
              			priceStr = priceStr.replace('Free shipping', '') #strips out Free Shipping
              		print "%s\t%d\t%s" % (priceStr,newFlag,title)
              		fw.write("%d\t%d\t%d\t%f\t%s\n" % (yr,numPce,newFlag,origPrc,priceStr))
              	i += 1
		currentRow = soup.findAll('table', r="%d" % i)
	fw.close()
    
def setDataCollect():
	scrapePage('setHtml/lego8288.html','out.txt', 2006, 800, 49.99)
	scrapePage('setHtml/lego10030.html','out.txt', 2002, 3096, 269.99)
	scrapePage('setHtml/lego10179.html','out.txt', 2007, 5195, 499.99)
	scrapePage('setHtml/lego10181.html','out.txt', 2007, 3428, 199.99)
	scrapePage('setHtml/lego10189.html','out.txt', 2008, 5922, 299.99)
	scrapePage('setHtml/lego10196.html','out.txt', 2009, 3263, 249.99)

def crossValidation(xArr,yArr,numVal=10):
	m=len(yArr)
	indexList=range(m)
	errorMat=zeros((numVal,30))
	for i in range(numVal):
		trainX=[];trainY=[]
		testX=[];testY=[]
		random.shuffle(indexList)
		for j in range(m):
			if j<m*0.9:
				trainX.append(xArr[indexList[j]])
				trainY.append(yArr[indexList[j]])
			else:
				testX.append(xArr[indexList[j]])
				testY.append(yArr[indexList[j]])
		wMat=ridgeTest(trainX,trainY)
		print wMat
		for k in range(30):
			matTestX=mat(testX);matTrainX=mat(trainX)
			meanTrain=mean(matTrainX,0)
			varTrain=var(matTrainX,0)
			matTestX=(matTestX-meanTrain)/varTrain
			yEst=matTestX*mat(wMat[k,:]).T+mean(trainY)
			errorMat[i,k]=rssError(yEst.T.A,array(testY))
	meanErrors=mean(errorMat,0)
	minMean=float(min(meanErrors))
	bestWeights=wMat[nonzero(meanErrors==minMean)]
	print bestWeights
	xMat=mat(xArr);yMat=mat(yArr).T
	meanX=mean(xMat,0);varX=var(xMat,0)
	unReg=bestWeights/varX
	print "the best model from ridge regression is:\n",unReg
	print "with constant term:",-1*sum(multiply(meanX,unReg))+mean(yMat)

# setDataCollect()
data,label=loadDataSet('out.txt')
crossValidation(data,label)
ridgeWeights=ridgeTest(data,label)
# print ridgeWeights