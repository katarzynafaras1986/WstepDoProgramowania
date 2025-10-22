def podaj_a():
    try:
        liczba_a = float(input(f"Podaj liczbę wymierną a w formacie dziesiętnym:"))
        return liczba_a
    except ValueError:
        print("Proszę podać poprawnie liczbę wymierną w formacie dziesiętnym")
        return podaj_a()


def podaj_b():
    try:
        liczba_b = float(input(f"Podaj liczbę wymierną b w formacie dziesiętnym:"))
        return liczba_b
    except ValueError:
        print("Proszę podać poprawnie liczbę wymierną w formacie dziesiętnym")
        return podaj_b()


x = podaj_a()
y = podaj_b()


def rozwiaz_rownanie(a, b):
    if a == 0:
        if b == 0:
            print(f"Dla a równego {a}, oraz b równego {b}, występuje nieskończenie wiele rozwiązań")
        else:
            print(f"Dla a równego {a}, oraz b równego {b}, nie ma rozwiązania - sprzeczność")
    else:
        print(f"Dla a równego {a}, oraz b równego {b}, x~{-b / a}")


rozwiaz_rownanie(x, y)
