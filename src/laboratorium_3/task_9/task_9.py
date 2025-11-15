# Zad. 9
# Napisz programy, które:
# • Wczyta (zmienną) imię oraz wyświetli tekst „Witaj” oraz wczytane imię.
# • Wczyta (zmienną) wiek oraz wyświetli tekst „Twój wiek to: ” oraz wczytany
# wiek.
# • Wczyta (zmienne) imię i nazwisko i wyświetli inicjały.
# • Wczyta łańcuch i wyświetli go pięć razy.
# • Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta połączone te dwa
# łańcuchy.
# • Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta pierwszą połowę

print("Program który wczyta (zmienną) imię oraz wyświetli tekst „Witaj” oraz wczytane imię.")
imie = input("Podaj imię: ")
print("Witaj", imie)

print("Program który wczyta (zmienną) wiek oraz wyświetli tekst „Twój wiek to: ” oraz wczytany wiek.")
wiek = input("Podaj swój wiek: ")
print("Twój wiek to:", wiek)

print("Program który wczyta (zmienne) imię i nazwisko i wyświetli inicjały.")
imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")

inicjaly = imie[0] + nazwisko[0]
print("Twoje inicjały:", inicjaly.upper())

print("Program który wczyta łańcuch i wyświetli go pięć razy")
tekst = input("Podaj tekst: ")

for i in range(5):
    print(tekst)

print("Program który wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta połączone te dwa łańcuchy")
t1 = input("Podaj pierwszy łańcuch: ")
t2 = input("Podaj drugi łańcuch: ")

polaczony = t1 + t2
print("Połączony łańcuch:", polaczony)

print("Program który czyta dwa łańcuchy, a w trzecim łańcuchu zapamięta pierwszą połowę")
t1 = input("Podaj pierwszy łańcuch: ")
t2 = input("Podaj drugi łańcuch: ")

polowa1 = t1[:len(t1) // 2]
polowa2 = t2[:len(t2) // 2]

trzeci = polowa1 + polowa2

print("Nowy łańcuch (połówki):", trzeci)
