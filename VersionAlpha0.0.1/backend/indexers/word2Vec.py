import config
dbm = __import__(config.DATABASE_MANAGER)

import sys 
import os
import antlr4
from math import sqrt

from helpers._SourceIndexerW2VHash import getSourceIndexer

def index(submission_id):
    manager = dbm.DatabaseManager()
    data = manager.get_file(submission_id)
    name        = data[0]
    print(name)
    source      = bytes(data[1]).decode("utf-8")
    language    = data[2]

    #import parser and lexer based on language
    #TODO: vulnerability, filter language field
    #TODO: add a less hacky way of dealing with the C CPP problem 

    parserLang = language 
    if parserLang == "C":
        parserLang = "CPP" 

    __import__("helpers."+parserLang+"Parser")
    Parser = getattr(sys.modules["helpers."+parserLang+"Parser"],parserLang+"Parser")

    __import__("helpers."+parserLang+"Lexer")
    Lexer  = getattr(sys.modules["helpers."+parserLang+"Lexer"] ,parserLang+"Lexer" )

    inputData = antlr4.InputStream(source)
    lexer = Lexer(inputData)
    tokens = antlr4.CommonTokenStream(lexer)
    parser = Parser(tokens) 
    tree = parser.compilationUnit()

    sourceIndexer = getSourceIndexer(manager,submission_id,language)
    tokenList = sourceIndexer.visit(tree)
    manager.finish_indexing(submission_id, sourceIndexer.get_indexer_id())
    print(tokenList)



    