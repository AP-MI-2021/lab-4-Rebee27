def printMeniu():
    print("1.Citire lista")
    print("2.Afișarea listei după eliminarea duplicatelor")
    print("3.Afișarea sumei primelor n numere pozitive din listă, unde n se citește de la tastatură.")
    print(
        "4.Să se afișeze “DA” în cazul în care toate numerele pozitive din listă sunt în ordine crescătoare și “NU” altfel.")
    print(
        "5.Afișarea listei obținute din lista inițială în care numerele care apar doar o singură dată sunt înlocuite cu numărul de divizori proprii ai numărului.")
    print("x.Iesire")


def citireLista():
    l = []
    givenString = input("Dati lista, cu elemente separate prin virgula")
    numberAsString = givenString.split(",")
    for x in numberAsString:
        l.append(int(x))
    return l

'''
2.Afișarea listei după eliminarea duplicatelor
param l : lista data de la tastatura
return : lista fara duplicate
'''
def eliminare_duplicate(l):
    rezultat = []
    for i in l:
        if i not in rezultat:
            rezultat.append(i)
    return rezultat


def test_eliminare_duplicate():
    assert eliminare_duplicate([5, 6, 6, 5, 7, 0, 6]) == [5, 6, 7, 0]
    assert eliminare_duplicate([2, 3, 4, 5, 6]) == [2, 3, 4, 5, 6]
    assert eliminare_duplicate([1, 1]) == [1]


'''
3.Afișarea sumei primelor n numere pozitive din listă, unde n se citește de la tastatură
param l : lista data de la tastatura
param n : numarul elementelor din lista date pentru suma
return : Suma primelor n nr pozitive
'''

'''
def suma_n_pozitive(l):
    n = int(input("Dati numarul de numere pentru suma"))
    nr = 0
    for x in l:
        while x > 0 and nr <= n:
            suma = suma + x
            nr = nr + 1
    return suma


def test_suma_n_pozitive():
    assert suma_n_pozitive([1, 2, 3, 4, 5]) == 15
    assert suma_n_pozitive([-1, -2, 3, 4, 5]) == 12
    assert suma_n_pozitive([-1, -2, -3, -4, -5]) == 0
'''

def main():
    test_eliminare_duplicate()
    l = []
    while True:
        printMeniu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            print(eliminare_duplicate(l))
        elif optiune == "3":
            print()
        elif optiune == "4":
            print()
        elif optiune == "5":
            print()
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati!")


main()
