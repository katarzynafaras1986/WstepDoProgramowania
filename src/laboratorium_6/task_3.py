# Zadanie 3. Utwórz tablice a = np.array([1, 2, 3, 4]) b = np.array([10, 20, 30, 40]). Pomnóż je element
# po elemencie oraz wyznacz iloczyn skalarny (dot product). (Wskazówka: a*b, a @ b lub np.dot(a,b)).
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(f"Tablica pierwsza: {a}")
print(f"Tablica druga: {b}")

wymnozone = a * b

print(f"wymnozone: {wymnozone}")

iloczyn_skalarny = a @ b

print(f"iloczyn skalarny: {iloczyn_skalarny}")