# Generated from JavaParser.g4 by ANTLR 4.7.1
from antlr4 import *
from indexer.JavaLexer import JavaLexer

# This class defines a complete generic visitor for a parse tree produced by JavaParser.

#theStuff = dict()

from hashlib import md5

class Tokenizer(ParseTreeVisitor):

    #this provides some default behavior
    def visit(self, ctx):
        if str(type(ctx)) == "<class 'antlr4.tree.Tree.TerminalNodeImpl'>":
            #theStuff[type(ctx.getParent())] = True
            #by default terminals simply evaluate to their symbol
            #to override this the vist... method which encounters the terminal should manually its children producing the desired terminal values for the terminal children
            #if that implementation is done then this line does not need to be changed, the default behavior will still be to use the symbol name
            return str(JavaLexer.symbolicNames[ctx.getSymbol().type])

        theList = ctx.accept(self)

        theHash = ""
        
        if len(theList) > 1:
            #do the aggregation
            #right now this simply concatenates all the strings and hashes
            #this needs to be changed so that similar sub-trees will get similar hashes

            #have all terminals evaluate to a type 
            #have all non-terminals evaluate to a type
            #name the thing according to the type frequency count
            for x in theList:
                if str(x).strip() != "":
                    theHash = theHash + x + "\n"
            
            #theHash = md5(theHash.encode()).hexdigest()
        else:
            theHash = theList[0]

        #store the hash in the DB along with some kind of link to its accociated code 
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
        print("Start parsing")
        print(ctx.getChildCount())

        tmp =  self.visitChildren(ctx)

        ret = "" 
        for x in tmp:
            ret = ret + x 
        #define a file scope dict called theStuff
        #in the visit method add something like theStuff[type(ctx.getParent())] = True 
        #then all vist... s with terminal children will be added to the stuff, and the keys of the stuff can be print to produce a list of terminal visit...s which required an implementation
        # for k in theStuff.keys():
        #     print(k)

        ret = ret.split("\n") 
        ret2 = [] 
        for x in ret:
            if x.strip() != "":
                ret2.append(x)
        return ret2


    # Visit a parse tree produced by JavaParser#packageDeclaration.
    def visitPackageDeclaration(self, ctx):
        print("packages")
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


