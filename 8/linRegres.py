 # encoding: utf-8
from numpy import *;
import matplotlib.pyplot as p;

def loadData(filename):
	X = [];y = [];
	with open(filename) as f:
		aNum = f.readlines();
		for line in aNum:
			L = [];
			L = line.strip().split('\t');
			for i in range(len(L)):
				L[i] = float(L[i]);
			y.append(L[-1]);
			del L[-1];
			X.append(L);
	return mat(X),mat(y).T;

def  compW(X,y):
	""" Function doc """
	if linalg.det(X.T*X)  == 0.0:
		print("It is a mistakes!");
		return;
	return (X.T*X).I*X.T*y;
	
def figure(X,y,w):#三个参数，数据集，结果集，权重
	fig = p.figure();
	ax = fig.add_subplot(111);
	ax.scatter(X[:,1],y);#散点图
	ax.plot(X[:,1],X*w);#拟合直线
	p.show();

def corrc(X,y,w):#计算预测值和真实值的相关系数
	return corrcoef((X*w).T,y.T);#两个参数必须是行向量
	
if __name__ == '__main__':
	X,y = loadData('/usr/local/py_workspace/machine-learning/data/8/ex0.txt');
	w = compW(X,y);
	print '真实值和预测值的相关系数为:',corrc(X,y,w);
	figure(X,y,w);

	
