# JaviPy Java to Python Converter
### Teoria Kompilacji i Kompilatory - Projekt
#### Autorzy: Amelia Adamczuk, Magdalena Bernat

***
***
## Założenia projektu
JaviPy to proste w obsłudze narzędzie umożliwiające konwersję kodu źródłowego napisanego w języku Java <br>
na równoważny kod w języku Python, zachowując w pełni jego zgodność i funkcjonalność.

## Tokeny:
```antlr
// literal
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*
NUMBER: '-'? ( '0' | [1-9][0-9]* ) ( '.' [0-9]+ )?
STRING: (".*?"|'.*?')
NULL: 'null'

// type
VOID: 'void'
INT: 'int'
FLOAT: 'float'
STRING: 'string'
BOOLEAN: 'boolean'

// keyword
CLASS: 'class'
FOR: 'for'
IF: 'if'
ELSE: 'else'
WHILE: 'while'
BREAK: 'break'
CONTINUE: 'continue'
RETURN: 'return'
TRY: 'try'
CATCH: 'catch'
IMPORT: 'import'

// operator
PLUS: '+'
MINUS: '-'
MULTIPLY: '*'
DIVIDE: '/'
ASSIGN: '='
EQUAL: '=='
NOTEQUAL: '!='
LESS: '<'
LESSOREQ: '<='
MORE: '>'
MOREOREQ: '>='
OR: '||'
AND: '&&'
NOT: '!'

// delimiter
SEMICOLON: ';'
LEFTPAREN: '('
RIGHTPAREN: ')'
LEFTBRACKET: '['
RIGHTBRACKET: ']'
LEFTBRACE: '{'
RIGHTBRACE: '}'
COMMA: ','

COMMENT: ('//' ~('\n' | '\r')* '\n'?  | '/*' .*? '*/') -> skip;
NEWLINE: '\n'
WHITESPACE: '\t'
```

## Gramatyka:
```antlr
program             : (import_statement)* declaration+

import_statement    : IMPORT IDENTIFIER (DOT IDENTIFIER)* SEMICOLON
declaration         : class_declaration | enum_declaration

enum_declaration    : ENUM IDENTIFIER LEFTBRACE enum_body RIGHTBRACE
enum_body           : IDENTIFIER (COMMA IDENTIFIER)*

class_declaration   : CLASS IDENTIFIER LEFTBRACE class_body RIGHTBRACE
class_body          : (field_declaration | method_declaration | constructor)*

field_declaration   : type IDENTIFIER (ASSIGN literal)? SEMICOLON
method_declaration  : type IDENTIFIER LEFTPAREN parameter_list? RIGHTPAREN block
constructor         : IDENTIFIER LEFTPAREN parameter_list? RIGHTPAREN block

type                : VOID | INT | FLOAT | STRING | BOOLEAN
literal             : NUMBER | STRING | TRUE | FALSE | NULL
parameter_list      : parameter (COMMA parametr)*
parameter           : type_specifier IDENTIFIER

block               : LEFTBRACE (statement SEMICOLON)* RIGHTBRACE
statement           : assignment
                      | expression  
                      | if_statement 
                      | loop_statement
                      | try_catch_statement
                      | print_statement
                      | return_statement
                      | break_statement
                      | continue_statement
                      | function_call
                      | COMMENT

assignment          : type? IDENTIFIER ASSIGN (literal | IDENTIFIER)

expression          : logical_expression | arithmetic_expression

logical_expression  : logical_term (logical_operator logical_term)*
logical_term        : NOT? (LEFTPAREN logical_expression RIGHTPAREN | IDENTIFIER | literal | arithmetic_expression)
logical_operator    : OR | AND

arithmetic_expression : arithmetic_term (arithmetic_operator arithmetic_term)*
arithmetic_term     : LEFTPAREN arithmetic_expression RIGHTPAREN | IDENTIFIER | literal
arithmetic_operator : PLUS
                      | MINUS
                      | MULTIPLY
                      | DIVIDE
                      | EQUAL
                      | NOTEQUAL
                      | LESS
                      | LESSOREQ
                      | MORE
                      | MOREOREQ

if_statement        :
loop_statement      : for_statement | while_statement
try_catch_statement :
print_statement     :
return_statement    :
break_statement     :
continue_statement  :
funcion_call        :

//dopisac mozliwosc dodawania komentarzy


/*

expression          : term ((PLUS | MINUS | MULTIPLY | DIVIDE | EQUAL | NOTEQUAL | LESS | LESSOREQ | MORE | MOREOREQ | OR | AND) term)*

term                : IDENTIFIER 
                    | NUMBER 
                    | STRING 
                    | '(' expression ')'
                    | function_call

assignment          : IDENTIFIER '=' expression

conditional         : 'if' expression ':' block ('elif' expression ':' block)* ('else' ':' block)?

loop                : 'for' IDENTIFIER 'in' expression ':' block
                    | 'while' expression ':' block

return_statement    : 'return' expression

print_statement     : 'print' '(' expression ')'

function_call       : IDENTIFIER '(' argument_list? ')'

argument_list       : expression (',' expression)*

try_catch_statement : 'try' ':' block 'except' IDENTIFIER ':' block
                    | 'try' ':' block 'except' IDENTIFIER 'as' IDENTIFIER ':' block

break_statement     : 'break'

continue_statement  : 'continue'

pass_statement      : 'pass'

import_statement    : 'import' module_name

with_statement      : 'with' with_item (',' with_item)* ':' block
*/

with_item           : expression ('as' IDENTIFIER)?

```
