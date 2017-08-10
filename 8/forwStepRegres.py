#encoding:utf-8
#前向逐步回归
from numpy import *;
import linRegres as lr;
import matplotlib.pyplot as plt;
import ridgeRegres as rr;

def stageWise(X,y,eps = 0.01,numIter = 100):
	ymean = mean(y,0);
	y = y -ymean;
	xmean = mean(X,0);
	xvar = var(X,0);
	X = (X-xmean)/xvar;
	m,n = shape(X);
	BestW = zeros((n,1));
	BestWMat = zeros((numIter,n));
	for i in range(numIter):
		lowestError = inf;#正无穷
		#print BestW.T;
		for j  in range(n):
			curW = BestW.copy();
			for k in [-1,1]:
				curWCopy = curW.copy();
				curWCopy[j] = curWCopy[j]+k*eps;
				ypredict = X * curWCopy; 
				if rr.squareError(ypredict,y)<lowestError:
					lowestError = rr.squareError(ypredict,y);
					BestW = curWCopy.copy();
		BestWMat[i,:] = BestW.copy().T;
	return BestWMat;

if __name__ =='__main__':
	X,y = lr.loadData('/usr/local/py_workspace/machine-learning/data/8/abalone.txt');
	result = stageWise(X,y,0.005,1000);
	#graphy with 1000 iterator
	fig = plt.figure();
	ax = fig.add_subplot(111);
	ax.plot(result);
	plt.show();
	
	
