# Zadanie 1. Stwórz tablicę 5x5 (wartości od 0 do 24) oraz wyciągnij z niej obramowanie (pierwszy/
# ostatni wiersz i kolumna).
import numpy as np

arr = np.arange(0,25).reshape(5,5)
print(arr)
print(arr[0,:])
print(arr[1:, -1])
print(arr[-1, :-1][::-1])
print(arr[1:-1, 0][::-1])
