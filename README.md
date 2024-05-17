# JaviPy Java to Python Converter
### Teoria Kompilacji i Kompilatory - Projekt
#### Autorzy: Amelia Adamczuk, Magdalena Bernat

***
***
## Założenia projektu
JaviPy to proste w obsłudze narzędzie umożliwiające konwersję kodu źródłowego napisanego w języku Java <br>
na równoważny kod w języku Python, zachowując w pełni jego zgodność i funkcjonalność.
- Język implementacji: Python
- Wykorzystany generator parserów: ANTLR

## Gramatyka
W folderze grammar znajduje się spis wszystkich rozpoznawanych przez nasz konwerter tokenów oraz produkcji gramatycznych języka Java. <br>
Każdy program musi zaczynać się od deklaracji klasy lub enuma, albo opcjonalych importów. W składowe każdej klasy mogą wchodzić <br>
między innymi deklaracje zmiennych i metod z możliwymi modyfikatorami dostępu (public/private/protected/static). W ciele każdej metody, <br>
poza deklaracjami zmiennych, mogą zjadować się np. instrukcje warunkowe, pętle czy wywołania innych metod.

## Drzewa składniowe
Folder img zawiera trzy przykładowe drzewa wygenerowane na podstawie odpowiednich fragmentów kodu z katalogu example, np.: <br>
```java
//code ex1
public static class Main {
        public void main(String[] args) {
            for (int i = 1; i <= 10; i++) {
                System.out.println("wartosc i: " + i);
            }
        }
}
```
![](https://github.com/maadZia/JaviPy-converter/blob/main/img/parseTree1.png)
***
***
