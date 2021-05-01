from graphviz import Digraph
import webbrowser
import generarAutom
import cargarArch

automatas = generarAutom.automatas #Lista de diccionarios de automatas
gramaticas = cargarArch.gramaticas

def recorrido():
    print("\n>Automatas de pila generados:")
    for autom in automatas:
        for k, v in autom.items():
            if k == 'nombre':
                print(v)

    nomAutom = input("\n>Ingrese el nombre del automata: ")
    bandera = True

    for autom in automatas:
        for k, v in autom.items():
            if k == 'nombre':
                if nomAutom == v:
                    condicion_terminal = input("\n¿Después de la primera producción, todas las siguientes inician con simbolos terminales?  (si o no): ")
                    entrada = input("\n>Ingrese una cadena de entrada: ")
                    pila = ""
                    estado = 'i'
                    pos = 0
                    contError = 0
                    iteracion = 0
                    bandera = True

                    fileHTML = open("Reporte Automata (recorrido).html", "w")
                    fileHTML.write("<HTML>")
                    fileHTML.write("<link rel=\"stylesheet\" href=\"Plantilla Reporte HTML/assets/css/main.css\"/>")
                    fileHTML.write("<HEAD>")
                    fileHTML.write("Samuel Isaac Pérez Pérez - 201902308")
                    fileHTML.write("</HEAD>")

                    fileHTML.write("<BODY>")
                    fileHTML.write("<article id=\"first\" class=\"container box style1 right\">")
                    fileHTML.write("<header align=\"center\">")
                    fileHTML.write("<h2>" + nomAutom + "</h2>")
                    fileHTML.write("<h2>Reporte de recorrido</h2>")
                    fileHTML.write("</header>")
                    fileHTML.write("</article>")
                    
                    while True:
                        if estado == 'i':
                            fileHTML.write("<article id=\"first\" class=\"container box style1 right\">")
                            fileHTML.write("<b>Iteración</b>: " + str(iteracion) + "<br>")
                            fileHTML.write("<b>Transición</b>: $, $; #  ($=lambda) <br>")
                            fileHTML.write("<b>Pila</b>: " + pila + "<br>")
                            fileHTML.write("<b>Entrada</b>: ")
                            nomImage = 'images/Automata de pila (recorrido) i'
                            automata_imagen(nomAutom[3:], estado, nomImage)
                            fileHTML.write("<img src='images/Automata de pila (recorrido) i.png' align='center'>")
                            fileHTML.write("</article>")
                            iteracion += 1

                            pila += '#'
                            estado = 'p'
                        elif estado == 'p':
                            fileHTML.write("<article id=\"first\" class=\"container box style1 right\">")
                            fileHTML.write("<b>Iteración</b>: " + str(iteracion) + "<br>")
                            transix = '$, $; ' + autom['transicion inicial']
                            fileHTML.write("<b>Transición</b>: " + transix +  " ($=lambda) <br>")
                            fileHTML.write("<b>Pila</b>: " + pila + "<br>")
                            fileHTML.write("<b>Entrada</b>: " + entrada[pos])
                            nomImage = 'images/Automata de pila (recorrido) p'
                            automata_imagen(nomAutom[3:], estado, nomImage)
                            fileHTML.write("<img src='images/Automata de pila (recorrido) p.png' align='center'>")
                            fileHTML.write("</article>")
                            iteracion += 1

                            pila = autom['transicion inicial'] + pila
                            estado = 'q'
                        elif estado == 'q':
                            nomImage = 'images/Automata de pila (recorrido) q'
                            automata_imagen(nomAutom[3:], estado, nomImage)

                            if bandera == True:
                                for transicion in autom['transiciones']:
                                    for subTrans in transicion:
                                        x = subTrans #Solo para quitar el Unused de subTrans
                                        x += ""
                                        if transicion[0] == pila[0]:
                                            fileHTML.write("<article id=\"first\" class=\"container box style1 right\">")
                                            fileHTML.write("<b>Iteración</b>: " + str(iteracion) + "<br>")
                                            transix = '$, ' + transicion[0] + '; ' + transicion[1] + '  ($=lambda)'
                                            fileHTML.write("<b>Transición</b>: " + transix + "<br>")
                                            fileHTML.write("<b>Pila</b>: " + pila + "<br>")
                                            fileHTML.write("<b>Entrada</b>: " + entrada[pos])
                                            fileHTML.write("<img src='images/Automata de pila (recorrido) q.png' align='center'>")
                                            fileHTML.write("</article>")
                                            iteracion += 1

                                            pila = transicion[1] + pila[1:]
                                            bandera = False
                                    break

                            if condicion_terminal == 'si':
                                for transicion in autom['transiciones']:
                                    for subTrans in transicion:
                                        if transicion[0] == pila[0]:
                                            produccion = transicion[1]
                                            if produccion[0] == entrada[pos]:
                                                fileHTML.write("<article id=\"first\" class=\"container box style1 right\">")
                                                fileHTML.write("<b>Iteración</b>: " + str(iteracion) + "<br>")
                                                transix = '$, ' + transicion[0] + '; ' + transicion[1] + '  ($=lambda)'
                                                fileHTML.write("<b>Transición</b>: " + transix + "<br>")
                                                fileHTML.write("<b>Pila</b>: " + pila + "<br>")
                                                fileHTML.write("<b>Entrada</b>: " + entrada[pos])
                                                fileHTML.write("<img src='images/Automata de pila (recorrido) q.png' align='center'>")
                                                fileHTML.write("</article>")
                                                iteracion += 1

                                                pila = transicion[1] + pila[1:]

                            if condicion_terminal == 'no':
                                for transicion in autom['transiciones']:
                                    for subTrans in transicion:
                                        if transicion[0] == pila[0]:
                                            #x = subTrans #Solo para quitar el Unused de subTrans
                                            #x += ""
                                            fileHTML.write("<article id=\"first\" class=\"container box style1 right\">")
                                            fileHTML.write("<b>Iteración</b>: " + str(iteracion) + "<br>")
                                            transix = '$, ' + transicion[0] + '; ' + transicion[1] + '  ($=lambda)'
                                            fileHTML.write("<b>Transición</b>: " + transix + "<br>")
                                            fileHTML.write("<b>Pila</b>: " + pila + "<br>")
                                            fileHTML.write("<b>Entrada</b>: " + entrada[pos])
                                            fileHTML.write("<img src='images/Automata de pila (recorrido) q.png' align='center'>")
                                            fileHTML.write("</article>")
                                            iteracion += 1

                                            pila = transicion[1] + pila[1:]
                                            transicion[0] = ' ' + transicion[0]

                            if entrada[pos] == pila[0]:
                                fileHTML.write("<article id=\"first\" class=\"container box style1 right\">")
                                fileHTML.write("<b>Iteración</b>: " + str(iteracion) + "<br>")
                                transix = pila[0] + ', ' + pila[0] + '; $  ($=lambda)' 
                                fileHTML.write("<b>Transición</b>: " + transix + "<br>")
                                fileHTML.write("<b>Pila</b>: " + pila + "<br>")
                                fileHTML.write("<b>Entrada</b>: " + entrada[pos])
                                fileHTML.write("<img src='images/Automata de pila (recorrido) q.png' align='center'>")
                                fileHTML.write("</article>")
                                iteracion += 1

                                pila = pila[1:]
                                pos += 1
                            else:
                                contError += 1

                            
                            if pos == len(entrada):
                                estado = 'f'
                            elif contError == len(entrada):
                                estado = 'f'

                        elif estado == 'f':
                            for transicion in autom['transiciones']:
                                for subTrans in transicion:
                                    nt = transicion[0]
                                    transicion[0] = nt.replace(' ', '')
                            if pila[0] == '#':
                                nomImage = 'images/Automata de pila (recorrido) f'
                                automata_imagen(nomAutom[3:], estado, nomImage)
                                fileHTML.write("<article id=\"first\" class=\"container box style1 right\">")
                                fileHTML.write("<b>Iteración</b>: " + str(iteracion) + "<br>")
                                fileHTML.write("<b>Transición</b>: $, #; $  ($=lambda)<br>")
                                fileHTML.write("<b>Pila</b>: " + pila + "<br>")
                                fileHTML.write("<b>Entrada</b>: ")
                                fileHTML.write("<img src='images/Automata de pila (recorrido) q.png' align='center'>")
                                fileHTML.write("</article>")
                                iteracion += 1
                                fileHTML.write("<article id=\"first\" class=\"container box style1 right\">")
                                fileHTML.write("<b>Iteración</b>: " + str(iteracion) + "<br>")
                                fileHTML.write("<b>Transición</b>: <br>")
                                fileHTML.write("<b>Pila</b>: <br>")
                                fileHTML.write("<b>Entrada</b>: ")
                                fileHTML.write("<img src='images/Automata de pila (recorrido) f.png' align='center'>")
                                fileHTML.write("</article>")
                                fileHTML.write("<article id=\"first\" class=\"container box style1 right\">")
                                fileHTML.write("<header align=\"center\">")
                                fileHTML.write("<b><h3>¡La cadena ingresada es válida!</h3></b>")
                                fileHTML.write("</header>")
                                fileHTML.write("</article>")

                                print(">La cadena ha sido aceptada")
                                print(">Se ha generado un reporte de recorrido sobre el proceso")
                                
                                fileHTML.write("</BODY>")
                                fileHTML.write("</HTML>")
                                fileHTML.close() #Cerrando el archivo HTML

                                #Abriendo el archivo HTML automaticamente
                                url = 'Reporte Automata (recorrido).html'
                                webbrowser.open(url)
                            else:
                                print(">La cadena no es valida")
                                print(">Se ha generado un reporte de recorrido sobre el proceso")

                                fileHTML.write("<article id=\"first\" class=\"container box style1 right\">")
                                fileHTML.write("<header align=\"center\">")
                                fileHTML.write("<b><h3>¡La cadena ingresada no es válida!</h3></b>")
                                fileHTML.write("</header>")
                                fileHTML.write("</article>")
                                fileHTML.write("</BODY>")
                                fileHTML.write("</HTML>")
                                fileHTML.close() #Cerrando el archivo HTML

                                #Abriendo el archivo HTML automaticamente
                                url = 'Reporte Automata (recorrido).html'
                                webbrowser.open(url)
                            break
                    
                    return  #Si lo encuentra se detiene
                
                else:
                    bandera = False

    if bandera == False:
        print(">Automata no encontrado.")

