# Zad. 5:
# Napisz skrypt, który pobiera długości boków prostokąta, a następnie oblicza jego pole i
# obwód oraz wyświetla wyniki na ekranie.
def zwaliduj(a):
    if a <= 0:
        print("Proszę podać poprawną długośc dla boku a")
        return False
    return True


def podaj_a():
    try:
        bok_a = int(input(f"Podaj długośc boku a prostokąta:"))
        return bok_a if zwaliduj(bok_a) else podaj_a()
    except ValueError:
        print("Proszę podać poprawną długośc dla boku a")
        return podaj_a()


def podaj_b():
    try:
        bok_b = int(input(f"Podaj długośc boku b prostokąta:"))
        return bok_b if zwaliduj(bok_b) else podaj_b()
    except ValueError:
        print("Proszę podać poprawną długość  dla boku b")
        return podaj_b()


def oblicz(a, b):
    print(f"Pole prostokąta o bokach {a} oraz {b} wynosi {a * b}")
    print(f"Obwód prostokąta o bokach {a} oraz {b} wynosi {2 * (a + b)}")


x = podaj_a()
y = podaj_b()
oblicz(x, y)
