# Zad. 6 Napisz skrypt w Pythonie, który sprawdza, czy litera wprowadzona przez użytkownika jest
# duża czy mała

def sprawdz_wielkosc_litery(litera):
    if litera.isupper():
        print(f"{litera} jest dużą literą")
    elif litera.islower():
        print(f"{litera} jest małą literą")


sprawdz_wielkosc_litery(input(f"Wprowadź literę: "))
