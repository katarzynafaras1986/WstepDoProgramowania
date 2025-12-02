# Zad. 4 dodatkowe
# Napisz program, który wczyta od użytkownika zdanie. Wypisz z niego wszystkie litery w kolejności
#-*-coding: utf-8-*-

zdanie = input("Podaj zdanie: ")

zdanie_jako_lista = list(zdanie.lower())

zdanie_jako_lista = [element for element in zdanie_jako_lista if element.isalpha() and len(element.strip()) != 0]

print("Lista bez cyfr i pustych znaków: ", zdanie_jako_lista)

zdanie_jako_lista =  dict.fromkeys(zdanie_jako_lista)

zdanie_jako_lista = list(zdanie_jako_lista)

print("Bez powtórzeń: ", zdanie_jako_lista)

zdanie_jako_lista.sort()

print("Posortowane alfabetycznie", zdanie_jako_lista)

alfabet = {"a", "ą", "b", "c", "ć", "d", "e", "ę", "f", "g", "h", 'i', 'j', 'k', 'l', 'ł','m', 'n', 'ń','o', 'ó', 'p', 'q', 'r', 's', 'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ź', 'ż'}

nowa_lista = [element for element in alfabet if element not in zdanie_jako_lista]

nowa_lista.sort()

print("Alfabet bez liter użytych w zdaniu: ",  nowa_lista)