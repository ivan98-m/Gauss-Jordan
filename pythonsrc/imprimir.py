def imprimir_ecuaciones(n):
    ecuacion3 = ecuacion4 = ecuacion5 = ""
    lista_flotantes = [float(i) for i in n]
    lista_formato = []
    for i in lista_flotantes:
        if i - int(i) == 0:
            lista_formato.append(int(i))
        else:
            lista_formato.append(i)

    if len(lista_flotantes) == 6:
        ecuacion1 = lista_formato[0:3]
        ecuacion2 = lista_formato[3:6]
    if len(lista_flotantes) == 12:
        ecuacion1 = lista_formato[0:4]
        ecuacion2 = lista_formato[4:8]
        ecuacion3 = lista_formato[8:12]
    if len(lista_flotantes) == 20:
        ecuacion1 = lista_formato[0:5]
        ecuacion2 = lista_formato[5:10]
        ecuacion3 = lista_formato[10:15]
        ecuacion4 = lista_formato[15:20]
    if len(lista_flotantes) == 30:
        ecuacion1 = lista_formato[0:6]
        ecuacion2 = lista_formato[6:12]
        ecuacion3 = lista_formato[12:18]
        ecuacion4 = lista_formato[18:24]
        ecuacion5 = lista_formato[24:30]

    def ceros(lista: list) -> bool:
        return all(dato == 0 for dato in lista)

    def formato(ecuacion):
        if isinstance(ecuacion, str): return ""

        terminos = ecuacion[:-1]
        resultado = ecuacion[-1]
        i = 0
        var = ""
        cadena = ""
        #print(f"Elementos individuales: {terminos[0]}, {terminos[1]}")
        for _ in terminos:
            if i == 0:
                if ecuacion[0] == 0:
                    i+=1
                    var = "y "
                    continue
                else:
                    cadena = str(ecuacion[0]) + "x "
                    i+=1
                    var = "y "
                    continue

            if terminos[i] > 0:
                if ceros(terminos[0:i]):
                    cadena += (str(terminos[i]) + var)
                else:
                    cadena += ("+ " + str(terminos[i]) + var)
            elif terminos[i] < 0:
                cadena +=("- "+str(abs(terminos[i])) + var)
            elif terminos[i] == 0:
                pass

            if i == 1: var = "z "
            if i == 2: var = "w "
            if i == 3: var = "v "

            i += 1

        if ceros(terminos) and resultado == 0:
            cadena = "0 = 0 Ecuación nula"
        else:
            cadena += ("= " + str(resultado))
        return cadena

    f = formato(ecuacion1)+'\n'+formato(ecuacion2)+'\n'+formato(ecuacion3)+'\n'+formato(ecuacion4)+'\n'+formato(ecuacion5)

    print(f"Formato de una ecuacion: {f}")

    #self.textecuaciones.setText(f)
    return f

def imprimir_soluciones(x):
    print(x)
    cad=""
    variables = ['x', 'y', 'z', 'w', 'v']
    lista_soluciones = [float(i) for i in x]
    cont=0
    for i in lista_soluciones:
        cad += variables[cont] + " = " + str(i) +'\n'
        cont = cont+1
    return cad