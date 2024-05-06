# JaviPy Java to Python Converter
### Teoria Kompilacji i Kompilatory - Projekt
#### Autorzy: Amelia Adamczuk, Magdalena Bernat


## Tokeny:
```md
// literal
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*
NUMBER: '-'? ( '0' | [1-9][0-9]* ) ( '.' [0-9]+ )?
STRING: (".*?"|'.*?')

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
RETURN: 'return'
TRY: 'try'
CATCH: 'catch'

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

// delimiter
SEMICOLON: ';'
LEFTPAREN: '('
RIGHTPAREN: ')'
LEFTBRACKET: '['
RIGHTBRACKET: ']'
LEFTBRACE: '{'
RIGHTBRACE: '}'

COMMENT: '//' ~('\n' | '\r')* '\n'?  | '/*' .*? '*/' -> skip;
NEWLINE: '\n'
WHITESPACE: '\t'
```

## Gramatyka:
```ruby
program             : (class_declaration | function_declaration | statement)*

class_declaration   : 'class' IDENTIFIER ':' INDENT (class_member)* DEDENT
class_member        : function_declaration | attribute_declaration

function_declaration : 'def' IDENTIFIER '(' parameter_list? ')' ':' block

attribute_declaration : IDENTIFIER '=' expression

parameter_list      : IDENTIFIER (',' IDENTIFIER)*

block               : INDENT statement* DEDENT

statement           : expression 
                    | assignment 
                    | conditional 
                    | loop 
                    | return_statement 
                    | print_statement 
                    | COMMENT
                    | try_catch_statement
                    | with_statement
                    | break_statement
                    | continue_statement
                    | pass_statement
                    | import_statement

expression          : term (OPERATOR term)*

term                : IDENTIFIER 
                    | NUMBER 
                    | DECIMAL 
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

with_item           : expression ('as' IDENTIFIER)?

```
