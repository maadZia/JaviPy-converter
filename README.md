# JaviPy Java to Python Converter
### Teoria Kompilacji i Kompilatory - Projekt
#### Autorzy: Amelia Adamczuk, Magdalena Bernat


## Tokeny:
1. IDENTIFIER
   * '[a-zA-Z_][a-zA-Z0-9_]*'
3. NUMBER
   * '-?\d+'
4. DECIMAL
   * '-?\d+(\.\d+)'
4. STRING
   * '(".?"|'.?')'
5. KEYWORD
   * 'class'
   * 'for'
   * 'if'
   * 'else'
   * 'while'
   * 'break'
   * 'return'
6. TYPE
   * 'void'
   * 'int'
   * 'float'
   * 'boolean'
   * 'string'
7. OPERATOR
   * '+'
   * '-'
   * '*'
   * '/'
   * '='
   * '=='
   * '!='
8. DELIMITER
   * ';' 
   * '{' 
   * '}' 
   * '(' 
   * ')' 
   * ','
9. COMMENT
   * '// komentarz'
   * '/* komentarz */'
10. WHITESPACES
    * '\n'
    * '\t'
   

## Gramatyka:
```python
    program : (class_declaration | function_declaration | statement)*
    class_declaration : 'class' IDENTIFIER ':' INDENT (class_member)* DEDENT
    class_member : function_declaration | attribute_declaration
    function_declaration : 'def' IDENTIFIER '(' parameter_list? ')' ':' block
    attribute_declaration : IDENTIFIER '=' expression
    parameter_list : IDENTIFIER (',' IDENTIFIER)*

    block       : INDENT statement* DEDENT
    statement   : expression | assignment | conditional | loop | return_statement | print_statement | COMMENT
    expression  : term (OPERATOR term)*
    term        : IDENTIFIER | NUMBER | DECIMAL | STRING | '(' expression ')'
    assignment  : IDENTIFIER '=' expression
    conditional : 'if' expression ':' block ('elif' expression ':' block)* ('else' ':' block)?
    loop        : 'for' IDENTIFIER 'in' expression ':' block

    return_statement : 'return' expression
    print_statement : 'print' '(' expression ')'
