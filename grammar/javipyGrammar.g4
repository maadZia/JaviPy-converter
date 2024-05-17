grammar javipyGrammar;


program             : (import_statement)* declaration+;

import_statement    : IMPORT IDENTIFIER (DOT IDENTIFIER)* SEMICOLON;
declaration         : access? (class_declaration | enum_declaration);

enum_declaration    : ENUM IDENTIFIER LEFTBRACE enum_body RIGHTBRACE;
enum_body           : IDENTIFIER (COMMA IDENTIFIER)*;

class_declaration   : CLASS IDENTIFIER LEFTBRACE class_body RIGHTBRACE;
class_body          : (field_declaration | method_declaration | constructor | enum_declaration)*;

field_declaration   : access? STATIC? data_type IDENTIFIER (ASSIGN literal)? SEMICOLON;
method_declaration  : access? STATIC? type IDENTIFIER LEFTPAREN parameter_list? RIGHTPAREN block;
constructor         : access? IDENTIFIER LEFTPAREN parameter_list? RIGHTPAREN block;

access              : PUBLIC | PRIVATE | PROTECTED;

data_type           : INT | FLOAT | STRING | BOOLEAN | IDENTIFIER;
type                : VOID | data_type;
literal             : NUMBER | TEXT | TRUE | FALSE | NULL;
parameter_list      : parameter (COMMA parameter)*;
parameter           : data_type (LEFTBRACKET RIGHTBRACKET)? IDENTIFIER;
argument_list       : argument (COMMA argument)*;
argument            : literal | IDENTIFIER;

block               : LEFTBRACE (statement SEMICOLON | block_statement)* RIGHTBRACE;

statement           : local_variable
                    | assignment
                    | print_statement
                    | return_statement
                    | break_statement
                    | continue_statement
                    | function_call;

block_statement     : if_statement
                    | switch_case_statement
                    | loop_statement
                    | try_catch_statement;

local_variable      : data_type IDENTIFIER (LEFTBRACKET RIGHTBRACKET)?;
assignment          : data_type? (THIS DOT)? IDENTIFIER ASSIGN (literal | IDENTIFIER
                    | arithmetic_expression | class_object | enum_object);

class_object        : NEW IDENTIFIER LEFTPAREN argument_list? RIGHTPAREN;
enum_object         : IDENTIFIER DOT IDENTIFIER;

expression          : logical_expression | arithmetic_expression;

logical_expression  : logical_term (logical_operator logical_term)*;
logical_term        : NOT? (LEFTPAREN logical_expression RIGHTPAREN | IDENTIFIER | literal | arithmetic_expression);

logical_operator    : OR | AND;

arithmetic_expression : arithmetic_term (arithmetic_operator arithmetic_term)*;
arithmetic_term     : LEFTPAREN arithmetic_expression RIGHTPAREN | IDENTIFIER | literal;

arithmetic_operator : PLUS
                    | MINUS
                    | MULTIPLY
                    | DIVIDE
                    | compare_operator;

compare_operator    : LESSTHAN
                    | LESSOREQ
                    | MORETHAN
                    | MOREOREQ
                    | EQUAL
                    | NOTEQUAL;


if_statement        : IF LEFTPAREN expression RIGHTPAREN block (else_statement)*;
else_statement      : ELSE if_statement;

switch_case_statement : SWITCH LEFTPAREN IDENTIFIER RIGHTPAREN LEFTBRACE switch_block RIGHTBRACE;
switch_block        : (switch_case)* default_case;
switch_case         : CASE (IDENTIFIER | TEXT) COLON (statement SEMICOLON)+;
default_case        : DEFAULT COLON (statement SEMICOLON)+;

loop_statement      : for_statement | while_statement;

for_statement       : FOR LEFTPAREN assignment SEMICOLON for_condition SEMICOLON for_iteration RIGHTPAREN block;
for_condition       : IDENTIFIER compare_operator (IDENTIFIER | NUMBER);
for_iteration       : IDENTIFIER (INCREMENT | DECREMENT);

while_statement     : WHILE LEFTPAREN while_condition RIGHTPAREN block;
while_condition     : for_condition | expression | IDENTIFIER | NUMBER | TRUE | FALSE;

try_catch_statement : TRY block (catch_statement)+;
catch_statement     : CATCH LEFTPAREN data_type IDENTIFIER RIGHTPAREN block;

print_statement     : (PRINT | PRINTLN) LEFTPAREN print_term RIGHTPAREN;
print_term          : TEXT (PLUS (IDENTIFIER | LEFTPAREN expression RIGHTPAREN))?
                    | IDENTIFIER (COMMA IDENTIFIER)*
                    | expression;

return_statement    : RETURN (IDENTIFIER | literal)?;
break_statement     : BREAK;
continue_statement  : CONTINUE;

function_call       : (IDENTIFIER DOT)? IDENTIFIER LEFTPAREN argument_list? RIGHTPAREN;




// type
VOID: 'void';
INT: 'int';
FLOAT: 'float';
STRING: 'String';
BOOLEAN: 'boolean';

// keyword
CLASS: 'class';
ENUM: 'enum';
PUBLIC: 'public';
PRIVATE: 'private';
PROTECTED: 'protected';
STATIC: 'static';
NEW: 'new';
FOR: 'for';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
BREAK: 'break';
SWITCH: 'switch';
CASE: 'case';
DEFAULT: 'default';
CONTINUE: 'continue';
RETURN: 'return';
TRY: 'try';
CATCH: 'catch';
IMPORT: 'import';
PRINT: 'System.out.print';
PRINTLN: 'System.out.println';

// operator
PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
ASSIGN: '=';
EQUAL: '==';
NOTEQUAL: '!=';
LESSTHAN: '<';
LESSOREQ: '<=';
MORETHAN: '>';
MOREOREQ: '>=';
OR: '||';
AND: '&&';
NOT: '!';
INCREMENT: '++';
DECREMENT: '--';

// delimiter
SEMICOLON: ';';
COLON: ':';
LEFTPAREN: '(';
RIGHTPAREN: ')';
LEFTBRACKET: '[';
RIGHTBRACKET: ']';
LEFTBRACE: '{';
RIGHTBRACE: '}';
COMMA: ',';
DOT: '.';

// literal
NUMBER: '-'? ( '0' | [1-9][0-9]* ) ( '.' [0-9]+ )?;
TEXT: '"' (.*?) '"';
THIS: 'this';
NULL: 'null';
TRUE: 'true';
FALSE: 'false';
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

COMMENT: ('//' ~('\n' | '\r')* '\n'?  | '/*' .*? '*/') -> skip;
WHITESPACE: [ \t\r\n]+ -> skip;