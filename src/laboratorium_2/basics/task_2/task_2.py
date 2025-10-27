# Zad. 2
# Napisz program porządkowania trzech liczb x, y i z. Od najmniejszej do największej, bez użycia
# wbudowanych funkcji

def podaj_liczbe(nazwa_liczby):
    try:
        liczba_a = float(input(f"Podaj liczbę wymierną \"{nazwa_liczby}\" w formacie dziesiętnym:"))
        return liczba_a
    except ValueError:
        print("Niepoprawna liczba!")
        return podaj_liczbe(nazwa_liczby)


x = podaj_liczbe("a")
y = podaj_liczbe("b")
z = podaj_liczbe("c")


def uporzadkuj_liczby(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a

    print(f"Liczby w kolejności rosnącej: {a}, {b}, {c}")


uporzadkuj_liczby(x, y, z)
