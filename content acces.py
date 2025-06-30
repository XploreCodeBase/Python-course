# mini_project_5_age_status_access.py

# Program kontrolujący dostęp w zależności od wieku i statusu konta

# Pobranie wieku i konwersja
age_input = input("Podaj wiek: ")
age = int(age_input)

# Pobranie statusu
status = input("Podaj status konta (premium/standard): ").lower()

# Logika decyzyjna
if age >= 18 and status == "premium":
    print("Masz pełen dostęp do wszystkich funkcji.")
elif age >= 18 and status == "standard":
    print("Masz ograniczony dostęp.")
else:
    print("Brak dostępu.")

# Wyjaśnienie:
# - Warunek if wymaga spełnienia dwóch kryteriów (and)
# - elif sprawdza inny wariant dla pełnoletnich
# - else obsługuje pozostałe przypadki
# - .lower() ułatwia porównania tekstu
