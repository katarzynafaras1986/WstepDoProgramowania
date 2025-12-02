# Stwórz listę z imionami 4 osób.
# a. Posortuj ją alfabetycznie i wyświetl,
# b. Dodaj na końcu dwie osoby i pobierz ostatnią z nich poleceniem pop().
# c. Na pozycji 3 dodaj jeszcze jedną osobę.
# d. Odwróć kolejność na liście i zduplikuj ją.
lista_z_imionami = ["Kasia", "Ewelina", "Kuba", "Krzysio", "Bartuś"]
print("Lista z imionami: ", lista_z_imionami)
lista_z_imionami.sort()
print("Lista posortowana: ", lista_z_imionami)
lista_z_imionami.append("Marcin")
lista_z_imionami.append("Piotrek")
print("Lista z dodanymi 2 osobami: ", lista_z_imionami)
print("Ostatnia osoba popem: ", lista_z_imionami.pop())
lista_z_imionami.insert(2, "Marek", )
print("Lista z dodaną osobą \"Marek\" na pozycji trzeciej 2: ", lista_z_imionami)
lista_z_imionami.reverse()
print("Odwrócona: ", lista_z_imionami)
print("Zduplikowana: ", lista_z_imionami*2)