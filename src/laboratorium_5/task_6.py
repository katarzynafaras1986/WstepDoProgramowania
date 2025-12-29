# Zadanie 6.
# Odpowiedz na pytania i krótko uzasadnij odpowiedź:


# 1. Co się stanie? Czy kod się wykona, czy wystąpi błąd? Jeśli błąd, podaj jego typ i powód.
# def t(x, *, y, z=0):
#     return x + y + z
# val= t(1, 2, z=3)
# 2. Wyjaśnij co dokładnie zwróci y oraz jak Python rozdzielił argumenty.
f = lambda a, /, *args, b=0: (a, sum(args) + b)
y = f(3, 4, 5, b=2)
print(y)

# Odp:1 - Kod zakończy się błędem typu TypeError i nie zostanie poprawnie wykonany.
# Parametr y jest parametrem tylko nazwanym (keyword-only), ponieważ w definicji funkcji znajduje się po *.
#
# To oznacza, że:
#
# y musi być przekazany jako argument nazwany
#
# nie można go przekazać pozycyjnie
#
# W wywołaniu:
#
# t(1, 2, z=3)
# Python interpretuje:
# 1 → x
# 2 → próba przypisania do y pozycyjnie ❌ (niedozwolone)
# Komunikat błędu :     val= t(1, 2, z=3)
# TypeError: t() takes 1 positional argument but 2 positional arguments (and 1 keyword-only argument) were given

# Odp:2 - y zwrócił (3, 11)
# python rozdzielił argumenty następująco:
# a = 3
# args = (4, 5)
# b = 2
#  i wykonał obliczenia;
# sum(args) = 4 + 5 = 9
# sum(args) + b = 9 + 2 = 11
