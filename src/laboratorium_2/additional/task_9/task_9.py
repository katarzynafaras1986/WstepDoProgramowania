# Zad 9. dodatkowe
# Napisz skrypt zmieniający wszystkie duże litery małe i na odwrót.
# Podpowiedz: skorzytaj z metody swapcase().

def zmien_wielkosc_liter(text):
    print(f"Text ze zmienioną wilkością liter {text.swapcase()}")


zmien_wielkosc_liter(input(f"Wprowadź tekst do zmiany wielkości liter: "))
