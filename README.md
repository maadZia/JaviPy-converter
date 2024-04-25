## Teoria Kompilacji i Kompilatory - Projekt
### Autorzy: Amelia Adamczuk, Magdalena Bernat


## JaviPy Java to Python Converter
#### Tokeny:
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
   

```python
def hello_world():
    print("Hello, world!")

hello_world()
```
