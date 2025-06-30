# mini_project_4_number_validator.py

# Program weryfikujący czy dane wejściowe to liczba
# Obsługuje brak danych i sytuacje, gdy wpis nie jest liczbą

# Pobranie danych od użytkownika
user_input = input("Podaj liczbę: ")

# Sprawdzenie, czy użytkownik wpisał cokolwiek
if user_input == "":
    print("Brak danych.")
# Sprawdzenie, czy wpis zawiera tylko cyfry
elif user_input.isdigit():
    # Konwersja na int, bo mamy pewność, że to liczba całkowita
    number = int(user_input)
    doubled = number * 2
    print(f"Podwojona wartość: {doubled}")
else:
    # Obsługa sytuacji, gdy użytkownik podał tekst lub inne znaki
    print("Nie można wykonać obliczeń, ponieważ to nie jest liczba całkowita.")

# Wskazówka:
# - .isdigit() sprawdza, czy tekst zawiera wyłącznie cyfry (bez minusów i kropek)
# - Jeśli planujesz obsługiwać liczby ujemne lub zmiennoprzecinkowe,
#   potrzebujesz bardziej zaawansowanych metod (o tym w kolejnych lekcjach)
