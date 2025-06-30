# mini_project_2_temperature_calculator.py

# Program oceniający temperaturę
# Pobiera temperaturę w stopniach Celsjusza i ocenia zakres

# Pobranie temperatury jako string
temp_input = input("Podaj temperaturę w C: ")
temperature = float(temp_input)  # Konwersja na float dla precyzji

# Instrukcje warunkowe określające przedział temperatury
if temperature < 0:
    print("Mróz.")
elif temperature <= 20:
    print("Chłodno.")
else:
    print("Ciepło.")

# Wskazówka:
# Kolejność warunków ma znaczenie.
# Najpierw sprawdzamy zakresy bardziej szczegółowe (np. <0),
# potem bardziej ogólne (np. <=20), na końcu else.
