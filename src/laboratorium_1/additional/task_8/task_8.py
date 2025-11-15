# Zad. 8:
# Narysuj schemat blokowy algorytmu i napisz program rozwiązywania rownania
# kwadratowego ax2 + bx + c = 0, gdzie a, b i c są wspołczynnikami podawanymi przez
# uzytkownika.
from math import sqrt


def zwaliduj_a(a):
    if a == 0:
        print(f"To nie jest równanie kwadratowe, podaj liczbę różną od zera")
        return False
    return True


def podaj_a():
    try:
        liczba_a = float(input(f"Podaj liczbę wymierną a w formacie dziesiętnym:"))
        return liczba_a if zwaliduj_a(liczba_a) else podaj_a()
    except ValueError:
        print("Proszę podać poprawnie liczbę wymierną w formacie dziesiętnym")
        return podaj_a()


def podaj_b():
    try:
        liczba_b = float(input(f"Podaj liczbę wymierną b w formacie dziesiętnym:"))
        return liczba_b
    except ValueError:
        print("Proszę podać poprawnie liczbę wymierną w formacie dziesiętnym")
        return podaj_b()


def podaj_c():
    try:
        liczba_c = float(input(f"Podaj liczbę wymierną c w formacie dziesiętnym:"))
        return liczba_c
    except ValueError:
        print("Proszę podać poprawnie liczbę wymierną w formacie dziesiętnym")
        return podaj_c()


x = podaj_a()
y = podaj_b()
z = podaj_c()


def rozwiaz_rownanie(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta == 0:
        print(f"Dla a równego {a}, b równego {b} oraz c ={c}, delta jest równa {delta}, x wynosi {-b / (2 * a)}")
    elif delta > 0:
        print(
            f"Dla a równego {a}, b równego {b} oraz c ={c}, delta jest równa {delta}. x1 wynosi {(-b - sqrt(delta)) / (2 * a)} a x2 wynosi {(-b + sqrt(delta)) / (2 * a)}")
    elif delta < 0:
        print(f"Delta jest równa {delta}. Brak rozwiązań")


rozwiaz_rownanie(x, y, z)
