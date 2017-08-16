#encoding:utf-8
#决策树
import numpy as np;
from scipy.stats import mode;
import matplotlib.pyplot as plt;

#设置字体以显示中文
def conf_zh(font_name):
    from pylab import mpl
    mpl.rcParams['font.sans-serif'] = [font_name]
    mpl.rcParams['axes.unicode_minus'] = False

#树节点格式的全局变量
decisionNode = dict(boxstyle = "sawtooth",fc="0.8");
leafNode = dict(boxstyle = "round4",fc = "0.8");
arrow_args = dict(arrowstyle = "<-");
	
def calcEntro(y):#compute the entropy
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
	
def plotNode(nodeTxt,centerPt,parentPt,nodeType,ax):
	ax.annotate(nodeTxt,xy = parentPt,xycoords = 'axes fraction',\
	xytext = centerPt,textcoords = 'axes fraction',va = 'center',ha = 'center',bbox=nodeType,\
	arrowprops = arrow_args);
	
	
def treePlotter():
	fig = plt.figure(facecolor ='white');#画板背景色
	fig.clf();#清除当前图像窗口
	ax= plt.subplot(111,frameon = False);#
	plotNode(U'决策节点',(0.5,0.1),(0.1,0.5),decisionNode,ax);
	plotNode(U'叶节点',(0.8,0.1),(0.3,0.8),leafNode,ax);
	plt.show();

	
if __name__=='__main__':
	conf_zh('Droid Sans Fallback');#
	#test create decideTree
	'''X = np.array([[1,1],[1,1],[1,0],[0,1],[0,1]]);
	y = np.array([[1],[1],[0],[0],[0]]);
	labels = ['no sur','flip'];
	print createTree(X,y,labels);'''
	#test plot decideTree
	treePlotter();
