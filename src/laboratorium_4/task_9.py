# Zad 9.
# Stwórz listę zakupów jako słownik (artykuł : kwota). Wyświetl go i podsumuj wydatki.

lista_zakupow = {"chleb" : 10, "jajka": 15, "mleko": 11, "masło": 10, "banany": 20, "woda": 5}

print("Lista zakupów: ", lista_zakupow)

wydatki = sum(cena for cena in lista_zakupow.values())

print("Wydatki: ", wydatki)