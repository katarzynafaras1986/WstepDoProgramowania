# Zad. 3
# Napisz program, który:
# a. Wczyta (zmienną) imię oraz wyświetli tekst „Witaj” oraz wczytane imię.
# b. Wczyta (zmienną) wiek oraz wyświetli tekst „Twój wiek to:” oraz wczytany wiek.
# c. Wczyta (zmienne) imię i nazwisko i wyświetli inicjały.
# d. Wczyta łańcuch i wyświetli go pięć razy.
# e. Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta połączone te dwa łańcuchy.
# f. Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta pierwszą połowę pierwszego i drugą połowę
# drugiego

imie = input("Podaj imie: ")

print("Witaj " + imie)

wiek = input("Podaj wiek: ")

print("Twój wiek to: " + wiek)

imie = input("Podaj imie: ")
nazwisko = input("Podaj nazwisko: ")

print("Twoje inicjały: ", imie[0:1].upper(), nazwisko[0:1].upper())

lancuch = input("Podaj lancuch1: ")
lancuch2 = input("Podaj lancuch2: ")

print("5 razy łańcuch: ", lancuch * 5)

lancuch = input("Podaj lancuch1: ")
lancuch2 = input("Podaj lancuch2: ")

print("Połączone łańcuchy 1 i 2: ", lancuch + lancuch2)

print("Połączone połówki: ", lancuch[:len(lancuch) // 2] + lancuch2[:len(lancuch2) // 2])

