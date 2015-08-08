from regression import *
abX,abY=loadDataSet('abalone.txt')
yHat1=lwlrTest(abX[0:99],abX[0:99],abY[0:99],0.1)
yHat2=lwlrTest(abX[0:99],abX[0:99],abY[0:99],1)
yHat3=lwlrTest(abX[0:99],abX[0:99],abY[0:99],10)

error1=rssError(abY[0:99],yHat1.T)
error2=rssError(abY[0:99],yHat2.T)
error3=rssError(abY[0:99],yHat2.T)

print error1,error2,error3

yHat1=lwlrTest(abX[100:199],abX[0:99],abY[0:99],0.1)
yHat2=lwlrTest(abX[100:199],abX[0:99],abY[0:99],1)
yHat3=lwlrTest(abX[100:199],abX[0:99],abY[0:99],10)

error1=rssError(abY[100:199],yHat1.T)
error2=rssError(abY[100:199],yHat2.T)
error3=rssError(abY[100:199],yHat2.T)

print error1,error2,error3

ws=standRegres(abX[0:99],abY[0:99])
yHat=mat(abX[100:199])*ws
error=rssError(abY[100:199],yHat.T.A)
print error