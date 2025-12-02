# Zad 8.
# Załóżmy, że pracujesz nad systemem wojskowym dotyczącym planowania operacji wojskowych.
# Podana jest poniższa krotka:
# stopnie = (
#  "Szeregowy",
#  "Kapral",
#  "Sierżancie",
#  "Porucznik",
#  "Kapitan",
#  "Major",
#  "Pułkownik",
# )
# Wykonaj poniższe kroki:
# - wyznacz liczbę wszystkich stopni wojskowych i przypisz do zmiennej ilość_stopnii,
# - znajdź indeks krotki dla elementu "Major" i przypisz do zmiennej Major_index,
# - sprawdź, czy wartość "Pułkownik" znajduje się w krotce stopnie i przypisz do zmiennej
# Pułkownik_wstepowanie.
# W wydrukuj otrzymane zmienne do konsoli w podanej kolejności.

stopnie = (
 "Szeregowy",
 "Kapral",
 "Sierżancie",
 "Porucznik",
 "Kapitan",
 "Major",
 "Pułkownik",
)

ilosc_stopni = len(stopnie)

print("ilosc_stopni: ", ilosc_stopni)

major_index = stopnie.index("Major")

print("major_index: ", major_index)

pulkownik_wstepowanie = "Pułkownik" in stopnie

print("pulkownik_wstepowanie: ", pulkownik_wstepowanie)

