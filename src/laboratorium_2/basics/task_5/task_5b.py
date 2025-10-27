# zad. 5
# a)
# Odczytaj podany plik notwania_gieldowe.txt zawierający dane dotyczące notowań kilku spółek.
# Wydrukuj każdą linię do konsoli.
# b)
# Dopisz do pliku notwania_gieldowe.txt, w kolejnej linii dane dotyczące nowej spółki: ALR, 113.
# Wydrukuj każdą linię ponownie do konsoli

from pathlib import Path

nazwa_pliku = "notowania_gieldowe.txt"

def znajdz_plik(nazwa_pliku, katalog_startowy="."):
    sciezka_startowa = Path(katalog_startowy)
    for sciezka in sciezka_startowa.rglob(nazwa_pliku):
        return sciezka
    return None

znaleziona_sciezka = znajdz_plik(nazwa_pliku)

if znaleziona_sciezka:
    print(f"Plik '{nazwa_pliku}' znaleziono w: {znaleziona_sciezka}")
    nowy_tekst = "ALR, 113.\n"

    with open(nazwa_pliku, 'a') as plik:
        plik.write("\n" + nowy_tekst)
    with open(znaleziona_sciezka, "r") as f:
        for linia in f:
            print(linia, end='')
else:
    print(f"Plik '{nazwa_pliku}' nie został znaleziony.")
