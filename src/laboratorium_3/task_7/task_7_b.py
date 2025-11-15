# Zad. 7 dodatkowe
# A)
# Grupa laboratoryjna składa się z n studentów (wartość n podaje użytkownik). Wprowadzamy liczbę
# punktów dla każdego studenta.
# Napisz program, który obliczy średnią liczbę punktów w grupie z wykorzystaniem pętli while.
# Zastosuj instrukcje continue w programie tak, aby po podaniu liczby punktów spoza przedziału 0 –
# 100 pomijać dalsze wykonywanie pętli. Sprawdź działanie programu.
# B)
# Następnie zmień pętlę na nieskończoną, czyli taką której warunek zawsze jest prawdziwy. Zakończ
# działanie pętli przy użyciu instrukcji break.
# Obie wersje zadnia proszę zamieścić w sprawozdaniu.

def podaj_liczbe(czego):
    try:
        return int(input(f"Podaj liczbę {czego}:"))
    except ValueError:
        print(f"Proszę podać poprawnie liczbę {czego}.")
        return podaj_liczbe(czego)


# B
def policz_srednia_b():
    liczba_studentow = podaj_liczbe('studentów')
    liczba_wszystkich_punktow = 0
    licznik = 1
    while True:
        liczba_punktow_studenta = podaj_liczbe('punktów studenta nr: ' + str(licznik))
        if liczba_punktow_studenta > 100 or liczba_punktow_studenta < 0:
            continue
        liczba_wszystkich_punktow += liczba_punktow_studenta
        fraza = "studenta" if licznik == 1 else "studentów"
        print(f"Średnia liczba punktów dla {licznik} {fraza} to {liczba_wszystkich_punktow / licznik:.2f}")
        licznik += 1
        if licznik == liczba_studentow + 1:
            break


policz_srednia_b()
