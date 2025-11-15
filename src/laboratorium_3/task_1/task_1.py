# Zad. 1
# Napisz program, który będzie kontrolować zużycie paliwa w samolocie. Przed rozpoczęciem każdej
# jednostki czasu wydrukuj do konsoli informację o pozostałych jednostkach paliwa. Gdy paliwo
# zostanie wyczerpane, wydrukuj do konsoli informacje 'Koniec lotu.'.
# Masz do dyspozycji następujące dane.:
# • ilość paliwa w samolocie w litrach
# • ilość paliwa zużywanego na sekundę w litrach
# • czas lotu w sekunadach
# Wartości początkowe:
# • paliwo = 100
# • paliwo_zużyte_na_s = 10
# • czas = 0

paliwo = 100
paliwo_zuzyte_na_sekunde = 10
czas = 0

while 0 < paliwo:
    czas += 1
    paliwo -= paliwo_zuzyte_na_sekunde
    print(f"Po {czas} sekundach lotu pozostało {paliwo} litrów paliwa")


