import sys 
import os
from antlr4 import *
from indexer.JavaLexer import JavaLexer
from indexer.JavaParser import JavaParser
from indexer.JavaSourceIndexer import JavaSourceIndexer
from math import sqrt
from indexer.DB import DB
import rpy2.robjects as R

def coSim(x, y):
    dot = 0 
    for v in range(len(x)):
        dot += x[v]*y[v]
    len1 = 0
    for v in x:
        len1 += (v**2)
    len1 = sqrt(len1)
    len2 = 0
    for v in y:
        len2 += (v**2)
    len2 = sqrt(len2) 

    return dot/(len1*len2)

theTestFiles = dict()
def main(args):
    theDB = DB(":memory:")
    for no, pe, files in os.walk(args[1]):
        for f in files:
            print("indexing: " + args[1] + "/" + f)
            inputData = FileStream(args[1] + "/" + f)
            lexer = JavaLexer(inputData)
            tokens = CommonTokenStream(lexer)
            parser = JavaParser(tokens) 
            tree = parser.compilationUnit()

            theFileID = -1
            with open(args[1] + "/" + f, 'r') as tehFile:
                theFileID = theDB.putFile(tehFile.read())[0]

            tokenList = JavaSourceIndexer(theDB, theFileID).visit(tree)
            #print(tokenList)
            theTestFiles[f] = tokenList
    
    problems = theTestFiles.keys()
    problems.sort() 
    
    finds = 0.0
    total = 0.0

    diffSims = []
    sameSims = []

    for i in range(len(problems)):
        sameSim = 0
        sameCount = 0
        diffSim = 0
        diffCount = 0
        for j in range(len(problems)):
            if problems[j][:problems[j].find(".")] == problems[i][:problems[i].find(".")] and problems[j] != problems[i]:
                sameSim += coSim(theTestFiles[problems[i]], theTestFiles[problems[j]])
                sameCount += 1
            else:
                diffSim += coSim(theTestFiles[problems[i]], theTestFiles[problems[j]])
                diffCount += 1
        sameSim /= sameCount
        diffSim /= diffCount
        if sameSim > diffSim:
            finds += 1.0
        else:
            print(problems[i] + " was more similar to arbitrary code than to mutations of " + problems[i])
        total += 1.0

        diffSims.append(diffSim)
        sameSims.append(sameSim)
     
    
    print(str(finds/total) + " percent of files were more similar to mutations of themselves than to arbitary code.")
    


    # t-test

    res = R.r['t.test'](R.FloatVector(sameSims), R.FloatVector(diffSims))
    
    print("The p-value of a student's t test, testing the difference in similarity between mutations of code, and arbitrary code is:")
    print(res.rx('p.value')[0][0])

    print("The 95% confidence interval of the difference is:")
    print(res.rx('conf.int')[0])
    
if __name__ == '__main__':
    main(sys.argv)
