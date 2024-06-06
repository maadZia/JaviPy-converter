# Generated from ..//Desktop//konw_v1//grammar//javipyGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .javipyGrammarParser import javipyGrammarParser
else:
    from javipyGrammarParser import javipyGrammarParser

# This class defines a complete listener for a parse tree produced by javipyGrammarParser.
class javipyGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by javipyGrammarParser#program.
    def enterProgram(self, ctx:javipyGrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#program.
    def exitProgram(self, ctx:javipyGrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#import_statement.
    def enterImport_statement(self, ctx:javipyGrammarParser.Import_statementContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#import_statement.
    def exitImport_statement(self, ctx:javipyGrammarParser.Import_statementContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#class_declaration.
    def enterClass_declaration(self, ctx:javipyGrammarParser.Class_declarationContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#class_declaration.
    def exitClass_declaration(self, ctx:javipyGrammarParser.Class_declarationContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#class_body.
    def enterClass_body(self, ctx:javipyGrammarParser.Class_bodyContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#class_body.
    def exitClass_body(self, ctx:javipyGrammarParser.Class_bodyContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#field_declaration.
    def enterField_declaration(self, ctx:javipyGrammarParser.Field_declarationContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#field_declaration.
    def exitField_declaration(self, ctx:javipyGrammarParser.Field_declarationContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#method_declaration.
    def enterMethod_declaration(self, ctx:javipyGrammarParser.Method_declarationContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#method_declaration.
    def exitMethod_declaration(self, ctx:javipyGrammarParser.Method_declarationContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#constructor.
    def enterConstructor(self, ctx:javipyGrammarParser.ConstructorContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#constructor.
    def exitConstructor(self, ctx:javipyGrammarParser.ConstructorContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#access.
    def enterAccess(self, ctx:javipyGrammarParser.AccessContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#access.
    def exitAccess(self, ctx:javipyGrammarParser.AccessContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#data_type.
    def enterData_type(self, ctx:javipyGrammarParser.Data_typeContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#data_type.
    def exitData_type(self, ctx:javipyGrammarParser.Data_typeContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#type.
    def enterType(self, ctx:javipyGrammarParser.TypeContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#type.
    def exitType(self, ctx:javipyGrammarParser.TypeContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#literal.
    def enterLiteral(self, ctx:javipyGrammarParser.LiteralContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#literal.
    def exitLiteral(self, ctx:javipyGrammarParser.LiteralContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#parameter_list.
    def enterParameter_list(self, ctx:javipyGrammarParser.Parameter_listContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#parameter_list.
    def exitParameter_list(self, ctx:javipyGrammarParser.Parameter_listContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#parameter.
    def enterParameter(self, ctx:javipyGrammarParser.ParameterContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#parameter.
    def exitParameter(self, ctx:javipyGrammarParser.ParameterContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#argument_list.
    def enterArgument_list(self, ctx:javipyGrammarParser.Argument_listContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#argument_list.
    def exitArgument_list(self, ctx:javipyGrammarParser.Argument_listContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#argument.
    def enterArgument(self, ctx:javipyGrammarParser.ArgumentContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#argument.
    def exitArgument(self, ctx:javipyGrammarParser.ArgumentContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#block.
    def enterBlock(self, ctx:javipyGrammarParser.BlockContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#block.
    def exitBlock(self, ctx:javipyGrammarParser.BlockContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#statement.
    def enterStatement(self, ctx:javipyGrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#statement.
    def exitStatement(self, ctx:javipyGrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#block_statement.
    def enterBlock_statement(self, ctx:javipyGrammarParser.Block_statementContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#block_statement.
    def exitBlock_statement(self, ctx:javipyGrammarParser.Block_statementContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#local_variable.
    def enterLocal_variable(self, ctx:javipyGrammarParser.Local_variableContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#local_variable.
    def exitLocal_variable(self, ctx:javipyGrammarParser.Local_variableContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#assignment.
    def enterAssignment(self, ctx:javipyGrammarParser.AssignmentContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#assignment.
    def exitAssignment(self, ctx:javipyGrammarParser.AssignmentContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#class_object.
    def enterClass_object(self, ctx:javipyGrammarParser.Class_objectContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#class_object.
    def exitClass_object(self, ctx:javipyGrammarParser.Class_objectContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#expression.
    def enterExpression(self, ctx:javipyGrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#expression.
    def exitExpression(self, ctx:javipyGrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#logical_expression.
    def enterLogical_expression(self, ctx:javipyGrammarParser.Logical_expressionContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#logical_expression.
    def exitLogical_expression(self, ctx:javipyGrammarParser.Logical_expressionContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#logical_term.
    def enterLogical_term(self, ctx:javipyGrammarParser.Logical_termContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#logical_term.
    def exitLogical_term(self, ctx:javipyGrammarParser.Logical_termContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#logical_operator.
    def enterLogical_operator(self, ctx:javipyGrammarParser.Logical_operatorContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#logical_operator.
    def exitLogical_operator(self, ctx:javipyGrammarParser.Logical_operatorContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#arithmetic_expression.
    def enterArithmetic_expression(self, ctx:javipyGrammarParser.Arithmetic_expressionContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#arithmetic_expression.
    def exitArithmetic_expression(self, ctx:javipyGrammarParser.Arithmetic_expressionContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#arithmetic_term.
    def enterArithmetic_term(self, ctx:javipyGrammarParser.Arithmetic_termContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#arithmetic_term.
    def exitArithmetic_term(self, ctx:javipyGrammarParser.Arithmetic_termContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#arithmetic_operator.
    def enterArithmetic_operator(self, ctx:javipyGrammarParser.Arithmetic_operatorContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#arithmetic_operator.
    def exitArithmetic_operator(self, ctx:javipyGrammarParser.Arithmetic_operatorContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#compare_operator.
    def enterCompare_operator(self, ctx:javipyGrammarParser.Compare_operatorContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#compare_operator.
    def exitCompare_operator(self, ctx:javipyGrammarParser.Compare_operatorContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#if_statement.
    def enterIf_statement(self, ctx:javipyGrammarParser.If_statementContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#if_statement.
    def exitIf_statement(self, ctx:javipyGrammarParser.If_statementContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#elseif_statement.
    def enterElseif_statement(self, ctx:javipyGrammarParser.Elseif_statementContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#elseif_statement.
    def exitElseif_statement(self, ctx:javipyGrammarParser.Elseif_statementContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#else_statement.
    def enterElse_statement(self, ctx:javipyGrammarParser.Else_statementContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#else_statement.
    def exitElse_statement(self, ctx:javipyGrammarParser.Else_statementContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#switch_case_statement.
    def enterSwitch_case_statement(self, ctx:javipyGrammarParser.Switch_case_statementContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#switch_case_statement.
    def exitSwitch_case_statement(self, ctx:javipyGrammarParser.Switch_case_statementContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#switch_block.
    def enterSwitch_block(self, ctx:javipyGrammarParser.Switch_blockContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#switch_block.
    def exitSwitch_block(self, ctx:javipyGrammarParser.Switch_blockContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#switch_case.
    def enterSwitch_case(self, ctx:javipyGrammarParser.Switch_caseContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#switch_case.
    def exitSwitch_case(self, ctx:javipyGrammarParser.Switch_caseContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#default_case.
    def enterDefault_case(self, ctx:javipyGrammarParser.Default_caseContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#default_case.
    def exitDefault_case(self, ctx:javipyGrammarParser.Default_caseContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#loop_statement.
    def enterLoop_statement(self, ctx:javipyGrammarParser.Loop_statementContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#loop_statement.
    def exitLoop_statement(self, ctx:javipyGrammarParser.Loop_statementContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#for_statement.
    def enterFor_statement(self, ctx:javipyGrammarParser.For_statementContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#for_statement.
    def exitFor_statement(self, ctx:javipyGrammarParser.For_statementContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#for_condition.
    def enterFor_condition(self, ctx:javipyGrammarParser.For_conditionContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#for_condition.
    def exitFor_condition(self, ctx:javipyGrammarParser.For_conditionContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#inc_dec.
    def enterInc_dec(self, ctx:javipyGrammarParser.Inc_decContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#inc_dec.
    def exitInc_dec(self, ctx:javipyGrammarParser.Inc_decContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#while_statement.
    def enterWhile_statement(self, ctx:javipyGrammarParser.While_statementContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#while_statement.
    def exitWhile_statement(self, ctx:javipyGrammarParser.While_statementContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#while_condition.
    def enterWhile_condition(self, ctx:javipyGrammarParser.While_conditionContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#while_condition.
    def exitWhile_condition(self, ctx:javipyGrammarParser.While_conditionContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#try_catch_statement.
    def enterTry_catch_statement(self, ctx:javipyGrammarParser.Try_catch_statementContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#try_catch_statement.
    def exitTry_catch_statement(self, ctx:javipyGrammarParser.Try_catch_statementContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#catch_statement.
    def enterCatch_statement(self, ctx:javipyGrammarParser.Catch_statementContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#catch_statement.
    def exitCatch_statement(self, ctx:javipyGrammarParser.Catch_statementContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#print_statement.
    def enterPrint_statement(self, ctx:javipyGrammarParser.Print_statementContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#print_statement.
    def exitPrint_statement(self, ctx:javipyGrammarParser.Print_statementContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#print_term.
    def enterPrint_term(self, ctx:javipyGrammarParser.Print_termContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#print_term.
    def exitPrint_term(self, ctx:javipyGrammarParser.Print_termContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#return_statement.
    def enterReturn_statement(self, ctx:javipyGrammarParser.Return_statementContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#return_statement.
    def exitReturn_statement(self, ctx:javipyGrammarParser.Return_statementContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#break_statement.
    def enterBreak_statement(self, ctx:javipyGrammarParser.Break_statementContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#break_statement.
    def exitBreak_statement(self, ctx:javipyGrammarParser.Break_statementContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#continue_statement.
    def enterContinue_statement(self, ctx:javipyGrammarParser.Continue_statementContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#continue_statement.
    def exitContinue_statement(self, ctx:javipyGrammarParser.Continue_statementContext):
        pass


    # Enter a parse tree produced by javipyGrammarParser#function_call.
    def enterFunction_call(self, ctx:javipyGrammarParser.Function_callContext):
        pass

    # Exit a parse tree produced by javipyGrammarParser#function_call.
    def exitFunction_call(self, ctx:javipyGrammarParser.Function_callContext):
        pass



del javipyGrammarParser