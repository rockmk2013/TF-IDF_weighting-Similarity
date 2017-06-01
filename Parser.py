#http://tartarus.org/~martin/PorterStemmer/python.txt
from PorterStemmer import PorterStemmer

class Parser:

	#A processor for removing the commoner morphological and inflexional endings from words in English
	stemmer=None

	stopwords=[]

	def __init__(self,):#導入字根還原的物件以及不理會的字彙表
		self.stemmer = PorterStemmer()

		#English stopwords from ftp://ftp.cs.cornell.edu/pub/smart/english.stop
		self.stopwords = open('english.stop', 'r').read().split()


	def clean(self, string):#清除文法上多餘的字彙
		""" remove any nasty grammar tokens from string """
		string = string.replace(".","")
		string = string.replace("\s+"," ")
		string = string.lower()
		return string
	

	def removeStopWords(self,list):
		""" Remove common words which have no search value """
		return [word for word in list if word not in self.stopwords ]


	def tokenise(self, string):
		""" break string up into tokens and stem words """
		string = self.clean(string)
		words = string.split(" ")
		
		return [self.stemmer.stem(word,0,len(word)-1) for word in words]


