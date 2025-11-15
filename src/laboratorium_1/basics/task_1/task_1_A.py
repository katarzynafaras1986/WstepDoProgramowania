# Zad. 1:
# A) Sprawdź w interpreterze typ wyników określonych działań - type( x ) i wyjaśnij, co
# oznaczają poszczególne operatory?
# 1. 1 + 2
# 2. 1 + 4.5
# 3. 3 / 2
# 4. 4 / 2
# 5. 3 // 2
# 6. -3 // 2
# 7. 11 % 2
# 8. 2 ** 10
# 9. 8 ** (1/3)
#moja metoda do drukowania wników
def print_result(result, subsection):
    print(f"Zadanie_1_A.{subsection} Wynik to: {result}, typ: {type(result)}")

#1. dodawanie dwóch intigerów którego wynikiem jest intiger
result= 1 + 2
print_result(result,1)

#2. dodawanie dwóch intigera oraz floata którego wynikiem jest float
result= 1 + 4.5
print_result(result,2)

#3. dzielenie intigera przez intigera z resztą wynikiem jest float
result= 3/2
print_result(result,3)

#4. dzielenie intigera przez intigera z resztą wynikiem jest float
result=4/2
print_result(result, 4)

#5. dzielenie intigera przez intigera bez reszty wynikiem jest intiger
result=3//2
print_result(result, 5)

#6. dzielenie intigera ujemnego przez intigera bez reszty wynikiem jest intiger ujemny
result=-3//2
print_result(result,6)

#7. dzielenie intigera ujemnego przez intigera bez reszty wynikiem jest intiger ujemny
result=11 % 2
print_result(result,7)

#8. potęgowanie intigera wynikiem jest intiger
result=2 ** 10
print_result(result, 8)

#9. potęgowanie intigera ułamkiem (czyli pierwiastkowanie) wynikiem jest float
result=8 ** (1/3)
print_result(result, 9)




