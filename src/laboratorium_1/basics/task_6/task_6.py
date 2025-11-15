# Zad. 6:
# Napisz skrypt, który pobiera od użytkownika drogę pokonaną przez samochód oraz
# średnie spalanie (w litrach na 100 km) i wyświetli informację o przewidywanym zużyciu
# paliwa oraz o szacowanych kosztach podróży (cena paliwa 6.5 zł/l).
# A) Zmodyfikuj skrypt tak, aby długość przejechanej drogi była generowana losowo
# (liczba całkowita z zakresu ), a użytkownik podawał aktualną cenę paliwa za litr.
# B) Zmodyfikuj zadania 6 tak, aby wyświetlanie wyników wykorzystywało f-string.
def zwaliduj(a):
    if a <= 0:
        print("Proszę podać poprawną liczbę")
        return False
    return True


def podaj_odleglosc():
    try:
        odleglosc = int(input(f"Podaj odległość do pokonania w kilometrach:"))
        return odleglosc if zwaliduj(odleglosc) else podaj_odleglosc()
    except ValueError:
        print("Proszę podać odleglosc w poprawnym formacie")
        return podaj_odleglosc()


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


odleglosc = podaj_odleglosc()
srednie_spalanie = podaj_srednie_spalanie()
oblicz_zuzycie(odleglosc, srednie_spalanie)
