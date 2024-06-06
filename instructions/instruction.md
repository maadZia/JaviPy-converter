# Instrukcja obsługi
## IDE
- sklonuj repozytorium:
  > git clone https://github.com/maadZia/JaviPy-converter.git
- otwórz projekt w wybranym IDE obsługującym język Python
- wklej kod wejściowy do pliku example/test.java lub zmień scieżkę do wybranego pliku w main.py
- uruchom plik main.py

Plik main.py pobiera kod zapisany w pliku example/test.java i konwertuje go do pliku output.py. Konwersja będzie możliwa <br>
tylko dla kodu zgodnego z gramatyką zawartą w pliku grammar/javipyGrammar.g4. <br>

![](https://github.com/maadZia/JaviPy-converter/blob/main/instructions/img/instruction1.png)

Jednym z kluczowych aspektów konwertera jest uwzględnienie sprawdzania, czy wszystkie zmienne używane
w kodzie źródłowym zostały odpowiednio zadeklarowane.
Jeśli konwerter stwierdzi, że zmienna została użyta bez wcześniejszej deklaracji, generowany jest komunikat błędu, 
który następnie wyświetlany jest w pliku wyjściowym zamiast przetłumaczonego kodu.

![](https://github.com/maadZia/JaviPy-converter/blob/main/instructions/img/instruction2.png)


## GUI
Aplikacja posiada także prosty w obsłudze interfejs graficzny
- uruchom plik app.py
- przejdź do strony serwera
- wpisz lub wklej kod w pierwsze pole tekstowe
- kliknij przycisk 'convert'
  
![](https://github.com/maadZia/JaviPy-converter/blob/main/instructions/img/instruction3.png)


Obsługa błędów:

<img src="https://github.com/maadZia/JaviPy-converter/blob/main/instructions/img/instruction4.png" width="500"/> <img src="https://github.com/maadZia/JaviPy-converter/blob/main/instructions/img/instruction5.png" width="500"/>

