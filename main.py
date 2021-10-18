def printMeniu():
    print("1.Citire lista")
    print("2.Afișarea listei după eliminarea duplicatelor")
    print("3.Afișarea sumei primelor n numere pozitive din listă, unde n se citește de la tastatură.")
    print("4.Să se afișeze “DA” în cazul în care toate numerele pozitive din listă sunt în ordine crescătoare și “NU” altfel.")
    print("5.Afișarea listei obținute din lista inițială în care numerele care apar doar o singură dată sunt înlocuite cu numărul de divizori proprii ai numărului.")
    print("x.Iesire")


def citireLista():
    l = []
    givenString = input("Dati lista, cu elemente separate prin virgula")
    numberAsString = givenString.split(",")
    for x in numberAsString:
        l.append(int(x))
    return l


def main():
    '''apelare teste'''
    l = []
    while True:
        printMeniu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            print()
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