#encoding:utf-8
#手写识别
import numpy as np;
from os import listdir;
import knn as kn;

def img2vector(filepath):#load 32*32-binary img file and tansfer to 1*1024 vector
	l = [];
	fp = open(filepath);
	for i in range(32):
		for j in fp.readline().strip():
			l.append(int(j));
	return l;#1*1024 list

def loadData(dirpath):
	X = [];
	y = [];
	filelist = listdir(dirpath);
	#print filelist;
	for files in filelist:
		X.append(img2vector(dirpath+files));
		y.append(int(files[0]));
	return np.mat(X),np.mat(y).T
		
def hw_Classify(X,y,testImgVector,k):
	return kn.knn(X,y,testImgVector,k);

def errorRate(ypredict ,y):
	m,n = np.shape(y);
	return sum(ypredict!=y)/float(m);
		
	
if __name__=='__main__':
	trainingdirpath = '../data/2/trainingDigits/';
	testdirpath = '../data/2/testDigits/';
	X,y = loadData(trainingdirpath);
	#test
	'''testImgVector = np.mat(img2vector(testdirpath+'6_12.txt'));
	print "predict is %d" % hw_Classify(X,y,testImgVector,3);'''
	#errorRate
	Xtest,ytest = loadData(testdirpath) ;
	m,n = np.shape(Xtest);
	ypredict =np.zeros((m,1));
	for i in range(m):
		ypredict[i] = hw_Classify(X,y,Xtest[i,:],3);
	print 'the errorRate is %.2lf'% errorRate(ypredict,ytest);
	
