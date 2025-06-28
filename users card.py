"""
Projekt: Karta użytkownika
Cel: Pokazanie konwersji string -> int i float oraz użycia f-string.
"""

# Dane wejściowe jako tekst
user_name = "Anna Kowalska"
user_age = "28"
user_balance = "150.00"

# Przypomnienie:
# Jeśli zmienna jest w cudzysłowie, Python traktuje ją jako tekst (str).
# Aby używać jej w obliczeniach, trzeba ją przekonwertować.

# Konwersja typów
user_age_int = int(user_age)          # Konwersja na int
user_balance_float = float(user_balance)  # Konwersja na float

# Dodanie bonusu
bonus = 10
new_balance = user_balance_float + bonus

# Wyświetlenie raportu
print("--- KARTA UŻYTKOWNIKA ---")
print(f"Imię i nazwisko: {user_name}")
print(f"Wiek: {user_age_int} lat")
print(f"Saldo początkowe: {user_balance_float:.2f} PLN")
print(f"Saldo po bonusie: {new_balance:.2f} PLN")

"""
Cheat-sheet:
- int("25") zamienia tekst na liczbę całkowitą.
- float("12.5") zamienia tekst na liczbę zmiennoprzecinkową.
- f-string pozwala łączyć tekst i zmienne w jednej linii.
- {wartość:.2f} formatuje liczbę do 2 miejsc po przecinku.
"""
