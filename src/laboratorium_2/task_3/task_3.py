# Zad. 3
# Zmienna Nazwa_pliku przechowującej jego nazwę.
# Sprawdź, czy plik o podanej nazwie jest z rozszerzeniem '.xlsx'.
# Nazwa_pliku= 'Raport_maj.xlsx'
# Wydrukuj do konsoli 'Tak' jeśli to prawda, przeciwnie 'Nie'.
# Podpowiedz:
# Skorzystaj z metody endswith (jest to metodą wbudowaną dla obiektów typu str w Pythonie),
# sprawdza ona, czy ciąg znaków (Nazwa_pliku) kończy się podanym sufiksem (w tym przypadku
# '.xlsx').

nazwa_pliku = "Raport_maj.xlsx"

def sprawdz_rozszerzeanie(nazwa_pliku, rozszerzenie):
    if nazwa_pliku.split(".")[1] == rozszerzenie:
        print("Tak")
    else:
        print("Nie")

sprawdz_rozszerzeanie(nazwa_pliku, "xlsx")
