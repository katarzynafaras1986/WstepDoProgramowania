# Zadanie 1. Wczytaj plik CSV. Dodaj kolumnę marża = (sprzedaż - koszt) / sprzedaż. Posortuj po rok i po
# kraj rosnąco
import pandas as pd

df = pd.read_csv("dane.csv", sep=';') # otwieranie pliku

df['Marża'] = (df['Sprzedaż'] - df['Koszt']) / df['Sprzedaż']

df_posortowane = df.sort_values(by=['Rok', 'Kraj'], ascending=True)

print(df_posortowane)

# Zadanie 2. Zwróć rekordy dla DE w latach >= 2023 i tylko kolumny sprzedaż i marża.

wynik = df_posortowane.loc[
    (df_posortowane['Kraj'] == 'DE') & (df_posortowane['Rok'] >= 2023),
    ['Sprzedaż', 'Marża']
]

# Wyświetlenie wyników dla roku 2026 i lat ubiegłych
print(wynik)
