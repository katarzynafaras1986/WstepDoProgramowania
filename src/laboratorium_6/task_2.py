# Zadanie 2. Dla macierzy losowej 6×4 (N(0,1)) znajdź: średnią każdej kolumny, indeksy min/max w
# każdej kolumnie.
import numpy as np

rng = np.random.default_rng()
macierz = rng.standard_normal((6, 4))
print(macierz)
print(f"Średnie z kolumn  {macierz.mean(axis=0)}")
print(f"min {macierz.argmin(axis=0)}")
print(f"max {macierz.argmax(axis=0)}")