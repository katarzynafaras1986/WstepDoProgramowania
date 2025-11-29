# Zad. 1
# Utwórz listę: Moja_lista=[1, 17, 3, 5, 3, 4, 86, 90, 2, 21], przetestuj działanie wszystkich
# zaprezentowanych operacji na listach, a ich wynik wyświetl w konsoli.

moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]
moja_lista2 = [181, 66, 36]

print('Pierwszy element: ', moja_lista[0])
print('Ostatni element: ', moja_lista[-1])
print('Długośc listy: ', len(moja_lista))
print('Największa wartość: ', max(moja_lista))
print('Najmniejsza wartość: ', min(moja_lista))
print('Posortowana: ', sorted(moja_lista))
moja_lista.append(40)
print('Z dodanym elementem: ', moja_lista)
print('Z dodanym elementem w indexie 5: ', moja_lista.insert(5, 50))
print('Ostatni zwrócony element: ', moja_lista.pop())
moja_lista.reverse()
print('Odwrócona lista: ', moja_lista)
moja_lista3 = moja_lista + moja_lista2
print('Połączona lista 2 i 3: ', moja_lista3)
moja_lista4 = moja_lista + moja_lista2
print('Połączenie listy 1 i 2 pięciokrotnie: ', moja_lista4 * 5)
print('Od początku do elementu 5: ', moja_lista[:5])
print('Od elementu o inexie 5 do końca: ', moja_lista[5:])
print('Zakres elementów 2-8 z krokiem 2: ', moja_lista[2:8:2])
print('Odwrócenie listy: ', moja_lista[::-1])
