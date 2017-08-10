#encoding:utf-8
#从excel表中导数据出
from xlrd import *;
from numpy import *;
def loadData(filepath):
	data = open_workbook(filepath);
	table = data.sheet_by_name(u'Sheet1');
	row = table.nrows;
	col = table.ncols;
	X = [];
	y = [];
	for i in range(row):
		X.append(table.row_values(i));
		y.append(table.row_values(i)[-1]);
	X = mat(X);
	X = X[:,0:-1];
	y = mat(y).T;
	return X,y;

if __name__=='__main__':
    loadData('../data/8/dalian1_weather1.xlsx');
