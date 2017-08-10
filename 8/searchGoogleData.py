#encoding:utf-8
#can't use
#获取google api提供的数据
from time import sleep;
import json;
import urllib2;
def searchForSet(setNum):
	sleep(10);#防止频率过快
	myAPIstr = 'get from code.google.com';
	searchURL = 'http://www.googleapis.com/shopping/search/v1/public/products?\
	key=%s&country=US&q=lego+%d&alt=json' % (myAPIstr,setNum);
	pg = urllib2.urlopen(searchURL);
	retDict = json.loads(pg.read());
	print retDict;
	
	
if __name__ =='__main__':
	searchForSet(8288);
	
