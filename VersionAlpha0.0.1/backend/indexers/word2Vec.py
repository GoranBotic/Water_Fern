import config
dbm = __import__(config.DATABASE_MANAGER)

import sys 
import os
import antlr4
from math import sqrt

from helpers._SourceIndexerW2VHash import SourceIndexer

def index(submission_id):
    manager = dbm.DatabaseManager()
    data = manager.get_file(submission_id)

    name        = data[0]
    source      = bytes(data[1].tolist()).decode("utf-8")
    language    = data[2]

    #import parser and lexer based on language
    #TODO: vulnerability, filter language field
    __import__("helpers."+language+"Parser")
    Parser = getattr(sys.modules["helpers."+language+"Parser"],language+"Parser")

    __import__("helpers."+language+"Lexer")
    Lexer  = getattr(sys.modules["helpers."+language+"Lexer"] ,language+"Lexer" )

    inputData = antlr4.InputStream(source)
    lexer = Lexer(inputData)
    tokens = antlr4.CommonTokenStream(lexer)
    parser = Parser(tokens) 
    tree = parser.compilationUnit()

    tokenList = SourceIndexer(manager,submission_id,language).visit(tree)




    