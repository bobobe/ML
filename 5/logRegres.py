#encoding:utf-8
#此文件用于逻辑回归的加载数据，训练数据，测试数据(以后改写成类)
from numpy import *;
def loadData(filepath):#加载数据(数据是txt格式存放)
	X = [];y = [];
	f = open(filepath);
	for line in f.readlines():
		lines = line.strip().split();
		row  = [1.0];
		row.extend([float(l) for l in lines[0:-2]])
		X.append(row);
			#X.append([1.0,float(lines[0]),float(lines[1])]);
		y.append([int(float(lines[-1]))]);
	return mat(X),mat(y);
		
def sigmoid(p):
	return 1.0/(1+exp(-p));


def grad(X,y):#梯度下降
	maxIter = 2000;
	alpha = 0.01;
	m,n = shape(X);
	w = zeros((n,1));
	for i in range(maxIter):
		w = w - alpha/m*X.T*(sigmoid(X*w)-y);
	return w;
	
def stocGrad(X,y):#随机梯度下降
	alpha = 0.01;
	m,n = shape(X);
	w = ones((n,1));
	for i in range(m):
		w = w-alpha*(sigmoid(X[i,:]*w)-y[i])[0,0]*(X[i,:]).T;
	return w;
	
def stocGrad1(X,y,num_iter):#随机梯度下降（改进）
	m,n = shape(X);
	w = ones((n,1));
	for i in range(num_iter):#more than 150	is better
		data = range(m);
		for j in range(m):
			alpha = 0.01/(1+i+j);#alpha是变化的
			index = random.randint(0,len(data));#随机选择样本
			w = w-alpha*(sigmoid(X[index,:]*w)-y[index])[0,0]*(X[index,:]).T;
			del(data[index]);
	return w;

def classify(X,w):#classify function
	y = sigmoid(X*w);
	return y>0.5;

def recallRate(ypredict,y):#compute the recall rate
	return float(sum(ypredict&y))/sum(y);
	
def preciseRate(ypredict,y):#compute the precise rate
	return float(sum(ypredict&y))/sum(ypredict);
	
def f1Rate(ypredict,y):#compute the F1 rate
	return 2*(recallRate(ypredict,y)*preciseRate(ypredict,y))/(recallRate(ypredict,y)+preciseRate(ypredict,y))
	
def errorRate(ypredict,y):#compute the error rate
	return float(sum(ypredict!=y))/len(y);

def multiTest(num,func = errorRate):#计算平均值，func默认是计算分类误差率的平均值
	X,y = loadData("/usr/local/py_workspace/data/5/horseColicTraining.txt");
	Xtest,ytest = loadData("/usr/local/py_workspace/data/5/horseColicTest.txt");
	sum = 0;
	for i in range(num):#循环计算num次，求平均值
		w = stocGrad1(X,y,150);
		ypredict = classify(Xtest,w);
		sum+=func(ypredict,ytest);
	return sum/num;
		
if __name__ =='__main__':#test
	X,y = loadData("/usr/local/py_workspace/data/5/horseColicTraining.txt");
	w = stocGrad1(X,y,150);
	Xtest,ytest = loadData("/usr/local/py_workspace/data/5/horseColicTest.txt");
	ypredict = classify(Xtest,w);
	print 'the recallrate is:%.2f' % recallRate(ypredict,ytest);
	print 'the preciserate is:%.2f' % preciseRate(ypredict,ytest);
	print 'the f1rate is:%.2f' % f1Rate(ypredict,ytest);
	print 'the errorrate is:%.2f' % errorRate(ypredict,ytest);
	
	print 'the mutiTestErrorRate is :%.2f' % multiTest(3);
		
