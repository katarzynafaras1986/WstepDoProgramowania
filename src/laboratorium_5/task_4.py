# Zadanie 4.
# Napisz funkcję sum_digits(n), która oblicza sumę cyfr liczby rekurencyjnie. Napisz dokumentacje tej
# funkcji, która opisywać będzie jej działanie.

def sum_digits(n):
    """
    Funkcja oblicza sumę cyfr liczby naturalnej n.

    Działa rekurencyjnie:
    - Jeśli liczba n jest mniejsza niż 10, zwraca ją bezpośrednio
      (jest to pojedyncza cyfra).
    - W przeciwnym wypadku zwraca sumę ostatniej cyfry liczby n
      oraz wyniku wywołania funkcji dla liczby n bez ostatniej cyfry.

    Parametry:
    n (int): Liczba naturalna, której cyfry mają zostać zsumowane.

    Zwraca:
    int: Suma cyfr liczby n.

    Przykład:
    >>> sum_digits(523)
    10
    """
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n//10)

print(sum_digits(523))