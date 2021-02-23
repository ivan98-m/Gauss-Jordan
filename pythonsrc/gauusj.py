#Matriz maxima a ingresar de 5x5
""" [1,2,3,4,5,6] 2x2 
[1,2,3,4,5,6,3,3,3,3,3,3] 3x3  """
import numpy as np

"""def pedirVal(orden):
    for i in range(orden):
        lista.append(int(input("Valor :"+str(i+1)+" ")))"""
        
def lista_inicial(lista,metodo):#Si esta en true es Gauus Jordan
    longitud=len(lista)
    if(longitud==6):
        matriz=np.array(lista, dtype='float').reshape(2,3)
        #matriz=np.reshape(lista,(2,3))
        #a=np.reshape(matriz,(2,2))
        b=matriz[:,2] #Igual de la ecuacion
        a=np.delete(matriz,2,axis=1)# Matriz de coeficientes
        #print(b)
        #print(a)
        
        if (np.linalg.det(a)==0):
            print ("No hay solucion el sistema es inconsitente")
            return 0,0,"No hay solucion el sistema es inconsitente"
        else:
            #print(np.linalg.det(a))
            print ("Aqui va la sol")
            if(metodo==True):
                X,A,sol=gaussJordan2(a,b)
                """ print(X)
                print(A) """
                return X,A,sol
            else:
                X,A,sol=gaussJordan(a,b)
                """ print(X)
                print(A) """
                return X,A,sol
            #print(gaussJordan(a,b))
    elif(longitud==12):
        matriz=np.array(lista, dtype='float').reshape(3,4)
        #matriz=np.reshape(lista,(2,3))
        #a=np.reshape(matriz,(2,2))
        b=matriz[:,3] #Igual de la ecuacion
        a=np.delete(matriz,3,axis=1)# Matriz de coeficientes
        #print(b)
        #print(a)
        
        if (np.linalg.det(a)==0):
            print ("No hay solucion el sistema es inconsitente")
            return 0,0,"No hay solucion el sistema es inconsitente"
        else:
            if(metodo==True):
                X,A,sol=gaussJordan2(a,b)
                """ print(X)
                print(A) """
                return X,A,sol
            else:
                X,A,sol=gaussJordan(a,b)
                """ print(X)
                print(A) """
                return X,A,sol
    elif (longitud==20):
        matriz=np.array(lista, dtype='float').reshape(4,5)
        #matriz=np.reshape(lista,(2,3))
        #a=np.reshape(matriz,(2,2))
        b=matriz[:,4] #Igual de la ecuacion
        a=np.delete(matriz,4,axis=1)# Matriz de coeficientes
        #print(b)
        #print(a)
        
        if (np.linalg.det(a)==0):
            print ("No hay solucion el sistema es inconsitente")
            return 0,0,"No hay solucion el sistema es inconsitente"
        else:
            if(metodo==True):
                X,A,sol=gaussJordan2(a,b)
                """ print(X)
                print(A) """
                return X,A,sol
            else:
                X,A,sol=gaussJordan(a,b)
                """ print(X)
                print(A) """
                return X,A,sol
    elif (longitud==30):
        matriz=np.array(lista, dtype='float').reshape(5,6)
        #matriz=np.reshape(lista,(2,3))
        #a=np.reshape(matriz,(2,2))
        b=matriz[:,5] #Igual de la ecuacion
        a=np.delete(matriz,5,axis=1)# Matriz de coeficientes
        #print(b)
        #print(a)
        
        if (np.linalg.det(a)==0):
            print ("No hay solucion el sistema es inconsitente")
            return 0,0,"No hay solucion el sistema es inconsitente"
        else:
            if(metodo==True):
                X,A,sol=gaussJordan2(a,b)
                """ print(X)
                print(A) """
                return X,A,sol
            else:
                X,A,sol=gaussJordan(a,b)
                """ print(X)
                print(A) """
                return X,A,sol
        
