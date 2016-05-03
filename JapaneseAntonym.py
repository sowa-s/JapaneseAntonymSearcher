#coding:utf-8
import csv
import pickle

class JapaneseAntonym:
	def __init__(self,dumpfileName="antonym.dump"):
		self.antonyDic = pickle.load(open(dumpfileName))
	def getAntonym(self,word):
		if word in self.antonyDic:
			return self.antonyDic[word]
		return []

class AntonymDicMaker:
	def __init__(self,filename='antonym.csv'):
		self.file = open(filename,'r')
		self.antonyDic = {}
	def createDic(self):
		reader = csv.reader(self.file)
		header = next(reader)
		for row in reader:
			if row[0] in self.antonyDic:
				self.antonyDic[row[0]] += [row[1]]
			else:
				self.antonyDic[row[0]] = [row[1]]
			if row[1] in self.antonyDic:
				self.antonyDic[row[1]] += [row[0]]
			else:
				self.antonyDic[row[1]] = [row[0]]
		self.file.close()

	def createPickle(self,filename="antonym.dump"):
		f = open(filename,'w')
		pickle.dump(self.antonyDic,f)
		f.close()

if __name__ == '__main__':
	s = JapaneseAntonym()	
	print s.getAntonym("勝ち")[0]