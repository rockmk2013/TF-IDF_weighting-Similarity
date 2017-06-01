from pprint import pprint
from Parser import Parser
import os
from os import listdir
from os.path import isfile, join
import util
from textblob import TextBlob as tb

class VectorSpace:
    """ A algebraic model for representing text documents as vectors of identifiers. 
    A document is represented as a vector. Each dimension of the vector corresponds to a 
    separate term. If a term occurs in the document, then the value in the vector is non-zero.
    """
    #建立array
    #Collection of document term vectors
    documentVectors = []

    #Mapping of vector index to keyword
    vectorKeywordIndex=[]

    
    #Tidies terms
    parser=None


    def __init__(self, documents=[]):#建document
        self.documentVectors=[]
        self.parser = Parser()
        if(len(documents)>0):
            self.build(documents)


    def build(self,documents):#建document的函數
        """ Create the vector space for the passed document strings """
        self.vectorKeywordIndex = self.getVectorKeywordIndex(documents)
        self.documentVectors = [self.makeVector(document) for document in documents]

        #print self.vectorKeywordIndex
        #print self.documentVectors


    def getVectorKeywordIndex(self, documentList):#包在建Document的函數裡面#
        """ create the keyword associated to the position of the elements within the document vectors """

        #Mapped documents into a single word string	
        vocabularyString = " ".join(documentList)

        vocabularyList = self.parser.tokenise(vocabularyString)
        #Remove common words which have no search value
        vocabularyList = self.parser.removeStopWords(vocabularyList)
        uniqueVocabularyList = util.removeDuplicates(vocabularyList)

        vectorIndex={}
        offset=0
        #Associate a position with the keywords which maps to the dimension on the vector used to represent this word
        for word in uniqueVocabularyList:
            vectorIndex[word]=offset
            offset+=1
        return vectorIndex  #(keyword:position)


    def makeVector(self, wordString):#將文字轉為向量
        """ @pre: unique(vectorIndex) """

        #Initialise vector with 0's
        vector = [0] * len(self.vectorKeywordIndex)
        wordList = self.parser.tokenise(wordString)
        wordList = self.parser.removeStopWords(wordList)
        for word in wordList:
            vector[self.vectorKeywordIndex[word]] += 1; #Use simple Term Count Model
        return vector


    def buildQueryVector(self, termList):#將使用者輸入的query轉為向量
        """ convert query string into a term vector """
        query = self.makeVector(" ".join(termList))
        return query


    def related(self,documentId):#利用向量夾角公式算出rating#比較兩篇文章之間的相關性
        """ find documents that are related to the document indexed by passed Id within the document Vectors"""
        ratings = [util.cosine(self.documentVectors[documentId], documentVector) for documentVector in self.documentVectors]
        ratings.sort(reverse=True)
        return ratings


    def search(self,searchList):#將QUERY導入並進行RATING的動作，找出符合的document
        """ search for documents that match based on a list of terms """
        
        queryVector = self.buildQueryVector(searchList)
        ratings  = [util.cosine(queryVector, documentVector) for documentVector in self.documentVectors]
        

        ratingstf = []
        for document in documents_tf:
            ratingstf.append(util.tf(searchList[0],document))

        score1=[]

        for i in range(0,len(ratings),1):
            score1.append(ratings[i]+ratingstf[i])

        ratings_docid=[]
        while score1: ratings_docid.append([DocId.pop(0),score1.pop(0)])
        ratings_docid.sort(key=lambda x:x[1],reverse=True)
        
        
        return ratings_docid
    def search_idf(self,searchList):#將QUERY導入並進行RATING的動作，找出符合的document
        """ search for documents that match based on a list of terms """
        
        queryVector = self.buildQueryVector(searchList)
        ratings  = [util.cosine(queryVector, documentVector) for documentVector in self.documentVectors]
        
        ratingsidf =[]
        for document in documents_tf:
            ratingsidf.append(util.tfidf(searchList[0],document,documents_tf))

        score=[]

        for i in range(0,len(ratings),1):
            score.append(ratings[i]+ratingsidf[i])

            
        ratings_docid=[]

        while score: ratings_docid.append([DocId_1.pop(0),score.pop(0)])

        ratings_docid.sort(key=lambda x:x[1],reverse=True)

        return ratings_docid    
    def search_jaccard(self,searchList):#將QUERY導入並進行RATING的動作，找出符合的document
        """ search for documents that match based on a list of terms """
        
        ratings = []
        for document in documents:
            ratings.append(util.jaccard_similarity(searchList[0],document))

        ratingstf =[]
        for document in documents_tf:
            ratingstf.append(util.tf(searchList[0],document))

        score3=[]

        for i in range(0,len(ratings),1):
            score3.append(ratings[i]+ratingstf[i])

            
        ratings_docid=[]

        while score3: ratings_docid.append([DocId_3.pop(0),score3.pop(0)])

        ratings_docid.sort(key=lambda x:x[1],reverse=True)

        return ratings_docid    
    def search_jaccard_idf(self,searchList):#將QUERY導入並進行RATING的動作，找出符合的document
        """ search for documents that match based on a list of terms """ 
        ratings = []
        for document in documents:
            ratings.append(util.jaccard_similarity(searchList[0],document))
        ratingsidf =[]
        for document in documents_tf:
            ratingsidf.append(util.tfidf(searchList[0],document,documents_tf))

        score2=[]

        for i in range(0,len(ratings),1):
            score2.append(ratings[i]+ratingsidf[i])

            
        ratings_docid=[]

        while score2: ratings_docid.append([DocId_2.pop(0),score2.pop(0)])

        ratings_docid.sort(key=lambda x:x[1],reverse=True)

        return ratings_docid      



