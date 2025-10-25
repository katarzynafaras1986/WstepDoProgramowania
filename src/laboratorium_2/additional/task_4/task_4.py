# Zad. 4 dodatkowe
# Jesteś menagerem drużyny piłkarskiej i chcesz obliczyć łączny wynik drużyny na podstawie liczby
# strzelonych przez nią bramek i ewentualnie zdobytych dodatkowych punktów. Napisz program,
# który dokona stosownych kalkulacji po wprowadzeniu liczby goli zdobytych przez drużynę.
# Utworzone są dwie zmienne gol i bonus, gdzie gol to liczba całkowita reprezentująca liczbę
# bramek zdobytych przez drużynę, a bonus to liczba całkowita reprezentująca wszelkie możliwe
# punkty bonusowe dla drużyny.
# Następnie użyj instrukcji warunkowej do obliczenia całkowitego wyniku zespołu zgodnie z
# następującymi zasadami:
# - każda zdobyta bramka to 10 punktów,
# - jeśli drużyna zdobędzie więcej niż 5 bramek, zdobywa dodatkowe 5 punktów bonusowych,
# - jeśli drużyna zdobędzie więcej niż 10 bramek, zdobywa dodatkowe 10 punktów bonusowych
# a) Po zdobyciu 5 goli drużyna otrzymuje 5 punktów bonusowych. Jeśli drużyna zdobędzie więcej
# niż 10 goli, to otrzyma za nie 10 punktów bonusowych dodatkowo
# Oblicz całkowity wynik drużyny, dodając punkty zdobyte ze zdobytych bramek i wszelkie
# stosowne punkty bonusowe. Wynik wydrukuj do konsoli.
# b) Punkty bonusowe po przekroczeniu 5 i 10 punktów są sumowane, tzn. po przekroczeniu więcej
# niż 10 bramek drużyna zdobywa obydwa bonusy.
# Oblicz całkowity wynik drużyny, dodając punkty zdobyte ze zdobytych bramek i wszelkie
# stosowne punkty bonusowe. Wynik wydrukuj do konsoli.
# Czytanie zwartości pliku
# Plik możemy otworzyć w jednym z trzech trybów:
# tryb "r" — tryb do czytania pliku (read)
# tryb "w" — tryb do zapisywania danych do pliku (write)
# tryb "a" — tryb do dopisywania zawartości na koniec pliku (append)
# Otwieranie pliku tekstowego
# plik = open("dane.txt", "r") # otwieramy plik w trybie do odczytu (r - read)
# print(plik.read()) # wypisanie zawartości pliku
# plik.close() # zamknięcie pliku
# Funkcja open() otwiera plik dane.txt w trybie do czytania. Obiekt plik zostaje skojarzony z plikiem
# dane.txt i od tego momentu możemy użyć metody read() aby pobrać zawartość pliku i np.
# wyświetlić ją na ekranie monitora.
# WSTĘP DO PROGRAMOWANIA – LAB. 2
# Pamiętaj, że po skończonej pracy na pliku należy go zamknąć metodą close(), w przeciwnym razie
# może to prowadzić do problemów związanych z zasobami i niewłaściwym zwalnianiem pamięci.
# Drugi sposób otwierania pliku w wybranym trybie
# with open("dane.txt", "r") as plik:
#  print(plik.read())
# W powyższym przykładzie używamy bloku with, który automatycznie zarządza zamknięciem pliku
# po zakończeniu bloku. Nie musimy wywoływać metody close(). Blok with jest często używany do
# obsługi plików w Pythonie, ponieważ gwarantuje właściwe zarządzanie zasobami.
# Czytanie pliku wierszami
# with open("dane.txt", "r") as plik:
#  for linia in plik:
#  print(linia)
# Zapisywanie danych do pliku
# with open("out.txt", "w") as plik:
#  plik.write("Ala ma kota")
# with open("out.txt", "r") as plik:
#  print(plik.read()) # Ala ma kota