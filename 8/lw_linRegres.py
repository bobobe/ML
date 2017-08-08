#encoding:utf-8
#局部加权线性回归
from numpy import *;
import matplotlib.pyplot as p;
import linRegres as lr;
def lwlr(testpoint,X,y,k=1.0):#预测单样本点testpoint的值
		m,n = shape(X);
		wt = eye(m);
		for j in range(m):
			diff = testpoint-X[j,:];
			wt[j,j] = exp(-diff*diff.T/(2*k**2));#取对角线为权重便于计算
		w = ones((n,1));
		if(linalg.det(X.T*wt*X)==0.0):
			print 'error,the det =0';
			return ;
		w = (X.T*wt*X).I*X.T*wt*y;
		return testpoint*w;#预测

def multi_lwlr(multiTest,X,y,k=1.0):#预测一组测试样本
	m,n = shape(multiTest);
	ypredict = zeros((m,1));
	for i in range(m):
		ypredict[i] = lwlr(multiTest[i,:],X,y,k);
	return ypredict;

def figure(X,y,ypredict):
	x = X[:,1];
	fig = p.figure();
	ax = fig.add_subplot(111);
	index = argsort(x,0); #排序
	x =x[index][:,0];
	ypredict = ypredict[index][:,0];
	y = y[index][:,0];
	ax.plot(x,ypredict);#把点用线连起来
	ax.scatter(x,y,c = 'red',s = 10);#散点图
	ax.scatter(x,ypredict,c = 'black',s = 10);
	p.show();
	
if __name__ == '__main__':
			X,y = lr.loadData('/usr/local/py_workspace/machine-learning/data/8/ex0.txt');
			ypredict = multi_lwlr(X,X,y,0.03);#改变k的大小观察拟合程度，选取最佳的k
			figure(X,y,ypredict);
