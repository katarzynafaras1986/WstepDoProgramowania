# Zadanie 5.
# Napisz funkcję zmieniającą miejscami dwa elementy listy wraz z obsługą wyjątków.
# Wymagania
# 1. Funkcja przyjmuje listę oraz indeksy.
# 2. Działa in-place (modyfikacja istniejącej listy)
# 3. Obsługuje ujemne indeksy
# 4. Wyrzuca:
# a. ValueError, gdy lista jest pusta
# b. TypeError, gdy argumenty mają niewłaściwe typy
# c. IndexError, gdy indeksy wychodzą poza zakres
# 5. (Dla chętnych – napisanie testów przy pomocy biblioteki pytest)
def zamien_miejscami_elementy_listy(lista, inex1, index2):
    if len(lista) == 0:
        raise ValueError("Lista nie może być pusta")
    if isinstance(inex1, int):
        raise TypeError("Index1 musi być intem")
    if isinstance(index2, int):
        raise TypeError("Index2 musi być intem")
    buffer = lista[inex1]
    lista[inex1] = lista[index2]
    lista[index2] = buffer
    if index1 len(lista) == 0:
