#encoding:utf-8
#岭回归
from numpy import *;
import linRegres as lr;
import matplotlib.pyplot as plt;
def ridgeRegres(X,y,lamda):
	#normalization
	ymean = mean(y,0);
	y = y-ymean;
	xmean = mean(X,0);
	xvar = var(X,0);
	X = (X-xmean)/xvar;
	#compute the gradient:
	m,n = shape(X);
	w = ones((n,1));
	I = eye(n);
	if(linalg.det(X.T*X+lamda*I)==0):
		print 'error,the det ==0!';
		return ;
	w = (X.T*X+lamda*I).I*X.T*y;
	return w;

def squareError(ypredict,y):
	m,n = shape(y);
	return (ypredict - y).T*(ypredict - y)/m;
	
def ridgeTest(X,y):
	m,n = shape(X);
	numTest = 30;#total 30 different lambda
	wMat = zeros((numTest,n));
	for i  in range(numTest):
		wMat[i,:] = (ridgeRegres(X,y,exp(i-10))).T;#尝试不同的lambda
	return wMat;
	
if __name__ =='__main__':
	X,y = lr.loadData('/usr/local/py_workspace/machine-learning/data/8/abalone.txt');
	wMat = ridgeTest(X[0:99],y[0:99]);
	#cross validation
	croX = X[100:199];
	croY = y[100:199];
	sqError = croX*wMat.T;
	for i in range (30):
		error = squareError(sqError[:,i],croY);
		print error;#find the lambda with the  minmum square error
	#graphy with different lambda
	fig = plt.figure();
	ax = fig.add_subplot(111);
	ax.plot(wMat);
	plt.show();
	
	
	
	
