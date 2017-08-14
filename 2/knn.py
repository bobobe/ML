#encoding:utf-8
#k-nn algorithm
import numpy as np;
from scipy.stats import mode
import matplotlib.pyplot as plt;

def createData():#for test
	X = np.array([[1,2],[1,2.4],[2,1.8],[4,7],[4.5,8],[10,9],[11,8.7],[6,4],[5,4.7]]);
	y = np.array([[1,1,1,2,2,3,3,4,4]]);
	return np.mat(X),np.mat(y.T);
	
def loadData(filepath):
	X = [];
	y = [];
	fp= open(filepath);
	for line in fp.readlines():
		lines = line.strip().split('\t');
		xline = [];
		for num in lines[0:-1]:
			xline.append(float(num));
		X.append(xline);
		y.append([lines[-1]]);
	for i in range(len(y)):
		if y[i][0] == 'largeDoses':
			y[i][0] = 2;
		elif y[i][0] == 'smallDoses':
			y[i][0] = 1;
		elif y[i][0] == 'didntLike':
			y[i][0] = 0;
		else:
			print 'error';
			return ;
	X = np.mat(X);
	X,ranges,minVars= autoNorm(X);
	y = np.mat(y);
	return X,y,ranges,minVars;

def knn(X,y,testPoint,k):
	m,n = np.shape(X);
	dis = np.array([euclidean_dis(X[i],testPoint) for i in range(m)]);
	index = np.argsort(dis,0);
	y = y[index];
	k_cata = y[0:k];
	#计算众数
	return int(mode(k_cata,1)[0][0,0]);

def aveErrRate(X,y,num_iter,k):#average test errorRate
	m,n = np.shape(X);
	averErrRate= 0;
	for i in range(num_iter):
		#shuffle
		X1 = X.copy();
		y1 = y.copy();
		X1,y1 = autoShuffle(X1,y1);
		#test an train
		xtrain = X1[0:int(m*0.9),:];
		ytrain = y1[0:int(m*0.9),:];
		xtest = X1[int(m*0.9):,:];
		ytest = y1[int(m*0.9):,:];
		#predict and testerror
		a,b = np.shape(xtest);
		ypredict = np.zeros((a,1));
		for i in range(a):
			ypredict[i,:] = knn(xtrain,ytrain,xtest[i,:],k);
		averErrRate = averErrRate + errorRate(ypredict,ytest);
	return averErrRate/float(num_iter);
		
def errorRate(ypredict,y):
	m,n = np.shape(ypredict);
	return sum(ypredict!=y)/float(m);
	
def autoShuffle(X,y):
	m,n = np.shape(X);
	index = range(m);
	np.random.shuffle(index);
	X = X[index,:];
	y = y[index,:];
	return X,y; 

#compute euclidean_distance of x and y;
def euclidean_dis(x,y):
	return (x - y)*(x-y).T;
	
def autoNorm(X):
	maxVar = np.max(X,0);
	minVar = np.min(X,0);
	X = (X-minVar)/(maxVar-minVar);
	return X,maxVar - minVar,minVar;

def figure(X,y):
	fig = plt.figure();
	ax = fig.add_subplot(121);
	bx = fig.add_subplot(122);
	m,n = np.shape(X);
	x0 = X[:,0];
	x1 = X[:,1];
	x2 = X[:,2];
	'''a1 =[];
	a2 = [];
	b1 = [];
	b2= [];
	c1=[];
	c2=[];
	for i in range(m):
		if y[i][0] ==0:
			a1.append(X[i,1]);
			a2.append(X[i,2]);
		elif y[i][0] ==1:
			b1.append(X[i,1]);
			b2.append(X[i,2]);
		elif	y[i][0] ==2:
			c1.append(X[i,1]);
			c2.append(X[i,2]);
		else:
			print 'error'
			return ;'''
	ax.scatter(x1,x2,c= 15.0*np.asarray(y))#the third parm is color
	bx.scatter(x0,x1,c= 15.0*np.asarray(y))
	ax.set_xlabel('percent of playing games');
	ax.set_ylabel('ice stream every week');
	bx.set_xlabel('miles of flying every year');
	bx.set_ylabel('percent of playing games');
	
	plt.show();
	
if __name__ =='__main__':
	#test
	'''X,y =  createData();
	a = np.array([[10,8]]);
	print knn(X,y,a,3);'''
	#loadData
	X,y,ranges,minVars = loadData('../data/2/datingTestSet.txt');
	#figure
	'''figure(X,y);'''
	#errorRate
	'''print aveErrRate(X,y,5,1);'''
    #predict the kind of a man
	resultList = ['not at all','in small doses','in large doses'];
	percentTats = float(raw_input("percentage of time spent playing video games?"));
	ffMiles = float(raw_input("frequent flier miles earned per year?"));
	iceCream = float(raw_input("liters of ice cream consumed per year?"));
	testPoint = np.array([[ffMiles,percentTats,iceCream]]);
	print "you will probably like this person: %s" % resultList[knn(X,y,(testPoint-minVars)/ranges,4)];
    
