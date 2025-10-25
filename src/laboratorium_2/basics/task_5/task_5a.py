# zad. 5
# a)
# Odczytaj podany plik notwania_gieldowe.txt zawierający dane dotyczące notowań kilku spółek.
# Wydrukuj każdą linię do konsoli.
# b)
# Dopisz do pliku notwania_gieldowe.txt, w kolejnej linii dane dotyczące nowej spółki: ALR, 113.
# Wydrukuj każdą linię ponownie do konsoli

nazwa_pliku = "C:\\Users\\73136\\notwania_gieldowe.txt"

with open(nazwa_pliku, "r") as f:
    for linia in f:
        print(linia, end='')

open(nazwa_pliku, "r")