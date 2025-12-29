import pytest

from task_5 import zamien_miejscami_elementy_listy

def test_zamiana_poprawna():
    lista = [1, 2, 3, 4, 5]
    wynik = zamien_miejscami_elementy_listy(lista, 0, 4)
    assert wynik == [5, 2, 3, 4, 1]

def test_zamiana_tych_samych_indeksow():
    lista = [1, 2, 3]
    wynik = zamien_miejscami_elementy_listy(lista, 1, 1)
    assert wynik == [1, 2, 3]  # lista nie powinna się zmienić

def test_lista_pusta():
    with pytest.raises(ValueError) as e:
        zamien_miejscami_elementy_listy([], 0, 1)
    assert "Lista nie może być pusta" in str(e.value)

def test_index1_nie_int():
    with pytest.raises(TypeError) as e:
        zamien_miejscami_elementy_listy([1, 2, 3], "0", 2)
    assert "Index1 musi być intem" in str(e.value)

def test_index2_nie_int():
    with pytest.raises(TypeError) as e:
        zamien_miejscami_elementy_listy([1, 2, 3], 0, "2")
    assert "Index2 musi być intem" in str(e.value)

def test_index1_out_of_bounds():
    with pytest.raises(IndexError) as e:
        zamien_miejscami_elementy_listy([1, 2, 3], 5, 1)
    assert "OutOfBoundException" in str(e.value)

def test_index2_out_of_bounds():
    with pytest.raises(IndexError):
        zamien_miejscami_elementy_listy([1, 2, 3], 1, 10)

def test_zamiana_z_indeksami_ujemnymi():
    lista = [10, 20, 30, 40]
    wynik = zamien_miejscami_elementy_listy(lista, -1, 0)
    assert wynik == [40, 20, 30, 10]