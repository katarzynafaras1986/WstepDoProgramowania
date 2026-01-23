# Zadanie 1. Wczytaj plik CSV. Dodaj kolumnę marża = (sprzedaż - koszt) / sprzedaż. Posortuj po rok i po
# kraj rosnąco
import pandas as pd

df = pd.read_csv("dane.csv", sep=';') # otwieranie pliku

df['Marża'] = (df['Sprzedaż'] - df['Koszt']) / df['Sprzedaż']

df_posortowane = df.sort_values(by=['Rok', 'Kraj'], ascending=True)

print(df_posortowane)