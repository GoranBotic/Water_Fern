antlr4 -Dlanguage=Python2 JavaLexer.g4 
antlr4 -Dlanguage=Python2 -visitor JavaParser.g4

#Ideally the code for the visitor should be written in a separate file, which will not be overwritten if the lexer and parser are re-generated
#Right here that code should get coppied over into the visitor