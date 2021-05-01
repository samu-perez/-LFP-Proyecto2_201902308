import webbrowser
import generarAutom

automatas = generarAutom.automatas
tabla_ = []

def tabla():
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
                    iteracion = 0
                    contError = 0
                    bandera = True
                    #$->λ
                    while True:
                        if estado == 'i':
                            tabla_.append([iteracion, pila, entrada[0], '(i, $, $; p, #)'])
                            iteracion += 1

                            pila += '#'
                            estado = 'p'
                        elif estado == 'p':
                            transix = '(p, $, $; q, ' + autom['transicion inicial'] + ')'
                            tabla_.append([iteracion, pila, entrada[pos], transix])
                            iteracion += 1

                            pila = autom['transicion inicial'] + pila
                            estado = 'q'
                        elif estado == 'q':
                            if bandera == True:
                                for transicion in autom['transiciones']:
                                    for subTrans in transicion:
                                        x = subTrans #Solo para quitar el Unused de subTrans
                                        x += ""
                                        if transicion[0] == pila[0]:
                                            transix = '(q, $, ' + transicion[0] + '; q, ' + transicion[1] + ')'
                                            tabla_.append([iteracion, pila, entrada[pos], transix])
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
                                                transix = '(q, $, ' + transicion[0] + '; q, ' + transicion[1] + ')'
                                                tabla_.append([iteracion, pila, entrada[pos], transix])
                                                iteracion += 1

                                                pila = transicion[1] + pila[1:]
                            if condicion_terminal == 'no':
                                for transicion in autom['transiciones']:
                                    for subTrans in transicion:
                                        if transicion[0] == pila[0]:
                                            transix = '(q, $, ' + transicion[0] + '; q, ' + transicion[1] + ')'
                                            tabla_.append([iteracion, pila, entrada[pos], transix])
                                            iteracion += 1

                                            pila = transicion[1] + pila[1:]
                                            transicion[0] = ' ' + transicion[0]

                            if entrada[pos] == pila[0]:
                                transix = '(q, ' + pila[0] + ', ' + pila[0] + '; q, $)'
                                tabla_.append([iteracion, pila, entrada[pos], transix])
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
                            aceptacion = ""
                            if pila[0] == '#':
                                tabla_.append([iteracion, pila, '$', '(q, $, #; f, $)'])
                                iteracion += 1
                                tabla_.append([iteracion, '$', '$', 'f'])

                                print(">La cadena ha sido aceptada")
                                print(">Se ha generado un reporte en tabla sobre el proceso")
                                aceptacion = "True"
                                tabla_html(nomAutom, entrada, aceptacion)
                                tabla_.clear()
                            else:
                                print(">La cadena no es valida")
                                print(">Se ha generado un reporte en tabla sobre el proceso")
                                aceptacion = 'False'
                                tabla_html(nomAutom, entrada, aceptacion)
                                tabla_.clear()

                            break
                    return  #Si lo encuentra se detiene
                
                else:
                    bandera = False
    
    if bandera == False:
        print(">Automata no encontrado.")

def tabla_html(nombre, entrada, aceptacion):
    fileHTML = open("Reporte Automata (tabla).html", "w")
    fileHTML.write("<HTML>")
    fileHTML.write("<link rel=\"stylesheet\" href=\"Plantilla 2 Reporte HTML/assets/css/main.css\"/>")
    fileHTML.write("<HEAD>")
    fileHTML.write("Samuel Isaac Pérez Pérez - 201902308")
    fileHTML.write("</HEAD>")

    fileHTML.write("<BODY>")
    fileHTML.write("<article id=\"first\" class=\"container box style1 right\">")
    fileHTML.write("<header align=\"center\">")
    fileHTML.write("<h2>" + nombre + "</h2>")
    fileHTML.write("<h2>Reporte en tabla</h2>")
    fileHTML.write("</header>")

    fileHTML.write("<b>Cadena de entrada: </b>" + entrada + "<br>")

    fileHTML.write("<table>")
    fileHTML.write("<tr>")
    fileHTML.write("<th><h4>Iteracion</h4></th>")
    fileHTML.write("<th><h4>Pila</h4></th>")
    fileHTML.write("<th><h4>Entrada</h4></th>")
    fileHTML.write("<th><h4>Transiciones</h4></th>")
    fileHTML.write("</tr>")
    for elem in tabla_:
        fileHTML.write("<tr>")
        for subElem in elem:
            fileHTML.write("<th>" + str(subElem) + "</th>")
        fileHTML.write("</tr>")
    fileHTML.write("</table>")

    if aceptacion == 'True':
        fileHTML.write("<b>Cadena aceptada</b>")
    elif aceptacion == 'False':
        fileHTML.write("<b>Cadena no valida</b>")

    fileHTML.write("</article>")
    fileHTML.write("</BODY>")
    fileHTML.write("</HTML>")
    fileHTML.close() #Cerrando el archivo HTML

    #Abriendo el archivo HTML automaticamente
    url = 'Reporte Automata (tabla).html'
    webbrowser.open(url)