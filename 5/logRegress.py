#a test
import scipy.io as sio;
from numpy import *;
def loadData(filename):
	data =  sio.loadmat(filename);#数据是mat格式存放
	X = data['X'];
	row,col = shape(X);
	for i in range(row):
		for j in range(col):
			X[i][j] = float(X[i][j]);
	one= ones((row,1));
	X = column_stack((one,X));
	y = data['Y'];
	for i in range(len(y)):
		y[i] = float(y[i]);
	return mat(X),mat(y);

def sigmoid(n):
	return 1.0/(1+exp(-n));
	
def grad(X,y):
	row,col = shape(X);
	w = zeros((col,1));
	maxCyc = 500;
	alpha = 0.001;
	for i in range(maxCyc):
		j = 1.0/row*(X.T*(sigmoid(X*w)-y));
		w = w-alpha*j;
	return w;
