# Zad. 6
# Napisz pętlę nieskończoną, w której użytkownik podaje liczby całkowite. W przypadku liczby ujemnej,
# następuję wyjście z pętli.

def podaj_liczbe_calkowita():
    try:
        return int(input(f"Podaj liczbę całkowitą: "))
    except ValueError:
        print(f"Proszę podać poprawnie liczbę całkowitą.")
        return podaj_liczbe_calkowita()


while True:
    liczba = podaj_liczbe_calkowita()
    if liczba < 0:
        break
