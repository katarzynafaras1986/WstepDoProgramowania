# Zad. 8
# Wyświetl z łańcucha tekst ="Python jest super" znaki o indeksach:
# • Zerowym
# • Ostatnim
# • Co drugi, zaczynając od zerowego
# • Co trzeci zaczynając od pierwszego
# • Od dziesiątego do ostatniego
# • Wyświetl od końca do początku

tekst = "Python jest super"

print("Zerowy znak:", tekst[0])

print("Ostatni znak:", tekst[-1])

print("Co drugi od zerowego:", tekst[0::2])

print("Co trzeci od pierwszego:", tekst[1::3])

print("Od dziesiątego do końca:", tekst[10:])

print("Od końca do początku:", tekst[::-1])
