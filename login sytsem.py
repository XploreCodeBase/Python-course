# mini_login_system.py
# Prosty system logowania użytkownika do panelu administracyjnego

# Pytamy użytkownika o nazwę konta.
# Funkcja input() zawsze zwraca tekst, dlatego stosujemy metodę .lower(),
# aby porównanie było odporne na wielkość liter (np. "Admin", "ADMIN", "admin").
login = input("Podaj nazwę użytkownika: ").lower()

# Instrukcja warunkowa sprawdza, czy login jest równy "admin"
if login == "admin":
    # Jeśli login to admin, wyświetlamy informację o pełnym dostępie.
    print("Witaj, administratorze! Masz pełen dostęp.")

# elif sprawdza kolejny warunek - czy login to "moderator"
elif login == "moderator":
    # Jeśli login to moderator, informujemy o ograniczonym dostępie.
    print("Witaj, moderatorze! Masz ograniczony dostęp.")

# else zostanie wykonane wtedy, gdy żaden z poprzednich warunków nie pasuje
else:
    # Jeśli login jest inny, informujemy użytkownika o braku uprawnień.
    print("Brak uprawnień do panelu administracyjnego.")

# Przykładowe działanie programu:
# Podaj nazwę użytkownika: Admin
# Witaj, administratorze! Masz pełen dostęp.
#
# Podaj nazwę użytkownika: moderator
# Witaj, moderatorze! Masz ograniczony dostęp.
#
# Podaj nazwę użytkownika: gosciu
# Brak uprawnień do panelu administracyjnego.

# WSKAZÓWKA:
# Jeśli nie zastosujesz .lower(), porównanie będzie czułe na wielkość liter.
# Wtedy wpisanie "Admin" nie zadziała, bo Python rozróżnia małe i wielkie litery.