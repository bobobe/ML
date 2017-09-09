#encoding:utf-8
def loadData():
	postingList = [['my','dog','has','flea','problems','help','please'],\
	['maybe','not','take','him','to','dog','park','stupid'],\
	['my','dalmation','is','so','cute','I','love','him'],\
	['stop','posting','stupid','worthless','garbage'],\
	['mr','licks','ate','my','steak','how','to','stop','him'],\
	['quit','buying','worthless','dog','food','stupid']];
	classVec = [0,1,0,1,0,1];
	
	return postingList,classVec;

#得到包含在所有文档中的不重复词的列表
def createVocabList(dataSet):
	vocabSet = set();
	for document in dataSet:
		vocabSet = vocabSet|set(document);
	return list(vocabSet);

#将文档转化为向量
def wordsToVec(vocabList,inputSet):
	returnVec = [0]*len(vocabList);
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)] = 1;
		else:
			print "the word: %s is not in my vocabulary!" % word;
	return returnVec;

def trainNB0(trainListX,y):
	
	
if __name__ =="__main__":
	#test
	listOPosts,listClasses = loadData();
	myVocabList = createVocabList(listOPosts);
	print myVocabList;
	print wordsToVec(myVocabList,listOPosts[0]);
	
	

