# Zad. 2.
# Napisz program, który wydrukuje do konsoli 10 pierwszych liczb pierwszych rozdzielonych
# przecinkiem tak jak pokazano poniżej.
# Pamiętaj, że liczba pierwsza - to taka liczba naturalna, która ma dokładnie dwa dzielniki naturalne:
# jedynkę i samą siebie.
# W rozwiązaniu użyj pętli while oraz instrukcji break
# Oczekiwany wynik:
# 2,3,5,7,11,13,17,19,23,29
ilosc_liczb_pierwszych = 10

def czy_liczba_pierwsza(liczba):
    if liczba <= 1:
        return False
    for i in range(2, int(liczba ** 0.5) + 1):
        if liczba % i == 0:
            return False
    return True


def wypisz_n_liczb_pierwszych(ilosc_liczb_pierwszych):
    liczby_pierwsze = []
    liczba = 0
    while ilosc_liczb_pierwszych > 0:
        if czy_liczba_pierwsza(liczba):
            liczby_pierwsze.append(liczba)
            ilosc_liczb_pierwszych -= 1
        liczba += 1
    print(liczby_pierwsze)


wypisz_n_liczb_pierwszych(10)
