# Zad 1.
# Napisz prosty program, który na podstawie podanej przez Studenta liczby zdobytych punktów,
# poinformuje go o rezultacie egzaminu.
# Każdy Student, który zdobył powyżej 80 punktów zalicza egzamin w terminie 0
# Studenci którzy otrzymali liczbę punków z przedziału 50-80, mogą poprawić jego wynik.
# Studenci, którzy zdobyli poniżej 50 punktów, muszą go poprawić.

def podaj_liczbe_punktow():
    try:
        liczba_a = int(input(f"Podaj liczbę zdobytych punktów:"))
        return liczba_a
    except ValueError:
        print("Proszę podać poprawnie liczbę punktow")
        return podaj_liczbe_punktow()

liczba_punktow = podaj_liczbe_punktow()

if liczba_punktow > 80:
    print("Zaliczasz egzamin w terminie 0")
elif liczba_punktow < 80 and liczba_punktow > 50:
    print("Możesz poprawić  wynik")
elif liczba_punktow < 50:
    print("Musisz poprawić wynik")