def gaussJordan2(matriz, vector):
    solucion=""
    print (matriz)
    print (vector)
    
    a=np.array(matriz,float)
    print("MATRIZ DE COEFICIENTES INICIAL")
    solucion += "MATRIZ DE COEFICIENTES INICIAL \n"+str(a)+"\n"
    print(a)
    b=np.array(vector,float)
    print("VECTOR DE RESULTADO INICIAL")
    solucion +="VECTOR DE RESULTADO INICIAL \n"+str(b)+"\n"
    print(b)
    
    n=len(b)
    print("NUMERO DE INCOGNITAS: "+str(n))
    solucion+="\n NUMERO DE INCOGNITAS: "+str(n)
    
    for k in range (n):
        
        if(np.fabs(a[k,k]) < 1.0e-12):
            solucion+="\nEl pivote de la primera fila es 0 por lo tanto se hace el cambio con una fila >0"
            print("El pivote de la primera fila es 0 por lo tanto se hace el cambio con una fila >0")
            for i in range(k+1,n):
                if (np.fabs(a[i,k]) > np.fabs(a[k,k])):
                    print("Fila Elejida :"+str(i+1))
                    solucion+="\nFila Elejida :"+str(i+1)
                    for j in range(k,n):
                        print("Con valores :"+str(a[i,j]))
                        solucion+="\nCon valores :"+str(a[i,j])
                        a[k,j],a[i,j]=a[i,j],a[k,j]
                    b[k],b[i]=b[i],b[k]
                    solucion+="\nNueva Matriz de coeficientes : \n"+str(a)
                    solucion+="\nNueva vector solución : \n"+str(b)
                    print(a)
                    print (b)
                    break
        
        #Division  de la fila pivote
        solucion+="\n\nEn la iteracion: "+str(k)
        print("\n En la iteracion: "+str(k))
        pivote=a[k,k]
        
        print("EL PIVOTE ES: "+str(pivote))
        solucion+="\n EL PIVOTE ES: "+str(pivote)
        
        for j in range(k,n):
            
            solucion+="\n\nDividimos los elementos de la fila: "+str(k)+" "+"sobre el pivote "+str(pivote)    
            a[k,j] /=pivote
            solucion+="\n\nLuego de la operacion: "+str(a[k,j])
        solucion+="\n Nueva matriz de coeficientes: \n"+str(a)
        b[k] /=pivote
        solucion+="\n Vector solucion luego de la op : \n"+str(b[k])
        solucion+="\nNuevo vector solucion: \n"+str(b)
        """ for i in range(k):
            print("entro")
            solucion+="\nLuego de la operacion: "+str(a[k,i]) """
        #Ciclo de elimacion
        solucion+="\n\nELIMINACION DE LAS FILAS CON VALOR DISTINTO A 0 RESPECTO AL ELEMENTO PIVOTE"
        for i in range(n):
            if(i==k or a[i,k] == 0): continue #verifico que el elemento no sea de la diagonal o sea 0
            
            factor=a[i,k]
            solucion+="\nFactor para la eliminación: "+str(factor)
            for j in range(k,n):
                solucion+="\nNuevo Elemento"+"="+str(a[i,j])+"-"+str(factor)+"*"+str(a[k,j])
                a[i,j] -=factor*a[k,j]
                
                solucion+="\nLuego de la operación: "+str(a[i,j])
            b[i]-=factor*b[k]
    return b,a,solucion
    
def gaussJordan(matriz, vector):
    solucion=""
    matrix = np.array(matriz, dtype=np.float64)
    vector = np.array(vector, dtype=np.float64)

    print("MATRIZ DE COEFICIENTES INICIAL")
    solucion+="MATRIZ DE COEFICIENTES INICIAL\n"+str(matrix)
    
    
    m = len(vector)# numero de incognitas en el sistema
    x = np.zeros(m)# Creo un arreglo para el resultado inicialmente con 0s

    for k in range(0, m):
        for r in range(k+1, m):
            factor=(matrix[r,k]/matrix[k,k])
            print("Factor"+str(factor))
            print(matrix[r,k],matrix[k,k])
            vector[r]=vector[r]-(factor*vector[k])
            print("Vector[r] "+str(vector[r]))
            for c in range(0,m):
                matrix[r,c]=matrix[r,c]-(factor*matrix[k,c])
                print("Matriz r,c "+str(matrix[r,c]))
    print(matrix)
    
    x[m-1]=vector[m-1]/matrix[m-1, m-1]
    print(x[m-1])
    for r in range(m-2, -1, -1):#Hago un ciclo en reversa, para eliminar todos los terminos a la derecha
        suma = 0                # de la diagonal
        for c in range(0,m):
            suma=suma+matrix[r,c]*x[c]
            print(str(matrix[r,c])+"  xc"+str(x[c]))
        x[r]=(vector[r]-suma)/matrix[r, r]

    return x,matrix,solucion

#lista_inicial([0,1,3,4,5,6])
""" orden=input("Orden del sistema :")
lista=[]
if(orden == "2"):
    pedirVal(6)
    matriz=np.reshape(lista,(2,3))
    #a=np.reshape(matriz,(2,2))
    b=matriz[:,2] #Igual de la ecuacion
    a=np.delete(matriz,2,axis=1)# Matriz de coeficientes
    #print(b)
    #print(a)
    
    if (np.linalg.det(a)==0):
        print ("No hay solucion el sistema es inconsitente")
    else:
        print ("Aqui va la sol")
        X,A=gaussJordan2(a,b)
       
        #print(gaussJordan(a,b))
elif(orden == "3"):
    pedirVal(12)
    matriz=np.reshape(lista,(3,4))
    b=matriz[:,3]
    a=np.delete(matriz,3,axis=1)
    if (np.linalg.det(a)==0):
        print ("No hay solucion el sistema es inconsitente")
    else:
        print ("SOLUCION DEL SISTEMA")
        X,A=gaussJordan2(a,b)
        print(X)
        print(A)
elif(orden == "4"):
    pedirVal(20)      
    matriz=np.reshape(lista,(4,5))
    b=matriz[:,4]
    a=np.delete(matriz,4,axis=1)
    if (np.linalg.det(a)==0):
        print ("No hay solucion el sistema es inconsitente")
    else:
        print ("Aqui va la sol")
        #print(gaussJordan(a,b))
        X,A=gaussJordan2(a,b)
        print(X)
        print(A)
elif(orden == "5"):
    pedirVal(30)      
    matriz=np.reshape(lista,(5,6))
    b=matriz[:,5]
    a=np.delete(matriz,5,axis=1)
    if (np.linalg.det(a)==0):
        print ("No hay solucion el sistema es inconsitente")
    else:
        print ("Aqui va la sol")
        X,A=gaussJordan2(a,b)
        print(X)
        print(A) """
#lista_inicial(float([1,2,3,4,5,6]))