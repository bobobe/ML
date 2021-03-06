#encoding:utf-8
#决策树
import numpy as np;
from scipy.stats import mode;
import matplotlib.pyplot as plt;
import pickle as pl;

#设置字体以显示中文
def conf_zh(font_name):
    from pylab import mpl
    mpl.rcParams['font.sans-serif'] = [font_name]
    mpl.rcParams['axes.unicode_minus'] = False

#compute the entropy
def calcEntro(y):
	m,n = np.shape(y);
	typeDic = {};
	for i in range(m):
		if y[i,:][0] not in typeDic.keys():
			typeDic[y[i,:][0]] = 1;
		else:
			typeDic[y[i,:][0]]+=1;
	entropy = 0;
	for v in typeDic.values():
		p = v/float(m);
		entropy += (p*np.log2(p));
	entropy = -entropy;
	return entropy;
	
def splitDataSet(X,y,index,value):#提取第index维等于value的样本,并去掉第index维
	newFeatureX = [];
	newFeatureY = [];
	m,n = np.shape(X);
	i = 0;
	for i in range(m):
		if(X[i,index]==value):
			reduceFeature = list(X[i,:index]);
			reduceFeature.extend(list(X[i,index+1:]));
			newFeatureX.append(reduceFeature);
			newFeatureY.append(y[i]);
		i+=1;
	return np.array(newFeatureX),np.array(newFeatureY);
	
def chooseBestFeatureToSplit(X,y):#选择信息增益最大的特征来分割,返回该特征的下标
	m,n = np.shape(X);
	if(n==1):#if n == 1,express that X only one feature, so the only choose is 0;
		return 0;
	Hy = calcEntro(y);
	#print 'the total entropy is %lf'% Hy;
	maxInfoIncre = 0;
	bestFeature = -1;
	for i in range(n):
		featureSet = set([ithFeature for ithFeature in X[:,i]]);
		Hyx = 0;
		for j in featureSet:
			xsplit,ysplit = splitDataSet(X,y,i,j);
			m1,n1 = np.shape(xsplit);
			p = m1/float(m);
			Hyx+=p*calcEntro(ysplit);
		#print 'the %dth feature infoIncrease is %lf' %(i,Hy-Hyx);
		if Hy - Hyx >maxInfoIncre:
			maxInfoIncre = Hy-Hyx;
			bestFeature = i;
	return bestFeature;
	
def majorityCnt(y):#多数表决
	return int(mode(y,0)[0]);
		
def createTree(X,y,labels):#create the dicide tree(labels is the description of the feature,it is a list)
	m1,n1 = np.shape(X);
	m2,n2 = np.shape(y);
	if list(y).count(y[0]) == m2:
		return y[0][0]; 
	if n1==0:
		return majorityCnt(y);
	splitIndex = chooseBestFeatureToSplit(X,y);
	splitFeature = labels[splitIndex];
	myTree = {splitFeature:{}};
	del(labels[splitIndex]);
	featureSet = set([splitValue for splitValue in X[:,splitIndex]]);
	for v in featureSet:
		subLabels = labels[:];
		splitX,splitY = splitDataSet(X,y,splitIndex,v);
		myTree[splitFeature][v] = createTree(splitX,splitY,subLabels);
	return myTree;
	
def getNumLeafs(myTree):#获取树的叶子节点数目(非递归)
	leafNum = 0;
	nodeList = [];
	nodeList.append(myTree.values()[0]);
	while(len(nodeList)!=0):#层序遍历
		nodeValue = nodeList[0];
		del nodeList[0];
		for nValue in nodeValue.values():
			#print type(nValue);
			if(type(nValue) != dict):
				leafNum += 1;
			else:
				nodeList.append(nValue);
	return leafNum;
	
def getTreeDepth(myTree):#获取树的深度-1(递归)
	maxDep = 0;
	thisDict = myTree.values()[0];
	for nValue in thisDict.values():
		if(type(nValue)==dict):
			thisDep = getTreeDepth(nValue)+1;
		else:
			thisDep = 1;
		if thisDep>maxDep:
			maxDep = thisDep;
	return maxDep;

#分类
def classify(inputTree,labels,testPt):
	thisLabel = inputTree.keys()[0];
	thisDict = inputTree[thisLabel];
	thisValue = testPt[labels.index(thisLabel)];
	if type(thisDict[thisValue])==dict:
		return classify(thisDict[thisValue],labels,testPt);
	else:
		return str(thisDict[thisValue]);

#序列化后存储树
def storeTree(inputTree,filename):
	f = open(filename,'w');
	pl.dump(inputTree,f);
	f.close();

#从文件读取得到树
def getTree(filename):
	f = open(filename);
	return pl.load(f);

	
if __name__=='__main__':
	#test create decideTree
	X = np.array([[1,1],[1,1],[1,0],[0,1],[0,1]]);
	y = np.array([[1],[1],[0],[0],[0]]);
	labels = ['no sur','flip'];
	t = createTree(X,y,labels);
	#store Tree
	storeTree(t,'tree.txt');
	t = getTree('tree.txt');
	print t;
	'''X = np.array([[1,2,3],[1,1,2],[1,3,1],[2,1,1],[2,2,1]]);
	y = np.array([[1],[0],[0],[0],[1]]);
	labels = ['no sur','flip','test'];
	t = createTree(X,y,labels);
	print t;'''
	#depth
	print 'the deepth of the dtree is: '+str(getTreeDepth(t));
	#leafNum
	print 'the leaf number of the dtree is: '+str(getNumLeafs(t));
	#classfiy
	testPt = [1,0];
	labels = ['no sur','flip'];
	print 'the class of the testPt is: '+classify(t,labels,testPt);
	
