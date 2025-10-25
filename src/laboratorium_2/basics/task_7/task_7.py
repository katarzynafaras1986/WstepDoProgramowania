# Zad 7. Podana jest poniższa zmienna przechowująca ciąg znaków - hasło:
# Hasło = 'pk47!jy0893'
# Sprawdź, czy podane hasło ma wymaganą długość 11 znaków oraz zwiera znak specjalny '!'. Jeżeli
# tak, wydrukuj do konsoli „Hasło jest poprawne”, w przeciwnym razie „Hasło jest nie poprawne”.
# Operator wycicnania:
# sekwencja[start:stop:step]
# WSTĘP DO PROGRAMOWANIA – LAB. 2
# start (opcjonalny): Indeks początkowy, od którego zaczyna się wycinek. Element o tym indeksie
# jest włączony do wyniku. Domyślnie start wynosi 0.
# stop (opcjonalny): Indeks końcowy, do którego wycinek jest pobierany, ale ten element nie jest
# już włączony do wyniku. Domyślnie stop to długość sekwencji.
# step (opcjonalny): Krok, z jakim pobierane są elementy. Domyślnie wynosi 1, co oznacza, że
# elementy są pobierane kolejno. Ustawienie go na -1 pozwala odwrócić sekwencję.
# Wycinanie części listy
# lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # Wyciągnięcie elementów od indeksu 2 do 5 (nie włącznie)
# podlista = lista[2:5]
# print(podlista) # Wynik: [2, 3, 4]
# # Pominięcie indeksu 'stop'
# podlista = lista[5:] # Od 5-tego indeksu do końca
# print(podlista) # Wynik: [5, 6, 7, 8, 9]
# # Ostatnie trzy elementy
# podlista = lista[-3:]
# print(podlista) # Wynik: [7, 8, 9]
# # Odwrócenie listy za pomocą ujemnego kroku
# podlista = lista[::-1]
# print(podlista) # Wynik: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # Co drugi element z zakresu od 1 do 8
# podlista = lista[1:8:2]
# print(podlista) # Wynik: [1, 3, 5, 7]
