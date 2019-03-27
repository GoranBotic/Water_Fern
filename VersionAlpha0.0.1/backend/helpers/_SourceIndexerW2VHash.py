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

class SourceIndexer(ParseTreeVisitor):

    def __init__(self, DB, theID, lang):
        self.DB = DB
        self.theID = theID
        self.model = Word2Vec.load('helpers/word2vec_models/'+lang+'Model.bin')
        __import__("helpers."+lang+"Lexer")
        self.Lexer = getattr(sys.modules["helpers."+lang+"Lexer"],lang+"Lexer")

    #this provides some default behavior
    def visit(self, ctx):
        #if we're at a terminal node in the tree, then that node corresponds to a symbol
        #retrieve the appropriate symbol from the lexer, convert it to a vector with W2V, and add a few fields to hold the shape variables
        if str(type(ctx)) == "<class 'antlr4.tree.Tree.TerminalNodeImpl'>":
            word = list(self.model[str(self.Lexer.symbolicNames[ctx.getSymbol().type])])
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
            if ((contextList[3] - contextList[2] >= 1) and (contextList[3] - contextList[2] <= 10)):
                block_id = self.DB.store_index("w2v_n_000", self.theID, theHash, contextList[2], contextList[3])

                #block_id = self.DB.store_index() 

                #add associations between this sub-tree and the most similar sub-trees
                similarBlocks = self.DB.find_cosine_similar_indicies("w2v_n_000", theHash, self.theID)
                similarity = []
                for r in similarBlocks:
                    print(r)
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

    # def visitTerminal(self, ctx):
    #     return 1
        

    # Visit a parse tree produced by JavaParser#compilationUnit.
    def visitCompilationUnit(self, ctx):
    
        tmp =  self.visitChildren(ctx)

        #define a file scope dict called theStuff
        #in the visit method add something like theStuff[type(ctx.getParent())] = True 
        #then all vist... s with terminal children will be added to the stuff, and the keys of the stuff can be print to produce a list of terminal visit...s which required an implementation
        # for k in theStuff.keys():
        #     print(k)
        return tmp


    # Visit a parse tree produced by JavaParser#packageDeclaration.
    def visitPackageDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#importDeclaration.
    def visitImportDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#typeDeclaration.
    def visitTypeDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#modifier.
    def visitModifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#classOrInterfaceModifier.
    def visitClassOrInterfaceModifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#variableModifier.
    def visitVariableModifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#classDeclaration.
    def visitClassDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#typeParameters.
    def visitTypeParameters(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#typeParameter.
    def visitTypeParameter(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#typeBound.
    def visitTypeBound(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#enumDeclaration.
    def visitEnumDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#enumConstants.
    def visitEnumConstants(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#enumConstant.
    def visitEnumConstant(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#enumBodyDeclarations.
    def visitEnumBodyDeclarations(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#interfaceDeclaration.
    def visitInterfaceDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#classBody.
    def visitClassBody(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#interfaceBody.
    def visitInterfaceBody(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#classBodyDeclaration.
    def visitClassBodyDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#memberDeclaration.
    def visitMemberDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#methodBody.
    def visitMethodBody(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#typeTypeOrVoid.
    def visitTypeTypeOrVoid(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#genericMethodDeclaration.
    def visitGenericMethodDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#genericConstructorDeclaration.
    def visitGenericConstructorDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#constructorDeclaration.
    def visitConstructorDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#fieldDeclaration.
    def visitFieldDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#interfaceBodyDeclaration.
    def visitInterfaceBodyDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#interfaceMemberDeclaration.
    def visitInterfaceMemberDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#constDeclaration.
    def visitConstDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#constantDeclarator.
    def visitConstantDeclarator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#interfaceMethodDeclaration.
    def visitInterfaceMethodDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#interfaceMethodModifier.
    def visitInterfaceMethodModifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#genericInterfaceMethodDeclaration.
    def visitGenericInterfaceMethodDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#variableDeclarators.
    def visitVariableDeclarators(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#variableDeclarator.
    def visitVariableDeclarator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#variableDeclaratorId.
    def visitVariableDeclaratorId(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#variableInitializer.
    def visitVariableInitializer(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#arrayInitializer.
    def visitArrayInitializer(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#classOrInterfaceType.
    def visitClassOrInterfaceType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#typeArgument.
    def visitTypeArgument(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#qualifiedNameList.
    def visitQualifiedNameList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#formalParameters.
    def visitFormalParameters(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#formalParameterList.
    def visitFormalParameterList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#formalParameter.
    def visitFormalParameter(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#lastFormalParameter.
    def visitLastFormalParameter(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#qualifiedName.
    def visitQualifiedName(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#literal.
    def visitLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#integerLiteral.
    def visitIntegerLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#floatLiteral.
    def visitFloatLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#annotation.
    def visitAnnotation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#elementValuePairs.
    def visitElementValuePairs(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#elementValuePair.
    def visitElementValuePair(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#elementValue.
    def visitElementValue(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#elementValueArrayInitializer.
    def visitElementValueArrayInitializer(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#annotationTypeDeclaration.
    def visitAnnotationTypeDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#annotationTypeBody.
    def visitAnnotationTypeBody(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#annotationTypeElementDeclaration.
    def visitAnnotationTypeElementDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#annotationTypeElementRest.
    def visitAnnotationTypeElementRest(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#annotationMethodOrConstantRest.
    def visitAnnotationMethodOrConstantRest(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#annotationMethodRest.
    def visitAnnotationMethodRest(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#annotationConstantRest.
    def visitAnnotationConstantRest(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#defaultValue.
    def visitDefaultValue(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#block.
    def visitBlock(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#blockStatement.
    def visitBlockStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#localVariableDeclaration.
    def visitLocalVariableDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#localTypeDeclaration.
    def visitLocalTypeDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#statement.
    def visitStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#catchClause.
    def visitCatchClause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#catchType.
    def visitCatchType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#finallyBlock.
    def visitFinallyBlock(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#resourceSpecification.
    def visitResourceSpecification(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#resources.
    def visitResources(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#resource.
    def visitResource(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#switchBlockStatementGroup.
    def visitSwitchBlockStatementGroup(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#switchLabel.
    def visitSwitchLabel(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#forControl.
    def visitForControl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#forInit.
    def visitForInit(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#enhancedForControl.
    def visitEnhancedForControl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#parExpression.
    def visitParExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#expressionList.
    def visitExpressionList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#methodCall.
    def visitMethodCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#expression.
    def visitExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#lambdaExpression.
    def visitLambdaExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#lambdaParameters.
    def visitLambdaParameters(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#lambdaBody.
    def visitLambdaBody(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#primary.
    def visitPrimary(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#classType.
    def visitClassType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#creator.
    def visitCreator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#createdName.
    def visitCreatedName(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#innerCreator.
    def visitInnerCreator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#arrayCreatorRest.
    def visitArrayCreatorRest(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#classCreatorRest.
    def visitClassCreatorRest(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#explicitGenericInvocation.
    def visitExplicitGenericInvocation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#typeArgumentsOrDiamond.
    def visitTypeArgumentsOrDiamond(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#nonWildcardTypeArgumentsOrDiamond.
    def visitNonWildcardTypeArgumentsOrDiamond(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#nonWildcardTypeArguments.
    def visitNonWildcardTypeArguments(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#typeList.
    def visitTypeList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#typeType.
    def visitTypeType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#primitiveType.
    def visitPrimitiveType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#typeArguments.
    def visitTypeArguments(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#superSuffix.
    def visitSuperSuffix(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#explicitGenericInvocationSuffix.
    def visitExplicitGenericInvocationSuffix(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#arguments.
    def visitArguments(self, ctx):
        return self.visitChildren(ctx)


