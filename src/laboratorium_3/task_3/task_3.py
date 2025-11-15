# Zad. 3.
# Mając podana listę ulic w danej dzielnicy i wiedząc, że na każdej ulicy znajduje się 5 bloków
# mieszkalnych, a w każdym z nich jest 10 lokali, wypisz listę wszystkich adresów w dzielnicy.
# Lista ulic w dzielnicy:
# • Jagodowa,
# • Lipowa,
# • Kwiatowa,
# • Kasztanowa,
# • Polna.
# Zad 4. dodatkowe
# Zamówiłeś w restauracji z grupą x przyjaciół, n potraw (liczbę zamówionych dań i liczbę gości, za
# każdym razem wskazuje użytkownik), następnie dla każdej potrawy podajesz jej cenę.
# Korzystając z pętli while napisz program, który pozwoli obliczyć średnią cenę zamówionej potrawy.
# Podziel sprawiedliwe rachunek miedzy wszystkich gości.

lista_ulic = ['Jagodowa', 'Lipowa', 'Kwiatowa', 'Kasztanowa', 'Polna']


def wypisz_liste_ulic(lista_ulic, liczba_blokow, liczba_mieszkan):
    for ulic in lista_ulic:
        for i in range(liczba_blokow + 1):
            for j in range(liczba_mieszkan + 1):
                print(ulic, i, j)


wypisz_liste_ulic(lista_ulic, 5, 10)
