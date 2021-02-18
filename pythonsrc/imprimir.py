def imprimir_txt_ecuaciones(n):
    lista2=n
    ec1=""
    for i in lista2:
        print("||" + i)
    if len(lista2) == 6:
        for i in lista2:
            if lista2.index(i) == 0 or lista2.index(i) == 3:
                ec1 +=(i+"x ")
            elif lista2.index(i) == 1 or lista2.index(i) == 4:
                if float(i) >= 0:
                    ec1 +=("+ "+i+"y  ")
                else:
                    ec1 +=(" "+i+"y ")
            elif lista2.index(i) == 2 or lista2.index(i) == 5:
                ec1 +=("= "+i+'\n')    
        print(ec1)
    return ec1
   
