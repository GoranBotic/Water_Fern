# Generated from CPP14.g4 by ANTLR 4.7.1
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by CPP14Parser.

class CPPParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CPP14Parser#compilationUnit.
    def visitCompilationUnit(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#translationunit.
    def visitTranslationunit(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#primaryexpression.
    def visitPrimaryexpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#idexpression.
    def visitIdexpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#unqualifiedid.
    def visitUnqualifiedid(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#qualifiedid.
    def visitQualifiedid(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#nestednamespecifier.
    def visitNestednamespecifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#lambdaexpression.
    def visitLambdaexpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#lambdaintroducer.
    def visitLambdaintroducer(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#lambdacapture.
    def visitLambdacapture(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#capturedefault.
    def visitCapturedefault(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#capturelist.
    def visitCapturelist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#capture.
    def visitCapture(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#simplecapture.
    def visitSimplecapture(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#initcapture.
    def visitInitcapture(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#lambdadeclarator.
    def visitLambdadeclarator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#postfixexpression.
    def visitPostfixexpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#typeidofexpr.
    def visitTypeidofexpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#typeidofthetypeid.
    def visitTypeidofthetypeid(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#expressionlist.
    def visitExpressionlist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#pseudodestructorname.
    def visitPseudodestructorname(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#unaryexpression.
    def visitUnaryexpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#unaryoperator.
    def visitUnaryoperator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#newexpression.
    def visitNewexpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#newplacement.
    def visitNewplacement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#newtypeid.
    def visitNewtypeid(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#newdeclarator.
    def visitNewdeclarator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#noptrnewdeclarator.
    def visitNoptrnewdeclarator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#newinitializer.
    def visitNewinitializer(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#deleteexpression.
    def visitDeleteexpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#noexceptexpression.
    def visitNoexceptexpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#castexpression.
    def visitCastexpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#pmexpression.
    def visitPmexpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#multiplicativeexpression.
    def visitMultiplicativeexpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#additiveexpression.
    def visitAdditiveexpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#shiftexpression.
    def visitShiftexpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#shiftoperator.
    def visitShiftoperator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#relationalexpression.
    def visitRelationalexpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#equalityexpression.
    def visitEqualityexpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#andexpression.
    def visitAndexpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#exclusiveorexpression.
    def visitExclusiveorexpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#inclusiveorexpression.
    def visitInclusiveorexpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#logicalandexpression.
    def visitLogicalandexpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#logicalorexpression.
    def visitLogicalorexpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#conditionalexpression.
    def visitConditionalexpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#assignmentexpression.
    def visitAssignmentexpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#assignmentoperator.
    def visitAssignmentoperator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#expression.
    def visitExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#constantexpression.
    def visitConstantexpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#statement.
    def visitStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#labeledstatement.
    def visitLabeledstatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#expressionstatement.
    def visitExpressionstatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#compoundstatement.
    def visitCompoundstatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#statementseq.
    def visitStatementseq(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#selectionstatement.
    def visitSelectionstatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#condition.
    def visitCondition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#iterationstatement.
    def visitIterationstatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#forinitstatement.
    def visitForinitstatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#forrangedeclaration.
    def visitForrangedeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#forrangeinitializer.
    def visitForrangeinitializer(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#jumpstatement.
    def visitJumpstatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#declarationstatement.
    def visitDeclarationstatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#declarationseq.
    def visitDeclarationseq(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#declaration.
    def visitDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#blockdeclaration.
    def visitBlockdeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#aliasdeclaration.
    def visitAliasdeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#simpledeclaration.
    def visitSimpledeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#static_assertdeclaration.
    def visitStatic_assertdeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#emptydeclaration.
    def visitEmptydeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#attributedeclaration.
    def visitAttributedeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#declspecifier.
    def visitDeclspecifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#declspecifierseq.
    def visitDeclspecifierseq(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#storageclassspecifier.
    def visitStorageclassspecifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#functionspecifier.
    def visitFunctionspecifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#typedefname.
    def visitTypedefname(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#typespecifier.
    def visitTypespecifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#trailingtypespecifier.
    def visitTrailingtypespecifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#typespecifierseq.
    def visitTypespecifierseq(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#trailingtypespecifierseq.
    def visitTrailingtypespecifierseq(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#simpletypespecifier.
    def visitSimpletypespecifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#thetypename.
    def visitThetypename(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#decltypespecifier.
    def visitDecltypespecifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#elaboratedtypespecifier.
    def visitElaboratedtypespecifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#enumname.
    def visitEnumname(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#enumspecifier.
    def visitEnumspecifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#enumhead.
    def visitEnumhead(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#opaqueenumdeclaration.
    def visitOpaqueenumdeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#enumkey.
    def visitEnumkey(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#enumbase.
    def visitEnumbase(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#enumeratorlist.
    def visitEnumeratorlist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#enumeratordefinition.
    def visitEnumeratordefinition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#enumerator.
    def visitEnumerator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#namespacename.
    def visitNamespacename(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#originalnamespacename.
    def visitOriginalnamespacename(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#namespacedefinition.
    def visitNamespacedefinition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#namednamespacedefinition.
    def visitNamednamespacedefinition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#originalnamespacedefinition.
    def visitOriginalnamespacedefinition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#extensionnamespacedefinition.
    def visitExtensionnamespacedefinition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#unnamednamespacedefinition.
    def visitUnnamednamespacedefinition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#namespacebody.
    def visitNamespacebody(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#namespacealias.
    def visitNamespacealias(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#namespacealiasdefinition.
    def visitNamespacealiasdefinition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#qualifiednamespacespecifier.
    def visitQualifiednamespacespecifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#usingdeclaration.
    def visitUsingdeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#usingdirective.
    def visitUsingdirective(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#asmdefinition.
    def visitAsmdefinition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#linkagespecification.
    def visitLinkagespecification(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#attributespecifierseq.
    def visitAttributespecifierseq(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#attributespecifier.
    def visitAttributespecifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#alignmentspecifier.
    def visitAlignmentspecifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#attributelist.
    def visitAttributelist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#attribute.
    def visitAttribute(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#attributetoken.
    def visitAttributetoken(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#attributescopedtoken.
    def visitAttributescopedtoken(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#attributenamespace.
    def visitAttributenamespace(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#attributeargumentclause.
    def visitAttributeargumentclause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#balancedtokenseq.
    def visitBalancedtokenseq(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#balancedtoken.
    def visitBalancedtoken(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#initdeclaratorlist.
    def visitInitdeclaratorlist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#initdeclarator.
    def visitInitdeclarator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#declarator.
    def visitDeclarator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#ptrdeclarator.
    def visitPtrdeclarator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#noptrdeclarator.
    def visitNoptrdeclarator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#parametersandqualifiers.
    def visitParametersandqualifiers(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#trailingreturntype.
    def visitTrailingreturntype(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#ptroperator.
    def visitPtroperator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#cvqualifierseq.
    def visitCvqualifierseq(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#cvqualifier.
    def visitCvqualifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#refqualifier.
    def visitRefqualifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#declaratorid.
    def visitDeclaratorid(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#thetypeid.
    def visitThetypeid(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#abstractdeclarator.
    def visitAbstractdeclarator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#ptrabstractdeclarator.
    def visitPtrabstractdeclarator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#noptrabstractdeclarator.
    def visitNoptrabstractdeclarator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#abstractpackdeclarator.
    def visitAbstractpackdeclarator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#noptrabstractpackdeclarator.
    def visitNoptrabstractpackdeclarator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#parameterdeclarationclause.
    def visitParameterdeclarationclause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#parameterdeclarationlist.
    def visitParameterdeclarationlist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#parameterdeclaration.
    def visitParameterdeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#functiondefinition.
    def visitFunctiondefinition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#functionbody.
    def visitFunctionbody(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#initializer.
    def visitInitializer(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#braceorequalinitializer.
    def visitBraceorequalinitializer(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#initializerclause.
    def visitInitializerclause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#initializerlist.
    def visitInitializerlist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#bracedinitlist.
    def visitBracedinitlist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#classname.
    def visitClassname(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#classspecifier.
    def visitClassspecifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#classhead.
    def visitClasshead(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#classheadname.
    def visitClassheadname(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#classvirtspecifier.
    def visitClassvirtspecifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#classkey.
    def visitClasskey(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#memberspecification.
    def visitMemberspecification(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#memberdeclaration.
    def visitMemberdeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#memberdeclaratorlist.
    def visitMemberdeclaratorlist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#memberdeclarator.
    def visitMemberdeclarator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#virtspecifierseq.
    def visitVirtspecifierseq(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#virtspecifier.
    def visitVirtspecifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#purespecifier.
    def visitPurespecifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#baseclause.
    def visitBaseclause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#basespecifierlist.
    def visitBasespecifierlist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#basespecifier.
    def visitBasespecifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#classordecltype.
    def visitClassordecltype(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#basetypespecifier.
    def visitBasetypespecifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#accessspecifier.
    def visitAccessspecifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#conversionfunctionid.
    def visitConversionfunctionid(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#conversiontypeid.
    def visitConversiontypeid(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#conversiondeclarator.
    def visitConversiondeclarator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#ctorinitializer.
    def visitCtorinitializer(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#meminitializerlist.
    def visitMeminitializerlist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#meminitializer.
    def visitMeminitializer(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#meminitializerid.
    def visitMeminitializerid(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#operatorfunctionid.
    def visitOperatorfunctionid(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#literaloperatorid.
    def visitLiteraloperatorid(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#templatedeclaration.
    def visitTemplatedeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#templateparameterlist.
    def visitTemplateparameterlist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#templateparameter.
    def visitTemplateparameter(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#typeparameter.
    def visitTypeparameter(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#simpletemplateid.
    def visitSimpletemplateid(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#templateid.
    def visitTemplateid(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#templatename.
    def visitTemplatename(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#templateargumentlist.
    def visitTemplateargumentlist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#templateargument.
    def visitTemplateargument(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#typenamespecifier.
    def visitTypenamespecifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#explicitinstantiation.
    def visitExplicitinstantiation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#explicitspecialization.
    def visitExplicitspecialization(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#tryblock.
    def visitTryblock(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#functiontryblock.
    def visitFunctiontryblock(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#handlerseq.
    def visitHandlerseq(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#handler.
    def visitHandler(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#exceptiondeclaration.
    def visitExceptiondeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#throwexpression.
    def visitThrowexpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#exceptionspecification.
    def visitExceptionspecification(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#dynamicexceptionspecification.
    def visitDynamicexceptionspecification(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#typeidlist.
    def visitTypeidlist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#noexceptspecification.
    def visitNoexceptspecification(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#theoperator.
    def visitTheoperator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#literal.
    def visitLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#booleanliteral.
    def visitBooleanliteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#pointerliteral.
    def visitPointerliteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#userdefinedliteral.
    def visitUserdefinedliteral(self, ctx):
        return self.visitChildren(ctx)


