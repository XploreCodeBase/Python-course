"""
Projekt: Statystyki użytkownika
Cel: Konwersja różnych typów danych i formatowanie liczb oraz procentów.
"""

# Dane wejściowe
user_id = "1500"
balance = "10000.5"
conversion = 0.0765  # Liczba zmiennoprzecinkowa

# Konwersje
user_id_int = int(user_id)
balance_float = float(balance)

# Wyświetlenie raportu
print("--- STATYSTYKI UŻYTKOWNIKA ---")
print(f"ID: {user_id_int}")
print(f"Saldo: {balance_float:,.2f} PLN")  # separator tysięcy + 2 miejsca po przecinku
print(f"Współczynnik konwersji: {conversion:.1%}")  # format procentowy

"""
Cheat-sheet:
- {wartość:,.2f} -> separator tysięcy i 2 miejsca po przecinku (np. 10,000.50).
- {wartość:.1%} -> procent z jednym miejscem po przecinku (np. 7.7%).
- int() konwertuje tekst na liczbę całkowitą.
- float() konwertuje tekst na float.
"""
