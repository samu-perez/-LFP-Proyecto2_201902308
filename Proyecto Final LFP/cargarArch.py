from tkinter import filedialog

gramaticas = []

def cargar_archivo():
    archivo = filedialog.askopenfilename(title = "Explorador de Archivos", initialdir = "C:/", 
    filetypes = (("Archivos GLC", "*.glc"), ("Todos los archivos", "*.*")))
    #archivo = "entrada.glc"
    diccAux = {}
    producciones = []
    if archivo != "":
        linea = 1
        with open(archivo) as fileObject:
            for line in fileObject:
                texto = line.rstrip()
                
                if linea == 1:
                    diccAux['nombre'] = texto
                    linea = 2
                elif linea == 2:
                    simbolos = texto.split(';')
                    diccAux['NT'] = simbolos[0]
                    diccAux['T'] = simbolos[1]
                    diccAux['NT inicial'] = simbolos[2]
                    linea = 3
                elif texto == '*':
                    diccAux['producciones'] = producciones
                    gramaticas.append(diccAux)
                    diccAux = {}
                    producciones = []
                    linea = 1
                    
                elif linea == 3:
                    producciones.append(texto.replace(' ', ''))

        print(">Se ha cargado el archivo correctamente.")

    else:
        print(">No se ha cargado el archivo de entrada.")
