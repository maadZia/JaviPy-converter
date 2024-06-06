# Generated from ..//Desktop//konw_v1//grammar//javipyGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .javipyGrammarParser import javipyGrammarParser
else:
    from javipyGrammarParser import javipyGrammarParser

# This class defines a complete generic visitor for a parse tree produced by javipyGrammarParser.

class javipyGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by javipyGrammarParser#program.
    def visitProgram(self, ctx:javipyGrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#import_statement.
    def visitImport_statement(self, ctx:javipyGrammarParser.Import_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#class_declaration.
    def visitClass_declaration(self, ctx:javipyGrammarParser.Class_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#class_body.
    def visitClass_body(self, ctx:javipyGrammarParser.Class_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#field_declaration.
    def visitField_declaration(self, ctx:javipyGrammarParser.Field_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#method_declaration.
    def visitMethod_declaration(self, ctx:javipyGrammarParser.Method_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#constructor.
    def visitConstructor(self, ctx:javipyGrammarParser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#access.
    def visitAccess(self, ctx:javipyGrammarParser.AccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#data_type.
    def visitData_type(self, ctx:javipyGrammarParser.Data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#type.
    def visitType(self, ctx:javipyGrammarParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#literal.
    def visitLiteral(self, ctx:javipyGrammarParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#parameter_list.
    def visitParameter_list(self, ctx:javipyGrammarParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#parameter.
    def visitParameter(self, ctx:javipyGrammarParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#argument_list.
    def visitArgument_list(self, ctx:javipyGrammarParser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#argument.
    def visitArgument(self, ctx:javipyGrammarParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#block.
    def visitBlock(self, ctx:javipyGrammarParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#statement.
    def visitStatement(self, ctx:javipyGrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#block_statement.
    def visitBlock_statement(self, ctx:javipyGrammarParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#local_variable.
    def visitLocal_variable(self, ctx:javipyGrammarParser.Local_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#assignment.
    def visitAssignment(self, ctx:javipyGrammarParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#class_object.
    def visitClass_object(self, ctx:javipyGrammarParser.Class_objectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#expression.
    def visitExpression(self, ctx:javipyGrammarParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#logical_expression.
    def visitLogical_expression(self, ctx:javipyGrammarParser.Logical_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#logical_term.
    def visitLogical_term(self, ctx:javipyGrammarParser.Logical_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#logical_operator.
    def visitLogical_operator(self, ctx:javipyGrammarParser.Logical_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#arithmetic_expression.
    def visitArithmetic_expression(self, ctx:javipyGrammarParser.Arithmetic_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#arithmetic_term.
    def visitArithmetic_term(self, ctx:javipyGrammarParser.Arithmetic_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#arithmetic_operator.
    def visitArithmetic_operator(self, ctx:javipyGrammarParser.Arithmetic_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#compare_operator.
    def visitCompare_operator(self, ctx:javipyGrammarParser.Compare_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#if_statement.
    def visitIf_statement(self, ctx:javipyGrammarParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#elseif_statement.
    def visitElseif_statement(self, ctx:javipyGrammarParser.Elseif_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#else_statement.
    def visitElse_statement(self, ctx:javipyGrammarParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#switch_case_statement.
    def visitSwitch_case_statement(self, ctx:javipyGrammarParser.Switch_case_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#switch_block.
    def visitSwitch_block(self, ctx:javipyGrammarParser.Switch_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#switch_case.
    def visitSwitch_case(self, ctx:javipyGrammarParser.Switch_caseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#default_case.
    def visitDefault_case(self, ctx:javipyGrammarParser.Default_caseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#loop_statement.
    def visitLoop_statement(self, ctx:javipyGrammarParser.Loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#for_statement.
    def visitFor_statement(self, ctx:javipyGrammarParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#for_condition.
    def visitFor_condition(self, ctx:javipyGrammarParser.For_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#inc_dec.
    def visitInc_dec(self, ctx:javipyGrammarParser.Inc_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#while_statement.
    def visitWhile_statement(self, ctx:javipyGrammarParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#while_condition.
    def visitWhile_condition(self, ctx:javipyGrammarParser.While_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#try_catch_statement.
    def visitTry_catch_statement(self, ctx:javipyGrammarParser.Try_catch_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#catch_statement.
    def visitCatch_statement(self, ctx:javipyGrammarParser.Catch_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#print_statement.
    def visitPrint_statement(self, ctx:javipyGrammarParser.Print_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#print_term.
    def visitPrint_term(self, ctx:javipyGrammarParser.Print_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#return_statement.
    def visitReturn_statement(self, ctx:javipyGrammarParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#break_statement.
    def visitBreak_statement(self, ctx:javipyGrammarParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#continue_statement.
    def visitContinue_statement(self, ctx:javipyGrammarParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javipyGrammarParser#function_call.
    def visitFunction_call(self, ctx:javipyGrammarParser.Function_callContext):
        return self.visitChildren(ctx)



del javipyGrammarParser