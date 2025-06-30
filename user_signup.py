# mini_project_1_registration.py

# Program rejestracji nowego użytkownika z weryfikacją wieku
# Użytkownik podaje imię oraz wiek.
# Jeśli wiek < 13 - konto wymaga zgody opiekuna.
# W przeciwnym razie konto jest tworzone.

# Pobranie imienia (string)
name = input("Podaj swoje imię: ")

# Pobranie wieku (string) i konwersja na liczbę
age_input = input("Podaj swój wiek: ")
age = int(age_input)  # Uwaga: int() wymaga, żeby użytkownik podał cyfrę

# Instrukcja warunkowa sprawdzająca wiek
if age < 13:
    print("Konto może zostać utworzone tylko za zgodą opiekuna.")
else:
    # f-string użyty do personalizacji komunikatu
    print(f"Witaj {name}! Twoje konto zostało utworzone.")

# To rozwiązanie pokazuje:
# - input()
# - konwersję na int
# - if / else
# - f-string
