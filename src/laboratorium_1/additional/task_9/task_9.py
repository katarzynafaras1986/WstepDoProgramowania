# Zad. 9:
# Napisz kalkulator, który wyświetli wyniki dodawania, odejmowania, mnożenia, dzielenia
# i potęgowania 2 liczb podanych przez użytkownika.
def wyswietl_menu():
    print("Wybierz jedną z opcji:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")


def wykonaj_operacje(wybor):
    match wybor:
        case 1:
            operacja_arytmetyczna = "Dodawanie"
            liczba_pierwsza = podaj_liczbe(operacja_arytmetyczna, "pierwszą")
            liczba_druga = podaj_liczbe(operacja_arytmetyczna, "drugą")
            print(liczba_pierwsza + liczba_druga)
        case 2:
            operacja_arytmetyczna = "Odejmowanie"
            liczba_pierwsza = podaj_liczbe(operacja_arytmetyczna, "pierwszą")
            liczba_druga = podaj_liczbe(operacja_arytmetyczna, "drugą")
            print(liczba_pierwsza - liczba_druga)
        case 3:
            operacja_arytmetyczna = "Mnożenie"
            liczba_pierwsza = podaj_liczbe(operacja_arytmetyczna, "pierwszą")
            liczba_druga = podaj_liczbe(operacja_arytmetyczna, "drugą")
            print(liczba_pierwsza * liczba_druga)
        case 4:
            operacja_arytmetyczna = "Dzielenie"
            liczba_pierwsza = podaj_liczbe(operacja_arytmetyczna, "pierwszą")
            liczba_druga = zwaliduj_dzielnik(podaj_liczbe(operacja_arytmetyczna, "drugą"))
            print(liczba_pierwsza / liczba_druga)


def podaj_liczbe(operacja_arytmetyczna, kolejnosc):
    try:
        return float(input(f"{operacja_arytmetyczna}. Podaj {kolejnosc} liczbę wymierną w formacie dziesiętnym:"))
    except ValueError:
        print("Proszę podać poprawnie liczbę wymierną w formacie dziesiętnym")
        return podaj_liczbe(operacja_arytmetyczna, kolejnosc)


def podaj_nr_opcji():
    try:
        wybor = int(input("Podaj numer opcji od 1 do 4): "))
        if wybor > 4 or wybor < 1:
            raise ValueError
        return wybor
    except ValueError:
        print("Proszę podać poprawny numer opcji od 1 do 4")
        return podaj_nr_opcji()


def zwaliduj_dzielnik(dzielnik):
    if dzielnik == 0:
        print("Nie dzielimy przez zero!")
        return zwaliduj_dzielnik(podaj_liczbe("Dzielenie", "drugą"))
    else:
        return dzielnik


wyswietl_menu()
wykonaj_operacje(podaj_nr_opcji())
