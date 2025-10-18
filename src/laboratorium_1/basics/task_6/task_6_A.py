import random


def zwaliduj(a):
    if a <= 0:
        print("Proszę podać cenę paliwa w poprawnym formacie")
        return False
    return True

def podaj_cene_paliwa():
    try:
        cena_paliwa = float(input(f"Podaj cenę paliwa:"))
        return cena_paliwa if zwaliduj(cena_paliwa) else podaj_srednie_spalanie()
    except ValueError:
        print("Proszę podać poprawną liczbę")
        return podaj_srednie_spalanie()

def podaj_srednie_spalanie():
    try:
        srednie_spalanie = int(input(f"Podaj średnie spalanie:"))
        return srednie_spalanie if zwaliduj(srednie_spalanie) else podaj_srednie_spalanie()
    except ValueError:
        print("Proszę podać poprawną liczbę")
        return podaj_srednie_spalanie()


def oblicz_zuzycie(a, b):
    wynik = a / 100 * b
    print(
        f"Przewidywane zużycie paliwa dla trasy o długości {a} km, przy średnim spalaniu {b} litrów na 100 kilometrów wynosi {wynik:.2f} litrów")
    print(f"Przewidywany koszt paliwa przy cenie 6.5zł/l wyniesie {wynik * 6.5:.2f}zł")


odleglosc = random.randint(1, 2000)
print(f"Wylosowana długość przejechanej drogi: {odleglosc}")
cena_paliwa = podaj_cene_paliwa()
srednie_spalanie = podaj_srednie_spalanie()
oblicz_zuzycie(odleglosc, srednie_spalanie)
