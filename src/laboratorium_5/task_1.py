# Zadanie 1.
# Napisz funkcję, która oblicza pierwiastki funkcji kwadratowej. Funkcja przyjmuje argumenty a,b,c,
# które są współczynnikami funkcji kwadratowej. Dla a=0, napisz wyjątek, gdy funkcja nie jest
# kwadratowa. Skorzystaj z biblioteki math. Napisz dokumentację tej funkcji, kiedy jest co obliczane itp.
from math import sqrt

def oblicz_pierwiastki_funkcji(a,b,c):
    """
    Przyjmuje 3 liczby jako argumenty.

    Args:
        a (int/float): Pierwsza liczba.
        b (int/float): Druga liczba.
        c (int/float): Trzecia liczba.

    Raises:
        ValueError: "A nie może być równe zero"

    Returns:
        string: Wynik obliczenia pierwiastków funkcji kwadratowej.
    """
    zwaliduj_a(a)
    rozwiaz_rownanie(a,b,c)

def zwaliduj_a(a):
    if a == 0:
        print(f"Dla a równego {a}, b równego {b} oraz c równego {c} - To nie jest równanie kwadratowe, podaj liczbę różną od zera")
        raise ValueError("A nie może być równe zero")
    return True

def rozwiaz_rownanie(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta == 0:
        print(f"Dla a równego {a}, b równego {b} oraz c równego {c}, delta jest równa {delta}, x wynosi {-b / (2 * a)}")
    elif delta > 0:
        print(
            f"Dla a równego {a}, b równego {b} oraz c równego {c}, delta jest równa {delta}. x1 wynosi {(-b - sqrt(delta)) / (2 * a)} a x2 wynosi {(-b + sqrt(delta)) / (2 * a)}")
    elif delta < 0:
        print(f"Dla a równego {a}, b równego {b} oraz c równego {c}, delta jest równa {delta}. Brak rozwiązań")

oblicz_pierwiastki_funkcji(1,2,3)
oblicz_pierwiastki_funkcji(1,-5,6)
oblicz_pierwiastki_funkcji(0,2,3)





