"""
Mini-projekt: System powitań
Cel: przećwiczenie różnych metod formatowania tekstu w funkcji print()
"""

# Zmienna tekstowa z imieniem użytkownika
user_name = "Kamil"

# Zmienna tekstowa z miastem użytkownika
user_city = "Warszawa"

# Zmienna liczbową z liczbą logowań
login_count = 5

# 1. Formatowanie za pomocą przecinków
# Przecinki automatycznie dodają spację i konwertują liczby na tekst
print("Witaj", user_name, "z miasta", user_city + ".", "Odnotowaliśmy", login_count, "logowań.")

# 2. Formatowanie za pomocą operatora +
# Wszystkie fragmenty muszą być typu string
# Dlatego liczby konwertujemy za pomocą str()
print("Witaj " + user_name + " z miasta " + user_city + ". Odnotowaliśmy " + str(login_count) + " logowań.")

# 3. Przykład problemu: próba połączenia tekstu z liczbą bez konwersji
# Odkomentuj poniższą linię, aby zobaczyć błąd TypeError
# print("Witaj " + user_name + " z miasta " + user_city + ". Odnotowaliśmy " + login_count + " logowań.")

"""
Przypomnienie:
- Przecinki w print() automatycznie konwertują liczby na string i dodają spacje.
- Operator + wymaga, aby wszystkie elementy były typu str – w przeciwnym razie program zgłosi błąd.
- Funkcja str() zamienia liczby na tekst, np. str(5) => "5".
"""
