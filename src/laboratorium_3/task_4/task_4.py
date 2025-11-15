# Zad 4. dodatkowe
# Zamówiłeś w restauracji z grupą x przyjaciół, n potraw (liczbę zamówionych dań i liczbę gości, za
# każdym razem wskazuje użytkownik), następnie dla każdej potrawy podajesz jej cenę.
# Korzystając z pętli while napisz program, który pozwoli obliczyć średnią cenę zamówionej potrawy.
# Podziel sprawiedliwe rachunek miedzy wszystkich gości.

def podaj_liczbe(czego):
    try:
        return int(input(f"Podaj liczbę {czego}:"))
    except ValueError:
        print(f"Proszę podać poprawnie liczbę {czego}.")
        return podaj_liczbe(czego)


def podaj_cene(numer_dania):
    try:
        return float(input(f"Podaj cenę dania nr:{numer_dania}:"))
    except ValueError:
        print(f"Proszę podać poprawnią cenę")
        return podaj_cene(numer_dania)


liczba_gosci = podaj_liczbe("gości")
liczba_zamówionych_dan = podaj_liczbe('zamówionych dań')


def policz_koszty_zamowien(liczba_gosci, liczba_zamówionych_dan):
    numer_dania = 1
    cena = 0
    while numer_dania <= liczba_zamówionych_dan:
        cena += podaj_cene(1)
        numer_dania += 1
    print(f"Łączna kwota rachunku: {cena:.2f} zł")
    print(f"Srednia cena: {cena / liczba_zamówionych_dan:.2f} zł")
    print(f"Za osobę: {cena / liczba_gosci:.2f} zł")


policz_koszty_zamowien(liczba_gosci, liczba_zamówionych_dan)
