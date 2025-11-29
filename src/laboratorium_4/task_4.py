# Zad. 4 dodatkowe
# Napisz program, który wczyta od użytkownika zdanie. Wypisz z niego wszystkie litery w kolejności
from traceback import format_tb

zdanie = input("Podaj zdanie: ")

zdanie_jako_lista = list(zdanie)

zdanie_jako_lista = [element for element in zdanie_jako_lista if not element.isdigit() and len(element.strip()) != 0]

print("Lista bez cyfr: ", zdanie_jako_lista)

print(zdanie_jako_lista)

zdanie_jako_lista.sort()

litery_alfabetu =  set(zdanie_jako_lista)

print("Litery: ", litery_alfabetu)

alfabet = {"a", "b", "c", "d", "e", "f", "g", "h", 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

nowa_lista = [element for element in alfabet if element not in litery_alfabetu]

print("Alfabet bez liter użytych w zdaniu: ", nowa_lista)