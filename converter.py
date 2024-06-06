import sys
from antlr4 import *
from gen.javipyGrammarLexer import javipyGrammarLexer
from gen.javipyGrammarParser import javipyGrammarParser
from gen.javipyGrammarVisitor import javipyGrammarVisitor
from antlr4.error.ErrorListener import ErrorListener


class JaviPyConverter(javipyGrammarVisitor):

    def __init__(self):
        self.indentation_level = 0
        self.output = ""
        self.fields = []
        self.has_constructor = False
        self.has_main = False
        self.current_class = ""
        self.locals = []  # na deklaracje zmiennych
        self.objects = []  # na obiekty klasy

    def indent(self):
        self.indentation_level += 1

    def dedent(self):
        self.indentation_level -= 1
        if self.indentation_level < 0:
            self.indentation_level = 0

    def get_indent(self):
        return "    " * self.indentation_level

    def visitProgram(self, ctx):
        for child in ctx.children:
            self.visit(child)
        return self.output

    def visitImport_statement(self, ctx):
        self.output += "import "
        identifiers = ctx.IDENTIFIER()
        for i, identifier in enumerate(identifiers):
            if i > 0:
                self.output += "."
            self.output += identifier.getText()
        self.output += "\n"

    def visitClass_declaration(self, ctx):
        self.output += f"{self.get_indent()}"
        class_name = ctx.IDENTIFIER().getText()
        self.current_class = class_name
        self.output += f"class {class_name}:\n"
        self.has_main = False
        self.has_constructor = False
        class_body_ctx = ctx.class_body()

        self.indent()
        self.visitClass_body(class_body_ctx)
        if class_body_ctx is None:
            self.output += f"{self.get_indent()}pass\n"
        self.dedent()
        self.current_class = ""

        if self.has_main:
            self.output += f"\n{self.get_indent()}"
            self.output += f"if __name__ == '__main__':\n"
            self.indent()
            self.output += f"{self.get_indent()}"
            self.output += f"{class_name}.main()"
            self.dedent()

    def visitClass_body(self, ctx):
        for child in ctx.children:
            if isinstance(child, javipyGrammarParser.Field_declarationContext):
                self.visit(child)
            elif isinstance(child, javipyGrammarParser.ConstructorContext):
                self.has_constructor = True
                self.visit(child)

        if not self.has_constructor and self.fields:
            self.output += f"{self.get_indent()}def __init__(self):\n"
            self.indent()
            for field, value in self.fields:
                self.output += f"{self.get_indent()}self.{field} = {value}\n"
            self.output += "\n"
            self.dedent()

        for child in ctx.children:
            if isinstance(child, javipyGrammarParser.Method_declarationContext):
                identifier = child.IDENTIFIER().getText()
                if identifier.lower() == "main":
                    self.has_main = True
                self.visit(child)

    # check
    def visitField_declaration(self, ctx):
        identifier = ctx.IDENTIFIER().getText()
        assignment = self.visit(ctx.literal()) if ctx.literal() else "None"
        self.fields.append((identifier, assignment))
        self.locals.append(identifier)

    def visitMethod_declaration(self, ctx):
        identifier = ctx.IDENTIFIER().getText()
        parameters = self.visit(ctx.parameter_list()) if ctx.parameter_list() else ""
        is_static = "static" in ctx.getText()
        decorator = "@staticmethod\n" if is_static else ""
        if is_static:
            if identifier.lower() == "main":
                self.output += f"{self.get_indent()}{decorator}"
                self.output += f"{self.get_indent()}def main():\n"
            else:
                self.output += f"{self.get_indent()}{decorator}"
                self.output += f"{self.get_indent()}def {identifier}({parameters}):\n"
        else:
            self.output += f"{self.get_indent()}"
            self.output += f"def {identifier}(self, {parameters}):\n" if parameters else f"def {identifier}(self):\n"
        self.indent()
        self.visit(ctx.block())
        self.dedent()
        self.locals.clear()
        self.locals += [pair[0] for pair in self.fields]
        self.output += "\n"

    # check
    def visitConstructor(self, ctx):
        parameters = ", " + self.visit(ctx.parameter_list()) if ctx.parameter_list() else ""
        block = self.visit(ctx.block())
        self.output += f"def __init__(self{parameters}) {block}\n"

    # check
    def visitLiteral(self, ctx):
        literal_map = {
            "true": "True",
            "false": "False",
            "null": "None"
        }
        literal = ctx.getText()
        return literal_map.get(literal, literal)

    # check
    def visitParameter_list(self, ctx):
        parameters = [self.visit(param) for param in ctx.parameter()]
        return ", ".join(parameters)

    # check
    def visitParameter(self, ctx):
        identifier = ctx.IDENTIFIER().getText()
        self.locals.append(identifier)
        return f"{identifier}"

    # check
    def visitArgument_list(self, ctx):
        arguments = [self.visit(arg) for arg in ctx.argument()]
        return ", ".join(arguments)

    # check
    def visitArgument(self, ctx):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.expression():
            return self.visit(ctx.expression())
        else:
            return ctx.IDENTIFIER().getText()

    def visitBlock(self, ctx):
        for child in ctx.children:
            self.visit(child)

    def visitStatement(self, ctx):
        for child in ctx.children:
            self.visit(child)

    def visitBlock_statement(self, ctx):
        for child in ctx.children:
            self.visit(child)

    def visitLocal_variable(self, ctx):
        identifier = ctx.IDENTIFIER().getText()
        self.locals.append(identifier)

    def visitAssignment(self, ctx):
        this_prefix = "self." if ctx.THIS() else ""
        identifier = ctx.IDENTIFIER()[0].getText()

        if ctx.data_type():
            self.locals.append(identifier)

        if identifier not in self.locals:
            raise ConversionError(f"variable '{identifier}' not found")

        if ctx.function_call():
            assignment_value = self.visitFunction_call(ctx.function_call(), is_assign=True)
        elif ctx.expression():
            assignment_value = self.visit(ctx.expression())
        elif ctx.literal():
            assignment_value = self.visit(ctx.literal())
        elif ctx.IDENTIFIER():
            assignment_value = ctx.IDENTIFIER()[1].getText()

        if not isinstance(ctx.parentCtx, javipyGrammarParser.For_statementContext):
            self.output += f"{self.get_indent()}{this_prefix}{identifier} = {assignment_value}\n"
        return f"{this_prefix}{identifier} = {assignment_value}"

    def visitClass_object(self, ctx):
        class_name = ctx.IDENTIFIER(0).getText()
        identifier = ctx.IDENTIFIER(1).getText()  # ExampleClass example = new ExampleClass();
        self.objects.append(identifier)
        arguments = self.visit(ctx.argument_list()) if ctx.argument_list() else ""
        self.output += f"{self.get_indent()}"
        self.output += f"{identifier} = {class_name}({arguments})\n"

    def visitExpression(self, ctx):
        return self.visitChildren(ctx)

    # check
    def visitLogical_expression(self, ctx):
        if len(ctx.logical_term()) == 1:
            return self.visit(ctx.logical_term(0))
        else:
            left = self.visit(ctx.logical_term(0))
            operator = self.visit(ctx.logical_operator(0))
            right = self.visit(ctx.logical_term(1))
            result = f"{left} {operator} {right}"
            for i in range(1, len(ctx.logical_operator())):
                operator = self.visit(ctx.logical_operator(i))
                right = self.visit(ctx.logical_term(i + 1))
                result = f"({result}) {operator} {right}"
            return result

    def visitLogical_term(self, ctx):
        result = ""
        if ctx.NOT():
            result += "not "
        if ctx.IDENTIFIER():
            result += ctx.IDENTIFIER().getText()
            if ctx.IDENTIFIER().getText() not in self.locals:
                raise ConversionError(f"variable '{ctx.IDENTIFIER().getText()}' not found")
        elif ctx.LEFTPAREN():
            result += f"({self.visit(ctx.logical_expression())})"
        elif ctx.literal():
            result += self.visit(ctx.literal())
        else:
            result += self.visit(ctx.arithmetic_expression())
        return result

    def visitLogical_operator(self, ctx):
        operator_map = {
            "&&": "and",
            "||": "or"
        }
        operator = ctx.getText()
        return operator_map.get(operator, operator)

    # check
    def visitArithmetic_expression(self, ctx):
        terms = [self.visit(ctx.arithmetic_term(i)) for i in range(len(ctx.arithmetic_term()))]
        operators = [self.visit(ctx.arithmetic_operator(i)) for i in range(len(ctx.arithmetic_operator()))]
        result = terms[0]
        for i in range(1, len(terms)):
            result += f" {operators[i - 1]} {terms[i]}"
        return result

    def visitArithmetic_term(self, ctx):
        if ctx.LEFTPAREN():
            return f"({self.visit(ctx.arithmetic_expression())})"
        elif ctx.IDENTIFIER():
            if ctx.IDENTIFIER().getText() not in self.locals:
                raise ConversionError(f"variable '{ctx.IDENTIFIER().getText()}' not found")
            return ctx.IDENTIFIER().getText()
        elif ctx.literal():
            return self.visit(ctx.literal())

    def visitArithmetic_operator(self, ctx):
        if ctx.compare_operator():
            return self.visit(ctx.compare_operator())
        else:
            return ctx.getText()

    def visitCompare_operator(self, ctx):
        return ctx.getText()

    # check
    def visitIf_statement(self, ctx):
        self.output += f"{self.get_indent()}if {self.visit(ctx.expression())}:\n"
        self.indent()
        self.visit(ctx.block())
        self.dedent()

        for elseif in ctx.elseif_statement():
            self.visit(elseif)

        if ctx.else_statement():
            self.visit(ctx.else_statement())
        self.output += "\n"

    def visitElseif_statement(self, ctx):
        self.output += f"{self.get_indent()}elif {self.visit(ctx.if_statement().expression())}:\n"
        self.indent()
        self.visit(ctx.if_statement().block())
        self.dedent()

        for elseif in ctx.if_statement().elseif_statement():
            self.visit(elseif)

        if ctx.if_statement().else_statement():
            self.visit(ctx.if_statement().else_statement())

    def visitElse_statement(self, ctx):
        self.output += f"{self.get_indent()}else:\n"
        self.indent()
        self.visit(ctx.block())
        self.dedent()

    # check
    def visitSwitch_case_statement(self, ctx):
        switch_variable = ctx.IDENTIFIER().getText()
        switch_cases = [self.visit(switch_case_ctx) for switch_case_ctx in ctx.switch_block().switch_case()]

        if switch_variable not in self.locals:
            raise ConversionError(f"variable '{switch_variable}' not found")

        self.output += f"\n{self.get_indent()}if {switch_variable} == {switch_cases[0]}:\n"
        self.indent()
        self.case_statements(ctx.switch_block().switch_case(0))
        self.dedent()

        for case in switch_cases[1:]:
            self.output += f"{self.get_indent()}elif {switch_variable} == {case}:\n"
            self.indent()
            self.case_statements(ctx.switch_block().switch_case(switch_cases.index(case)))
            self.dedent()

        self.visitDefault_case(ctx.switch_block().default_case())
        self.dedent()
        self.output += "\n"

    def case_statements(self, ctx):
        statements = [self.visit(statement_ctx) for statement_ctx in ctx.statement() if
                      statement_ctx.getText() != "break;"]
        statements = [statement for statement in statements if statement is not None]
        if statements:
            self.output += "\n".join(statements) + "\n"

    def visitSwitch_case(self, ctx):
        case_value = ctx.NUMBER().getText() if ctx.NUMBER() else ctx.TEXT().getText()
        return case_value

    def visitDefault_case(self, ctx):
        self.output += f"{self.get_indent()}else:\n"
        self.indent()
        self.case_statements(ctx)

    def visitLoop_statement(self, ctx):
        return self.visit(ctx.getChild(0))

    # check
    def visitFor_condition(self, ctx):
        identifier1 = ctx.IDENTIFIER(0).getText()
        operator = self.visit(ctx.compare_operator())
        identifier2_or_number = ctx.IDENTIFIER(1).getText() if ctx.IDENTIFIER(1) else ctx.NUMBER().getText()
        return f"{identifier1} {operator} {identifier2_or_number}"

    def visitInc_dec(self, ctx):
        identifier = ctx.IDENTIFIER().getText()
        operator = "+= 1" if ctx.INCREMENT() else "-= 1"
        self.output += f"{self.get_indent()}{identifier} {operator}\n"
        if identifier not in self.locals:
            raise ConversionError(f"variable '{identifier}' not found")

    def visitFor_statement(self, ctx):
        init = self.visit(ctx.assignment())
        condition = self.visit(ctx.for_condition())

        init_parts = init.split(' = ')
        loop_var = init_parts[0]
        start = init_parts[1]

        cond_parts = condition.split(' ')
        operator = cond_parts[1]
        end = cond_parts[2]

        if operator == "<=":
            end_int = int(end) + 1
        else:
            end_int = int(end)

        self.output += f"{self.get_indent()}for {loop_var} in range({start}, {end_int}):\n"
        self.indent()
        self.visit(ctx.block())
        self.dedent()

    # check
    def visitWhile_statement(self, ctx):
        condition = self.visit(ctx.while_condition())
        self.output += f"{self.get_indent()}while {condition}:\n"
        self.indent()
        self.visit(ctx.block())
        self.dedent()

    def visitWhile_condition(self, ctx):
        if ctx.for_condition():
            return self.visit(ctx.for_condition())
        elif ctx.expression():
            return self.visit(ctx.expression())
        elif ctx.IDENTIFIER():
            if ctx.IDENTIFIER().getText() not in self.locals:
                raise ConversionError(f"variable '{ctx.IDENTIFIER().getText()}' not found")
            return ctx.IDENTIFIER().getText()
        elif ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.TRUE():
            return "True"
        elif ctx.FALSE():
            return "False"
        else:
            raise ValueError("Unexpected while condition")

    # check
    def visitTry_catch_statement(self, ctx):
        self.output += f"{self.get_indent()}try:\n"
        self.indent()
        self.visit(ctx.block())
        self.dedent()
        for catch_ctx in ctx.catch_statement():
            self.visitCatch_statement(catch_ctx)

    def visitCatch_statement(self, ctx):
        exception_mapping = {
            "NullPointerException": "AttributeError",
            "IndexOutOfBoundsException": "IndexError",
            "IllegalArgumentException": "ValueError",
            "ClassCastException": "TypeError",
            "ArithmeticException": "ZeroDivisionError"
        }

        exception = ctx.IDENTIFIER(0).getText()
        exception_id = ctx.IDENTIFIER(1).getText()

        python_exception = exception_mapping.get(exception, "Exception")
        self.output += f"{self.get_indent()}except {python_exception} as {exception_id}:\n"
        self.indent()
        self.visit(ctx.block())
        self.dedent()

    def visitPrint_statement(self, ctx):
        print_terms = self.visit(ctx.print_term())
        self.output += self.get_indent()
        self.output += f"print({print_terms})\n"

    def visitPrint_term(self, ctx):
        terms = []
        if ctx.TEXT():
            text = ctx.TEXT().getText().strip('"')
            terms.append(f'"{text}"')
        if ctx.expression():
            expression = self.visit(ctx.expression())
            if expression in [field for field, _ in self.fields]:
                terms.append(f"self.{expression}")
            else:
                terms.append(expression)
        if ctx.IDENTIFIER():
            identifiers = [identifier.getText() for identifier in ctx.IDENTIFIER()]
            for identifier in identifiers:
                if identifier in [field for field, _ in self.fields]:
                    terms.append(f"self.{identifier}")
                else:
                    terms.append(identifier)
                if identifier not in self.locals:
                    raise ConversionError(f"variable '{identifier}' not found")
        return ", ".join(terms)

    def visitReturn_statement(self, ctx):
        result = ""
        if ctx.expression():
            result += self.visit(ctx.expression())
        elif ctx.literal():
            result += self.visit(ctx.literal())
        elif ctx.IDENTIFIER():
            result += ctx.IDENTIFIER().getText()
            if ctx.IDENTIFIER().getText() not in self.locals:
                raise ConversionError(f"variable '{ctx.IDENTIFIER().getText()}' not found")

        self.output += f"{self.get_indent()}return {result}\n"

    def visitBreak_statement(self, ctx):
        self.output += f"{self.get_indent()}break\n"

    def visitContinue_statement(self, ctx):
        self.output += f"{self.get_indent()}continue\n"

    def visitFunction_call(self, ctx, is_assign=False):
        identifiers = ctx.IDENTIFIER()
        if len(identifiers) == 2:
            object_name = identifiers[0].getText()
            function_name = identifiers[1].getText()

            if object_name not in self.objects:
                raise ConversionError(f"object '{object_name}' not found")

        else:
            object_name = self.current_class
            function_name = identifiers[0].getText()

        arguments = self.visit(ctx.argument_list()) if ctx.argument_list() else ""
        function_call_code = f"{object_name}.{function_name}({arguments})"

        if is_assign:
            return function_call_code
        else:
            self.output += f"{self.get_indent()}{function_call_code}\n"


class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError(f"line {line}:{column} {msg}")


def convert(input_text):
    input_stream = InputStream(input_text)
    lexer = javipyGrammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = javipyGrammarParser(token_stream)
    error_listener = ThrowingErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    try:
        tree = parser.program()
        converter = JaviPyConverter()
        result = converter.visit(tree)
        return result
    except RecognitionException as e:
        raise ConversionError(str(e))
    except Exception as e:
        raise ConversionError(str(e))


class ConversionError(Exception):
    pass


