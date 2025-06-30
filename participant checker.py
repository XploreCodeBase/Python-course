# mini_project_2_participant_checker.py

# Program, który sprawdza liczbę uczestników i dobiera odpowiednią salę

# Pobieramy dane od użytkownika
participants_input = input("Podaj liczbę uczestników: ")

# Sprawdzamy, czy wpis składa się wyłącznie z cyfr
if participants_input.isdigit():
    # Konwersja tekstu na liczbę
    participants = int(participants_input)

    # Potwierdzenie typu zmiennej
    if isinstance(participants, int):
        # Instrukcje warunkowe wybierające salę
        if participants > 100:
            print("Duża sala została zarezerwowana.")
        else:
            print("Mała sala została zarezerwowana.")
else:
    # Komunikat w przypadku błędnych danych
    print("Niepoprawna liczba uczestników.")

"""
Przykładowy wynik działania:

Podaj liczbę uczestników: 120
Duża sala została zarezerwowana.

Podaj liczbę uczestników: 50
Mała sala została zarezerwowana.

Podaj liczbę uczestników: abc
Niepoprawna liczba uczestników.
"""

# Wskazówka:
# - Najpierw zawsze używaj .isdigit(), dopiero potem konwertuj na int()
# - Dzięki temu program nie przerwie działania błędem