if __name__ == '__main__':
    #inputdata
    documents=[]
    for file in os.listdir("documents"):
        if file.endswith(".product"):
            f = os.path.join("documents", file)
            with open(f) as fh:
                documents.append(fh.read())   

    documents_tf=[]
    for filetf in os.listdir("documents"):
        if filetf.endswith(".product"):
            f1 = os.path.join("documents", filetf)
            with open(f1) as fh1:
                documents_tf.append(tb(fh1.read()))   

    #document1 = tb("""Python is a 2000 made-for-TV horror movie directed by Richard Clabaugh. The film features several cult favorite actors, including William Zabka of The Karate Kid fame, Wil Wheaton, Casper Van Dien, Jenny McCarthy, Keith Coogan, Robert Englund (best known for his role as Freddy Krueger in the A Nightmare on Elm Street series of films), Dana Barron, David Bowe, and Sean Whalen. The film concerns a genetically engineered snake, a python, that escapes and unleashes itself on a small town. It includes the classic final girl scenario evident in films like Friday the 13th. It was filmed in Los Angeles, California and Malibu, California. Python was followed by two sequels: Python II (2002) and Boa vs. Python (2004), both also made-for-TV films.""")
    #document2 = tb("""Python, from the Greek word, is a genus of nonvenomous pythons[2] found in Africa and Asia. Currently, 7 species are recognised.[2] A member of this genus, P. reticulatus, is among the longest snakes known.""")
    #document3 = tb("""The Colt Python is a .357 Magnum caliber revolver formerly manufactured by Colt's Manufacturing Company of Hartford, Connecticut.  It is sometimes referred to as a "Combat Magnum".[1] It was first introduced in 1955, the same year as Smith &amp; Wesson's M29 .44 Magnum. The now discontinued Colt Python targeted the premium revolver market segment. Some firearm collectors and writers such as Jeff Cooper, Ian V. Hogg, Chuck Hawks, Leroy Thompson, Renee Smeets and Martin Dougherty have described the Python as the finest production revolver ever made.""")

    #documents_tf = [document1, document2, document3]
            
    #建立docid 陣列        
    DocId=[]
    DocId_1=[]
    DocId_2=[]
    DocId_3=[]

    for f in os.listdir("documents"):
        DocId.append(f)
        DocId_1.append(f)
        DocId_2.append(f)
        DocId_3.append(f)
    
           
    #documents = ["The cat in the hat disabled",
    #             "A cat is a fine pet ponies.",
    #            "Dogs and cats make good pets.",
    #           "I haven't got a hat."]

    vectorSpace = VectorSpace(documents)

    #print(DocId)
    
    #print (vectorSpace.vectorKeywordIndex)

    #print (vectorSpace.documentVectors)

    #pprint(vectorSpace.related(1)[0:5])

    query = input('what is your query?')

    queryarray=[]

    queryarray.append(query)
    
    print("TF-weighting+cosine similarity.....")
    pprint(vectorSpace.search(queryarray)[0:5])#下query
    print("\n")
    print("TF-weighting+jaccard similarity.....")
    pprint(vectorSpace.search_jaccard(queryarray)[0:5])#下query
    print("\n")
    print("TF-IDF-weighting+cosine similarity.......")
    pprint(vectorSpace.search_idf(queryarray)[0:5])#下query
    print("\n")
    print("TF-IDF-weighting+jaccard similarity.....")
    pprint(vectorSpace.search_jaccard_idf(queryarray)[0:5])#下query




    

###################################################

