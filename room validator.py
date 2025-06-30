# mini_project_1_room_validator.py

# Program, który sprawdza, czy wpisany numer pokoju jest poprawny
# Jeśli użytkownik poda liczbę całkowitą dodatnią, rezerwuje pokój

# Pobieramy dane od użytkownika
room_input = input("Podaj numer pokoju: ")

# Sprawdzamy, czy wpis składa się wyłącznie z cyfr
if room_input.isdigit():
    # Konwersja na liczbę całkowitą
    room_number = int(room_input)

    # Dodatkowe sprawdzenie typu zmiennej (dla treningu)
    if isinstance(room_number, int):
        print(f"Pokój numer {room_number} został zarezerwowany.")
else:
    # Jeśli wpis zawiera inne znaki (np. litery)
    print("Niepoprawny numer pokoju. Spróbuj ponownie.")

"""
Przykładowy wynik działania:

Podaj numer pokoju: 205
Pokój numer 205 został zarezerwowany.

Podaj numer pokoju: 20a
Niepoprawny numer pokoju. Spróbuj ponownie.
"""

# Wskazówka:
# - .isdigit() działa tylko na liczbach dodatnich zapisanych jako cyfry
# - Jeśli wpiszesz '-5' lub '5.5', warunek zwróci False
