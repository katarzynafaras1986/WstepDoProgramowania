# Zad. 2
# Napisz program porządkowania trzech liczb x, y i z. Od najmniejszej do największej, bez użycia
# wbudowanych funkcji
x=input("liczba 1")
y=input("liczba 2")
z=input("liczba 3")

def uporzadkuj_liczby(a,b, c):
    if a < b:
        if b < c:
            print(a,b,c)
        elif b > c:
            print(a,c,b)


    elif y < z:
        if z < x:
            print(x,y,z)

uporzadkuj_liczby(x,y,z)
