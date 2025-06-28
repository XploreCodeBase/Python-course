# Dane wejściowe
user_id = "1001"
subscription_fee = "49.99"

# Konwersja typów
user_id_int = int(user_id)
subscription_fee_float = float(subscription_fee)

# Sprawdzenie, czy opłata jest większa od 0
is_valid = subscription_fee_float > 0

# Wyświetlanie wyników przy użyciu tradycyjnego formatowania
print("ID użytkownika:", user_id_int)
print("Typ ID:", type(user_id_int))

print("Opłata abonamentowa:", subscription_fee_float)
print("Typ opłaty:", type(subscription_fee_float))

print("Czy opłata jest poprawna?", is_valid)
print("Typ walidacji:", type(is_valid))