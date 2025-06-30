# mini_project_4_number_validator.py

# Program weryfikujący czy dane wejściowe to liczba
# Obsługuje brak danych i sytuacje, gdy wpis nie jest liczbą

# Pobranie danych
user_input = input("Podaj liczbę: ")

# Sprawdzenie, czy użytkownik wpisał cokolwiek
if user_input == "":
    print("Brak danych.")
else:
    # Próba konwersji na int
    try:
        number = int(user_input)
        doubled = number * 2
        print(f"Podwojona wartość: {doubled}")
    except ValueError:
        # Obsługa błędu konwersji, jeśli użytkownik wpisał np. tekst
        print("Nie można wykonać obliczeń.")

# Wskazówka:
# - if user_input == "" sprawdza pusty string
# - try/except zabezpiecza przed ValueError
