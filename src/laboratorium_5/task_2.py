# Zadanie 2.
# Napisz funkcję, która będzie tworzyć profil użytkownika z obowiązkowym imieniem oraz adresem
# email i dowolnymi dodatkowymi informacjami (min. 3). Funkcja zwraca słownik zawierający
# wszystkie dane profilu. Wykorzystaj funkcję isinstance() oraz strip().

def utworz_profil_uzytkownika(**kwargs):
    if len(kwargs) < 5:
        raise ValueError("Musisz podać minimum 3 dodastkowe argumenty.")
    if 'email' not in kwargs or 'imie' not in kwargs:
        raise ValueError("Musisz podać obowiązkowe argumenty: 'email' i 'imie'.")
    imie_raw = kwargs['imie'].strip()
    email_raw = kwargs['email'].strip()

    if not isinstance(imie_raw, str):
        raise TypeError("imie must be a string")
    if not isinstance(email_raw, str):
        raise TypeError("email must be a string")

    return kwargs


print(utworz_profil_uzytkownika(imie="kasia", email="k@o2.pl", wiek=39, wzrost=170, waga=65))
