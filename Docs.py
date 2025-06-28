"""
Projekt: Prosty kalkulator faktury
Cel: Konwersja string -> float i formatowanie liczb za pomocą f-string.
"""

# Dane wejściowe
product_name = "Monitor LCD"
price_net = "399.99"

# Konwersja ceny na float
price_net_float = float(price_net)

# Obliczenie ceny brutto (23% VAT)
price_gross = price_net_float * 1.23

# Wyświetlenie raportu
print("--- FAKTURA ---")
print(f"Produkt: {product_name}")
print(f"Cena netto: {price_net_float:.2f} PLN")
print(f"Cena brutto (23% VAT): {price_gross:.2f} PLN")

"""
Cheat-sheet:
- float("123.45") konwertuje tekst na liczbę zmiennoprzecinkową.
- {zmienna:.2f} wyświetla liczbę z dokładnością do dwóch miejsc po przecinku.
- Jeśli cena w cudzysłowie, musisz ją przekonwertować przed działaniami.
"""