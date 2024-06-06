# JaviPy Java to Python Converter
### Teoria Kompilacji i Kompilatory - Projekt
#### Autorzy: Amelia Adamczuk, Magdalena Bernat
<img src="https://github.com/maadZia/JaviPy-converter/blob/main/static/javiPy2.png" width="400"/>

***
***
## Założenia projektu
JaviPy to proste w obsłudze narzędzie umożliwiające konwersję kodu źródłowego napisanego w języku Java <br>
na równoważny kod w języku Python, zachowując w pełni jego zgodność i funkcjonalność.
- Język implementacji: Python
- Wykorzystany generator parserów: ANTLR

## Gramatyka
W folderze grammar znajduje się spis wszystkich rozpoznawanych przez nasz konwerter tokenów oraz wybranych produkcji gramatycznych języka Java.
Każdy program musi zaczynać się od deklaracji klasy lub opcjonalych importów. W składowe każdej klasy mogą wchodzić <br>
między innymi deklaracje zmiennych i metod z możliwymi modyfikatorami dostępu (public/private/protected/static). W ciele każdej metody, <br>
poza deklaracjami zmiennych, mogą zjadować się np. instrukcje warunkowe, pętle czy wywołania innych metod. <br>
> [javipyGrammar](https://github.com/maadZia/JaviPy-converter/blob/main/grammar/javipyGrammar.g4)

## Drzewa składniowe
Folder example/img zawiera cztery przykładowe drzewa wygenerowane na podstawie odpowiednich fragmentów kodu z katalogu example/code, np.: <br><br>
ex1.java
```java
public class Main {
        public static void main(String[] args) {
            for (int i = 1; i <= 10; i++) {
                System.out.println("wartosc i: " + i);
            }
        }
}
```
parseTree1.png
![](https://github.com/maadZia/JaviPy-converter/blob/main/example/img/parseTree1.png)

## Instrukcja obsługi
> [how to use](https://github.com/maadZia/JaviPy-converter/blob/main/instructions/instruction.md)

***
***
