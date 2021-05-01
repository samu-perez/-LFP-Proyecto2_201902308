import cargarArch

gramaticas = cargarArch.gramaticas

def mostrar_Gram():
    print("\n>Gramaticas cargadas al sistema:")
    for gram in gramaticas:
        for k, v in gram.items():
            if k == 'nombre':
                print(v)
    nomGram = input("\n>Ingrese el nombre de la gramatica: ")
    bandera = True
    for gram in gramaticas:
        for k, v in gram.items():
            if k == 'nombre':
                if nomGram == v:
                    print()
                    print("Nombre de la gramática: " + gram['nombre'])
                    print("No terminales = { " + gram['NT'] + " }")
                    print("Terminales = { " + gram['T'] + " }")
                    print("No terminal inicial = " + gram['NT inicial'])
                    print("Producciones:")
                    for produccion in gram['producciones']:
                        print(produccion)
                    return #Si la encuentra se detiene
                else:
                    bandera = False

    if bandera == False:
        print(">Gramatica no encontrada.")