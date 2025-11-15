# Zad. 3.
# Mając podana listę ulic w danej dzielnicy i wiedząc, że na każdej ulicy znajduje się 5 bloków
# mieszkalnych, a w każdym z nich jest 10 lokali, wypisz listę wszystkich adresów w dzielnicy.
# Lista ulic w dzielnicy:
# • Jagodowa,
# • Lipowa,
# • Kwiatowa,
# • Kasztanowa,
# • Polna.

lista_ulic = ['Jagodowa', 'Lipowa', 'Kwiatowa', 'Kasztanowa', 'Polna']


def wypisz_liste_ulic(lista_ulic, liczba_blokow, liczba_mieszkan):
    adresy = []
    for ulica in lista_ulic:
        for i in range(1, liczba_blokow + 1):
            for j in range(1, liczba_mieszkan + 1):
                adresy.append(f"{ulica} {i}/{j}")
    print(adresy)

wypisz_liste_ulic(lista_ulic, 5, 10)
