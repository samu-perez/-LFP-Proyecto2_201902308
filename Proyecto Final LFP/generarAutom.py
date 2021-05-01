from graphviz import Digraph
import webbrowser
import cargarArch

gramaticas = cargarArch.gramaticas
automatas = []

def generar_automata():
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
                    #--------------------GUARDANDO LAS TRANSICIONES DEL AUTOMATA ------------
                    diccAux = {}
                    diccAux['nombre'] = 'AP_' + nomGram
                    diccAux['transicion inicial'] = gram['NT inicial']
                    transiciones = []

                    for produccion in gram['producciones']:
                        transiciones.append(produccion.split('->'))
                    diccAux['transiciones'] = transiciones

                    automatas.append(diccAux)
                    #--------------------------------------------------------------------------
                    
                    g = Digraph('G', filename='Automata de pila', format='png')
                    g.attr(rankdir='LR')
                    g.attr(color='black')
                    g.attr('node', fontsize='22', style='filled', color='lightgrey')
                    g.node('i')
                    g.node('p')
                    g.node('q')
                    g.node('f', shape='doublecircle')

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

                    alfabeto = gram['T'] + ',' + gram['NT'] + ',#'
                    print(">Se ha generado el automata de pila")
                    automata_html(nomGram, gram['T'], alfabeto)  #Llamada al metodo de html
                    return #Si la encuentra se detiene
                else:
                    bandera = False

    if bandera == False:
        print(">Gramatica no encontrada.")

def automata_html(nombre, terminales, alfabeto):
    fileHTML = open("Reporte Automata.html", "w")
    fileHTML.write("<HTML>")
    fileHTML.write("<link rel=\"stylesheet\" href=\"Plantilla Reporte HTML/assets/css/main.css\"/>")
    fileHTML.write("<HEAD>")
    fileHTML.write("Samuel Isaac Pérez Pérez - 201902308")
    fileHTML.write("</HEAD>")

    fileHTML.write("<BODY>")
    fileHTML.write("<article id=\"first\" class=\"container box style1 right\">")
    fileHTML.write("<header align=\"center\">")
    fileHTML.write("<h2>AP_" + nombre + "</h2>")
    fileHTML.write("</header>")

    fileHTML.write("<b>Terminales</b> = { " + terminales + " }<br>")
    fileHTML.write("<b>Alfabeto de pila</b> = { " + alfabeto + " }<br>")
    fileHTML.write("<b>Estados</b> = { i, p, q, f }<br>")
    fileHTML.write("<b>Estado inicial</b> = { i }<br>")
    fileHTML.write("<b>Estado de aceptación</b> = { f }<br>")

    fileHTML.write("<img src='Automata de pila.png' align='center'>")
    #fileHTML.write("<img src='Automata de pila.png' align='center' width='400'>")

    fileHTML.write("</article>")
    fileHTML.write("</BODY>")
    fileHTML.write("</HTML>")
    fileHTML.close() #Cerrando el archivo HTML

    #Abriendo el archivo HTML automaticamente
    url = 'Reporte Automata.html'
    webbrowser.open(url)