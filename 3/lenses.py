#encoding:utf-8
import dTree as dt;
import treePlotter as tp;
import numpy as np;
def loadData(filename):
	f = open(filename);
	X = [];
	y = [];
	for line in f.readlines():
		lines = line.strip().split('\t');
		y.append([lines[-1]]);
		del lines[-1];
		X.append(lines);
	return np.array(X),np.array(y);

if __name__ =='__main__':
	lensesLabels = ['age','prescript','astigmatic','tearRate'];
	X,y = loadData('lenses.txt');
	print X;
	print y;
	t = dt.createTree(X,y,lensesLabels);
	print t;
	tp.treePlotter(t);
	
	
