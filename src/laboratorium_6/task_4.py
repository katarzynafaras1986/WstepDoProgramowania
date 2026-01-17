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

c = np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])
print(f"Iloczyn skalarny ac: {a @ c}")
print(f"Iloczyn skalarny ca: {c @ a}")

# Można wymnożyć a * c natomiast c * a nie można ponieważ iloczyn skalarny 2 tablic wymnaża wiersz przez kolumne,
# a po zmianie kolumn na 3 nie jest w stanie wymnożyć 2 pozycji z wiersza pierwszej tabeli z 3 pozycjami z kolumny drugiej tabeli.
