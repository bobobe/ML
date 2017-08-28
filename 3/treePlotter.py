#encoding:utf-8
#决策树
import numpy as np;
import matplotlib.pyplot as plt;
from dTree import *;
import treeGlobal as tplot;

#设置字体以显示中文
def conf_zh(font_name):
    from pylab import mpl
    mpl.rcParams['font.sans-serif'] = [font_name]
    mpl.rcParams['axes.unicode_minus'] = False

def plotNode(nodeTxt,centerPt,parentPt,nodeType):#画一个树枝+节点
	tplot.ax.annotate(nodeTxt,xy = parentPt,xycoords = 'axes fraction',\
	xytext = centerPt,textcoords = 'axes fraction',va = 'center',ha = 'center',bbox=nodeType,\
	arrowprops = tplot.arrow_args);

def plotMidText(cntrPt,parentPt,txtString):#树枝中间的文字
	xMid = (parentPt[0]+cntrPt[0])/2.0;
	yMid = (parentPt[1]+cntrPt[1])/2.0;
	tplot.ax.text(xMid,yMid,txtString);

def plotTree(myTree,parentPt,nodeTxt):#递归画整颗树
	numLeafs = getNumLeafs(myTree);
	depth = getTreeDepth(myTree);
	firstStr = myTree.keys()[0];
	cntrPt = (tplot.x0ff+(1.0+float(numLeafs))/2.0/tplot.totalW,tplot.y0ff);
	plotMidText(cntrPt,parentPt,nodeTxt);
	plotNode(firstStr,cntrPt,parentPt,tplot.decisionNode);
	secondDict = myTree[firstStr];
	tplot.y0ff = tplot.y0ff - 1.0/tplot.totalD;
	for key in secondDict.keys():
		if type(secondDict[key]) == dict:
			plotTree(secondDict[key],cntrPt,str(key));
		else:
			tplot.x0ff = tplot.x0ff+1.0/tplot.totalW;
			plotNode(secondDict[key],(tplot.x0ff,tplot.y0ff),cntrPt,tplot.leafNode);
			plotMidText((tplot.x0ff,tplot.y0ff),cntrPt,str(key));
	tplot.y0ff = tplot.y0ff +1.0/tplot.totalD;

def treePlotter(inTree):
	fig = plt.figure(facecolor ='white');#画板背景色
	fig.clf();#清除当前图像窗口
	tplot.ax= plt.subplot(111,frameon = False);#
	tplot.totalD = float(getTreeDepth(inTree));
	tplot.totalW = float(getNumLeafs(inTree));
	tplot.x0ff = -0.5/tplot.totalW;
	tplot.y0ff = 1.0;
	plotTree(inTree,(0.5,1.0),' ');
	'''plotNode(U'决策节点',(0.5,0.1),(0.1,0.5),tplot.decisionNode);
	plotNode(U'叶节点',(0.8,0.1),(0.3,0.8),tplot.leafNode);'''
	plt.show();
	
if __name__=='__main__':
	conf_zh('Droid Sans Fallback');#解决绘制时界面的中文显示问题
	#test create decideTree
	X = np.array([[1,1],[1,1],[1,0],[0,1],[0,1]]);
	y = np.array([[1],[1],[0],[0],[0]]);
	labels = ['no sur','flip'];
	t = createTree(X,y,labels);
	print t;
	'''X = np.array([[1,2,3],[1,1,2],[1,3,1],[2,1,1],[2,2,1]]);
	y = np.array([[1],[0],[0],[0],[1]]);
	labels = ['no sur','flip','test'];
	t = createTree(X,y,labels);
	print t;'''
	#test plot decideTree
	treePlotter(t);

