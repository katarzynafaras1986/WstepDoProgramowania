# Zadanie 4. Utwórz dwie tablice rozmiaru A = (2,3) oraz B = (3,2). Oblicz iloczyn skalarny tych tablic
# (A@B oraz B@A). Następnie zmień rozmiar tablicy B na (3,3). Czy mnożenia się udały? Jeżeli nie, to
# dlaczego?

import numpy as np

a = np.array([[1, 2,3],
              [4,5,6]])
b = np.array([[1,2],
             [2,3],
             [4,5]])
print(a)
print(b)

print(f"Iloczyn skalarny ab: {a @ b}")
print(f"Iloczyn skalarny ba: {b @ a}")
