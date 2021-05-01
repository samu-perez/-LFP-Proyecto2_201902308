import os
import time
import cargarArch
import mostrarGram
import generarAutom
import recorrido
import tabla

bandera = True
def menu():
    os.system('cls')
    
    print("**************  PROYECTO FINAL - LFP  ***************")
    print("-----------------------------------------------------")
    print("|  Lenguajes Formales y de Programación sección A+  |")
    print("|       Samuel Isaac Pérez Pérez - 201902308        |")
    print("-----------------------------------------------------")
    cont = 5
    global bandera
    while cont > 0 and bandera == True:
        print(cont)
        time.sleep(1)
        if cont == 1:
            print("******************** BIENVENIDO ********************")
            bandera = False
        cont -= 1

    print("Opciones: ")
    print("\t1 - Cargar archivo")
    print("\t2 - Mostrar información general de la gramática")
    print("\t3 - Generar autómata de pila equivalente")
    print("\t4 - Reporte de recorrido")
    print("\t5 - Reporte en tabla")
    print("\t6 - Salir")

while True:
    menu()
    opcionMenu = input("Ingrese el número de una opción >> ")

    if opcionMenu == "1":
        print("")
        print("Opción -> Cargar archivo:")
        cargarArch.cargar_archivo()
    
        input("------Pulsa una tecla para continuar------")
        
    elif opcionMenu == "2":
        print("")
        print("Opción -> Mostrar información general de la gramática:")
        mostrarGram.mostrar_Gram()
        
        input("------Pulsa una tecla para continuar------")

    elif opcionMenu == "3":
        print("")
        print("Opción -> Generar autómata de pila equivalente:")
        generarAutom.generar_automata()
        
        input("------Pulsa una tecla para continuar------")
    elif opcionMenu == "4":
        print("")
        print("Opción -> Reporte de recorrido:")
        recorrido.recorrido()
        
        input("------Pulsa una tecla para continuar------")
    elif opcionMenu == "5":
        print("")
        print("Opción -> Reporte en tabla:")
        tabla.tabla()
        
        input("------Pulsa una tecla para continuar------")
    elif opcionMenu == "6":
        print("Hasta la próxima :)")
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\n------Pulsa una tecla para continuar------")