# Zad 8.
# Stwórz program, który wykorzystując operator wycinania z podanego ciąg znaków (zmienna text)
# wyodrębni:
# pierwsze trzy znaki
# ostatnie dwa znaki
# text = 'Studiuje-Informatykę'
# Wynik wydrukuj do konsoli.

text = "Studiuje-Informatykę"

def wyodrebnij_znaki(text):
    print(f"Pierwsze 3 znaki: {text[0:3]}")
    print(f"Ostatnie 2 znaki: {text[-2:]}")

wyodrebnij_znaki(text)
