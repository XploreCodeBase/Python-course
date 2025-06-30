# mini_project_3_permission_check.py

# Program sprawdzający uprawnienia i status konta
# Użytkownik podaje login oraz status

# Pobranie loginu
login = input("Podaj nazwę użytkownika: ").lower()

# Pobranie statusu
status = input("Podaj status konta (aktywny/nieaktywny): ").lower()

# Sprawdzenie warunków z operatorami and/or
if login == "admin" and status == "aktywny":
    print("Pełny dostęp przyznany.")
elif status == "aktywny":
    print("Dostęp ograniczony.")
else:
    print("Brak uprawnień.")

# Wyjaśnienie:
# - .lower() gwarantuje, że porównanie nie zależy od wielkości liter
# - if sprawdza oba warunki naraz
# - elif działa, gdy użytkownik nie jest adminem, ale konto jest aktywne
# - else obsługuje wszystkie pozostałe sytuacje
