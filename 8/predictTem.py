#encoding:utf-8
#predict the temperature
import loadDataExcel as lde;
import numpy as np;
import linRegres as lr;
import ridgeRegres as rr;
filepath = '../data/8/abalone-reduce.txt';#'../data/8/dalian1_weather1.xlsx';

#linear regress;
def linRegres():
	X,y = lr.loadData(filepath);
	m,n = np.shape(X);
	X = np.column_stack((np.ones((m,1)),X));
	return lr.compW(X,y);

#redge regres
def ridgeRegres(numIter = 10):
	#loadData
	X,y = lr.loadData(filepath);
	m,n = np.shape(X);
	errorMat = np.zeros((numIter,30));
	#共进行numIter次岭回归，选取误差最小的
	for i in range(numIter):
		X1 = X.copy();
		y1 = y.copy();
		np.random.shuffle(X1);
		np.random.shuffle(y1);
		xtrain = X1[0:int(m*0.9),:];
		ytrain = y1[0:int(m*0.9),:];
		xtest = X1[int(m*0.9):,:];
		ytest = y1[int(m*0.9):,:];
		#每次岭回归尝试30次lambda值，选取最小误差的w做为此次岭回归的得到的w
		wMat = rr.ridgeTest(xtrain,ytrain);
		#测试集正则化
		xmean = np.mean(xtrain,0);
		xvar = np.var(xtrain,0);
		ymean = np.mean(y,0);
		xtest = (xtest - xmean)/xvar
		ytest = ytest - ymean;
		ypredictMat = xtest*wMat.T;
		#记录本次循环下不同lambda值对应的误差
		for j in range(30):
			errorMat[i,j] = rr.squareError(ypredictMat[:,j],ytest);
	#找到平均误差最小的w
	meanError = np.mat(np.mean(errorMat,0));
	index = np.argmin(meanError,1)[0,0]; 
	#index = np.argsort(meanError,1)[0,0];
	bestw = wMat[index,:];
	#w还原以和线性回归的w进行比较
	meanX = np.mean(X,0);
	varX = np.var(X,0);
	meany = np.mean(y,0);
	unw = bestw/varX;
	const = -np.mat(meanX)*np.mat(unw).T+meany;
	return	 np.column_stack((const,unw)).T;
	
	

if __name__ =='__main__':
	print linRegres();
	print ridgeRegres();
	
	
