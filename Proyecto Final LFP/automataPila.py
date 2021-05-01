import os

def menu():
    os.system('cls')
    
    print("***************  EXAMEN FINAL - LFP  ****************")
    print("-----------------------------------------------------")
    print("|  Lenguajes Formales y de Programación sección A+  |")
    print("|       Samuel Isaac Pérez Pérez - 201902308        |")
    print("-----------------------------------------------------")
    print("Opciones: ")
    print("\t1 - Automata de pila")
    print("\t2 - Salir")

while True:
    menu()
    opcionMenu = input("Ingrese el número de una opción >> ")

    if opcionMenu == "1":
        print("")
        print("Opción -> Automata de pila:")

        entrada = input("\nIngrese una cadena de entrada: ")
        pila = ""
        estado = 'i'
        pos = 0
        cont = 0
        contError = 0

        while True:
            if estado == 'i':
                pila += '#'
                estado = 'p'
                print(pila)
            elif estado == 'p':
                pila = 'S' + pila
                estado = 'q'
                print(pila)
            elif estado == 'q':
                if pila[0] == 'S':
                    pila = 'zTMz' + pila[1:]
                    print(pila)
                elif pila[0] == 'T' and (entrada[2] == '0' or entrada[1] == 'x'):
                    pila = 'L' + pila[1:]
                    print(pila)
                elif pila[0] == 'T' and (entrada[2] == '1' or entrada[1] == 'y'):
                    pila = 'K' + pila[1:]
                    print(pila)
                elif pila[0] == 'K' and entrada[pos] != 'y':
                    pila = '01K10' + pila[1:]
                    print(pila)
                elif pila[0] == 'K' and entrada[pos] == 'y':
                    pila = 'y' + pila[1:]
                    print(pila)
                elif pila[0] == 'L' and entrada[pos] != 'x':
                    pila = '00L11' + pila[1:]
                    print(pila)
                elif pila[0] == 'L' and entrada[pos] == 'x':
                    pila = 'x' + pila[1:]
                    print(pila)
                elif pila[0] == 'M' and entrada[pos] != 'z':
                    pila = 'aMa' + pila[1:]
                    print(pila)
                elif pila[0] == 'M' and entrada[pos] == 'z':
                    pila = 'z' + pila[1:]
                    print(pila)
                #Solo terminales
                elif entrada[pos] == pila[0]:
                    pila = pila[1:]
                    print(pila)
                    pos += 1
                else:
                    contError += 1
                cont += 1
                print("CONTADOR:", cont)
                if pos == len(entrada):
                    estado = 'f'
                elif contError == len(entrada):
                    estado = 'f'
                
            elif estado == 'f':
                if pila[0] == '#':
                    print("\n>La cadena ha sido aceptada")
                else:
                    print("\n>La cadena no es valida")
                break
    
        input("------Pulsa una tecla para continuar------")
        
    elif opcionMenu == "2":
        print("Hasta la próxima :)")
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\n------Pulsa una tecla para continuar------")