# Zadanie 3.
# Napisz funkcję, która zwraca listę tylko z liczbami parzystymi. Funkcja przyjmuje dowolną ilość
# argumentów. Wykorzystaj funkcję filter oraz lambda.

def wypisz_tylko_liczby_parzyste(*args):
    return  list(filter(lambda x: x % 2 == 0, list(filter(lambda x: isinstance(x, int) or isinstance(x, float), args))))

print(wypisz_tylko_liczby_parzyste(1,2,3,4,5))
print(wypisz_tylko_liczby_parzyste(1,2,3,4,"cos"))
