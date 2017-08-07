#分类可视化（点，决策边界）
#encoding:utf-8
import matplotlib.pyplot as plt;
import logRegres as lr;
from numpy import *;
def plotBestFit():
	fig = plt.figure();
	ax = fig.add_subplot(111);
	X,y = lr.loadData();
	#w = lr.grad(X,y);
	#w = lr.stocGrad(X,y);
	w = lr.stocGrad1(X,y);
	x1 =[];
	y1 =[];
	x0 =[];
	y0 =[];
	for i in range(shape(X)[0]):
		if(y[i]== 1):
			x1.append(X[i,1]);
			y1.append(X[i,2]);
		else:
			x0.append(X[i,1]);
			y0.append(X[i,2]);
			
	ax.scatter(x1,y1,c = 'red',marker = "s");
	ax.scatter(x0,y0,c = 'black',marker = "o");
	plt.xlabel('x1');plt.ylabel('x2');
	
	x3 = arange(-4,4,1);
	w = w.getA();#w[0]返回的还是一个矩阵，必须先转化为数组，才能返回一个数
	y3 = (-w[0]-w[1]*x3)/w[2];
	ax.plot(x3,y3);
	plt.show();
