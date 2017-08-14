#encoding:utf-8
#决策树
import numpy as np;

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
	
def splitDataSet(X,index,value):#提取第index维等于value的样本,并去掉第index维
	newFeature = [];
	for row in X:
		if(row[index]==value):
			reduceFeature = list(row[:index]);
			reduceFeature.extend(row[index+1:]);
			newFeature.append(reduceFeature);
	return np.array(newFeature);

if __name__=='__main__':
	X = np.array([[1,2],[3,1],[3,2],[5,2],[3,1],[3,2],[1,3],[3,2],[4,1]]);
	print splitDataSet(X,0,1);
	
