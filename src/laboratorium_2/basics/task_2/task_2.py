# Zad. 2
# Napisz program porządkowania trzech liczb x, y i z. Od najmniejszej do największej, bez użycia
# wbudowanych funkcji
x=input("liczba 1")
y=input("liczba 2")
z=input("liczba 3")

def uporzadkuj_liczby(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a

    print(f"Liczby w kolejności rosnącej: {a}, {b}, {c}")

uporzadkuj_liczby(x,y,z)