def automata_imagen(nomGram, estado, nomImage):
    for gram in gramaticas:
        for k, v in gram.items():
            if k == 'nombre':
                if nomGram == v:
                    #nomImage = 'images/Automata de pila (recorrido)'
                    g = Digraph('G', filename=nomImage, format='png')
                    g.attr(rankdir='LR')
                    g.attr(color='black')
                    g.attr('node', fontsize='22', style='filled', color='lightgrey')
                    if estado == 'i':
                        g.node('i', style='filled', color='yellow')
                        g.node('p')
                        g.node('q')
                        g.node('f', shape='doublecircle')
                    elif estado == 'p':
                        g.node('i')
                        g.node('p', style='filled', color='yellow')
                        g.node('q')
                        g.node('f', shape='doublecircle')
                    elif estado == 'q':
                        g.node('i')
                        g.node('p')
                        g.node('q', style='filled', color='yellow')
                        g.node('f', shape='doublecircle')
                    elif estado == 'f':
                        g.node('i')
                        g.node('p')
                        g.node('q')
                        g.node('f', shape='doublecircle', style='filled', color='yellow')

                    g.edge('i', 'p', label='λ, λ; #   ', fontsize='17')
                    g.edge('p', 'q', label='λ, λ; ' + gram['NT inicial'], fontsize='17')
                    transiciones = ""
                    for produccion in gram['producciones']:
                        transiciones += 'λ, ' + produccion.replace('->', '; ') + '\n'

                    transiciones += '\n'
                    terminales = gram['T'].split(',')
                    for terminal in terminales:
                        transiciones += terminal + ', ' + terminal + '; λ\n'

                    g.edge('q', 'q', label=transiciones, fontsize='17')
                    g.edge('q', 'f', label='λ, #; λ   ', fontsize='17')

                    g.render()
    