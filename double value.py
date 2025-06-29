"""
Projekt: Kalkulator podwojonej wartości
Cel: Pokazanie użycia input(), konwersji float i formatowania wyniku
"""

# Pobieramy dane od użytkownika
# input() zawsze zwraca tekst (str), nawet jeśli wpiszesz liczbę
user_input = input("Podaj liczbę: ")

# Konwersja string -> float
# Jeśli użytkownik wpisze coś innego niż liczba, program zgłosi błąd
# (np. ValueError przy wpisaniu "abc")
number = float(user_input)

# Obliczamy podwojoną wartość
double_value = number * 2

# Wyświetlamy wynik sformatowany do dwóch miejsc po przecinku
# Używamy f-string i flagi formatowania
print(f"Podwojona wartość: {double_value:.2f}")

"""
Przypomnienie:
- input() zawsze zwraca str
- float() konwertuje tekst na liczbę zmiennoprzecinkową
- {zmienna:.2f} wyświetla liczbę z dwoma miejscami po przecinku
"""
