# mini_project_3_score_checker.py

# Program, który ocenia wynik testu i przypisuje ocenę

# Pobieramy dane od użytkownika
score_input = input("Podaj wynik testu: ")

# Sprawdzamy, czy wpis zawiera same cyfry
if score_input.isdigit():
    # Konwersja na int
    score = int(score_input)

    # Potwierdzenie typu
    if isinstance(score, int):
        print("To jest liczba całkowita.")

        # Instrukcje warunkowe oceniające wynik
        if score > 90:
            print("Ocena: bardzo dobry.")
        elif score >= 60:
            print("Ocena: dobry.")
        else:
            print("Ocena: niedostateczny.")
else:
    print("Nieprawidłowy wynik testu.")

"""
Przykładowy wynik działania:

Podaj wynik testu: 95
To jest liczba całkowita.
Ocena: bardzo dobry.

Podaj wynik testu: 70
To jest liczba całkowita.
Ocena: dobry.

Podaj wynik testu: tekst
Nieprawidłowy wynik testu.
"""

# Wskazówka:
# - Kolejność warunków ma znaczenie – zaczynamy od najwyższego progu
# - Sprawdzenie isinstance() po konwersji potwierdza, że zmienna jest typu int
