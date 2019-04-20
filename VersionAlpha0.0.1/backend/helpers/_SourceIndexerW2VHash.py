# Generated from JavaParser.g4 by ANTLR 4.7.1
from antlr4 import *
from gensim.models import Word2Vec
from math import sqrt
import sys
from helpers.SimilarityMeasures import *
#from indexer.DB import DB

# This class defines a complete generic visitor for a parse tree produced by JavaParser.

#theStuff = dict()

from hashlib import md5

def getSourceIndexer(argDB, argtheID, arglang):
    #TODO: since the C grammar is irreparibly broken we use the CPP parser for C files
    #We still have a separate W2V model for C however, which was trained only on C files 
    #this TODO is here becuase this if is kind of hacky, and TODO makes it easier to find again in the case of weird behavior 
    parserLang = arglang 
    if parserLang == "C":
        parserLang = "CPP" 

    __import__("helpers."+parserLang+"ParserVisitor")
    PV = getattr(sys.modules["helpers."+parserLang+"ParserVisitor"],parserLang+"ParserVisitor")

    class SourceIndexer(PV):

        def __init__(self, DB, theID, lang):
            self.indexerID = "w2v_"+lang+"_n_000"
            self.DB = DB
            self.theID = theID
            self.theaID = self.DB.get_assign_id(self.theID)[0]
            self.model = Word2Vec.load('helpers/word2vec_models/'+lang+'Model.bin')
            __import__("helpers."+parserLang+"Parser")
            self.Parser = getattr(sys.modules["helpers."+parserLang+"Parser"],parserLang+"Parser")

        def get_indexer_id(self):
            return self.indexerID 

        #this provides some default behavior
        def visit(self, ctx):
            #if we're at a terminal node in the tree, then that node corresponds to a symbol
            #retrieve the appropriate symbol from the lexer, convert it to a vector with W2V, and add a few fields to hold the shape variables
            if str(type(ctx)) == "<class 'antlr4.tree.Tree.TerminalNodeImpl'>":
                word = None
                try:
                    word = list(self.model[str(self.Parser.symbolicNames[ctx.getSymbol().type])])
                except:
                    return None 
                    
                stop = len(word)-1
                for x in range(stop):
                    word.append(10)
                return (word, ctx.getParent().depth(), ctx.getSymbol().line,ctx.getSymbol().line)

            #otherwise this node has a list of children, so we get the children
            theList = ctx.accept(self)
            theHash = []

            #ctx.accept will return None when it fails to parse some code
            #ANTLR will simply discard tokens from the input stream until it finds sane input
            #this code just passes None back up the tree to allow ANTLR to continue and try to find sane input
            if theList == None:
                return None

            if theList == None:
                return None

            tmpList = []
            for l in theList:
                if l != None:
                    tmpList.append(l)

            theList = tmpList
            if len(theList) == 0:
                return None

            #modify theList to contain only index vectors, since that what the aggregation code expects
            #the additional information in theList will be used later
            fullList = [l for l in theList] 
            theList = [l[0] for l in theList]
            
            #if the list contains more than 1 child, we need to aggregate the children into a single vector
            if len(theList) > 1:
                #a blank vector to contain the aggregate
                aggregate = [0 for x in range(len(theList[0]))] 

                #magnitude of components start to end-1 of a vector
                def mag(start, end, X):
                    mag = 0
                    for i in range(start, end):
                        mag += (X[i]**2)
                    
                    return sqrt(mag)
                
                #dot product between components start to end-1 of vectors X and Y
                def dot(start, end, X, Y):
                    dot = 0
                    for i in range(start, end):
                        dot += (X[i]*Y[i])
                    return dot

                #cosine similarity between sub-vectors in X and Y
                #these values are used to fill in the 'shape' component of the index
                def coSim(X, Y):
                    top = int(len(X)/2)

                    lenX = []
                    lenY = [] 

                    for i in range(top):
                        lenX.append(mag(i, i+2, X))
                        lenY.append(mag(i, i+2, Y))

                    # lenX1 = mag(0, split+1, X)
                    # lenY1 = mag(0, split+1, Y) 

                    # lenX2 = mag(split, len(X)-2, X)
                    # lenY2 = mag(split, len(Y)-2, Y)

                    # score = (dot(0, split+1, X, Y)/(lenX1*lenY1),dot(split, len(X)-2, X, Y)/(lenX2*lenY2))

                    score = []
                    for i in range(top):
                        score.append(dot(i, i+2, X, Y)/(lenX[i]*lenY[i]))

                    return score

                #aggregate[:top+1] is the portion of aggregate which depends on the word2vec embedding 
                #the rest of aggregate is the shape components
                top = int(len(aggregate)/2)

                #average the word2vec embedding portion of all indexes
                for l in theList:
                    for v in range(len(l)):
                        aggregate[v] += l[v] 
                for v in range(top+1):
                    aggregate[v] /= len(theList) 

                
                for l in theList:
                    #if a vector has 10 in its final component, it is not an aggregate, so we need to calculate this vectors contribution to the shape components of the aggregate
                    #the shape components are averaged cosine similarity, so can never get a value of 10
                    if l[-1] == 10:
                        # aggregate[-2] += coSim(0, 1, aggregate, l)
                        # aggregate[-1] += coSim(1,2,aggregate, l)
                        score = coSim(aggregate,l)
                        # aggregate[-2] += score[0]
                        # aggregate[-1] += score[1]
                        for x in range(top):
                            aggregate[-(x+1)] += score[-(x+1)]

                #final divide the shape components by the number of contributors
                for x in range(top):
                    aggregate[-(x+1)] /= len(theList)
                # aggregate[-2] /= len(theList)
                # aggregate[-1] /= len(theList)

                theHash = aggregate

                #reduce the index to a unit vector
                magHash = mag(0, len(theHash), theHash)
                theHash = [x/magHash for x in theHash]

                def findStart(ctx):
                    if ctx.getChildCount() > 0:
                        return findStart(ctx.getChild(0))
                    else:
                        ret = (ctx.getSymbol()).line
                        return ret

                def findEnd(ctx):
                    if ctx.getChildCount() > 0:
                        
                        return findEnd(ctx.getChild(ctx.getChildCount()-1))
                    else:
                        
                        return ctx.getSymbol().line

                

                #store_index(self, itype, submission_id, index, start_line=0, end_line=0)

                maxDepth = 0
                strtLine = fullList[0][2]
                endLine = fullList[0][2]
                for l in fullList:
                    if l[1] > maxDepth:
                        maxDepth = l[1] 
                    if l[2] > endLine:
                        endLine = l[2] 
                    if l[2] < strtLine:
                        startLine = l[2]
                
                contextList = (theHash, maxDepth, strtLine, endLine)
                #(contextList[1] > 20 and contextList[1] < 30) or
                if ((contextList[3] - contextList[2] >= 2) and (contextList[3] - contextList[2] <= 20)):
                    block_id = self.DB.store_index(self.indexerID, self.theID, self.theaID, theHash, contextList[2], contextList[3])

                    #block_id = self.DB.store_index() 

                    #add associations between this sub-tree and the most similar sub-trees
                    similarBlocks = self.DB.find_cosine_similar_indicies(self.indexerID, theHash, self.theID, self.theaID)
                    similarity = []
                    for r in similarBlocks:
                        similarity.append(cosineSimilarity(theHash, r[2]))
                        print([r[0], self.theID, block_id, r[1], similarity[-1]])
                    
                    if len(similarity) >0:
                        aveSim = sum(similarity)/len(similarity)
                        for r in range(len(similarBlocks)): 
                            if similarBlocks[r][0] != self.theID and similarity[r] > aveSim:
                                self.DB.associate_indicies(similarBlocks[r][0], self.theID, block_id, similarBlocks[r][1], similarity[r])
                                


                theHash = contextList
            #this node had only 1 child, so just pass it up the tree
            else:
                theHash = fullList[0]

    
            #should also search for existing similar code

            return theHash

        def visitChildren(self, ctx):
            ret = []

            for x in range(ctx.getChildCount()):
                # if str(type(ctx.getChild(x))) == "<class 'antlr4.tree.Tree.TerminalNodeImpl'>":
                #     print(ctx.getChild(x).getSymbol())
                # else:
                #     print(ctx.getChild(x).getPayload().toStringTree())
                ret.append(self.visit(ctx.getChild(x)))

            return ret

    return SourceIndexer(argDB, argtheID, arglang)
