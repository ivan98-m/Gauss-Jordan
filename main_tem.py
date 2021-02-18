import sys
import numpy as np
from PyQt5.QtWidgets  import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCloseEvent
from gauusj import gaussJordan2, lista_inicial
from interfaz.Principal11_ui import *
from pythonsrc.validar_campos import Validar
from pythonsrc.graficar_2D import graficar_2d

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.validar=Validar(self.imprimir_ecuaciones)
        self.lista= self.validar.lista2
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.gaussjordan.clicked.connect(lambda:self.seleccion(self.gaussjordan))#envia el nombre del boton selccionado
        #self.otrometodo.clicked.connect(lambda:self.seleccion(self.otrometodo))
        #self.abrir_2x2()
    
    def gaussJordan2(matriz, vector):
    
        
        a=np.array(matriz,float)
        print("MATRIZ DE COEFICIENTES INICIAL")
        print(a)
        b=np.array(vector,float)
        print("VECTOR DE RESULTADO INICIAL")
        print(b)
        
        n=len(b)
        print("NUMERO DE INCOGNITAS: "+str(n))
        
        
        for k in range (n):
            
            if(np.fabs(a[k,k]) < 1.0e-12):
                for i in range(k+1,n):
                    if (np.fabs(a[i,k]) > np.fabs(a[k,k])):
                        for j in range(k,n):
                            a[k,j],a[i,j]=a[i,j],a[k,j]
                        b[k],b[i]=b[i],b[k]
                        break
            
            #Division  de la fila pivote
            pivote=a[k,k]
            for j in range(k,n):
                a[k,j] /=pivote
            b[k] /=pivote
            #Ciclo de elimacion
            for i in range(n):
                if(i==k or a[i,k] == 0): continue #verifico que el elemento no sea de la diagonal o sea 0
                factor=a[i,k]
                for j in range(k,n):
                    a[i,j] -=factor*a[k,j]
                b[i]-=factor*b[k]
        return b,a
    
    def seleccion(self, nom):
        self.metodo = nom.text()
        print(self.metodo)
        self.comboBox.activated[str].connect(self.validar_dimension_matriz)#envia el nombre de el item seleccionado

    def validar_dimension_matriz(self, text):
        if (text == "2x2"):
            #self.validar.lista2
            self.abrir_2x2()
        elif (text == "3x3"):
            self.abrir_3x3()
        elif (text == "4x4"):
            print("4x4")
        elif (text == "5x5"):
            print("5x5")

    def abrir_2x2(self):
        print(self.validar.prueba)
        print("2x2")
        self.validar.abrir_interfaz_2x2()
        self.textsolucion.setText("DOBLE CLICKkkk")
        #self.textecuaciones.setText(str(matriz))
        #self.imprimir_ecuaciones()
        #self.validar.dialogo.cl

        btn=self.metodo
        self.graficar.setEnabled(True)
        self.graficar.clicked.connect(self.graficar_ecuaciones_2d)
        #self.textecuaciones.setEnabled(True)
        #ecuaciones="2 + 4 = 8 \n5 - 6 = 9"
        #self.textecuaciones.setPlainText(ecuaciones)
        if(btn == "Gauss Jordan"):
            print(btn+" seleccionado")
        elif(btn == "Otro metodo"):
            print(btn+" seleccionado")
            #self.gaussJordan2()
        
    def imprimir_ecuaciones(self):
        cad=""
        
        for i in self.validar.lista2:
        
            if i == self.validar.lista2[2] or i == self.validar.lista2[5]:
                cad +=" = "+ i
                
            else: 
                cad +=i+" + "
        stra="".join(map(str, self.validar.lista2))
        self.textecuaciones.setText(stra)
        self.textsolucion.setText("Aqui va la solucion del sistema")
        """ self.validar.lista2.append(223);
        print (self.validar.lista2) """
       
        #self.textproceso.setText((self.validar.lista2))
        X,A,txtsol=lista_inicial(self.validar.lista2)
        self.textproceso.setText(txtsol)
        self.textsolucion.setText("Matriz de coeficientes"+"\n"+str(A)+"\n"
                                    "Solucion: "+"\n"+str(X))
    def graficar_ecuaciones_2d(self):
        print("valores mandados para graficar")
        for i in self.validar.lista2:
            print(i)
        graficar_2d(self.validar.lista2)

    def abrir_3x3(self):
        print("#Dimencion de matriz 3x3")
        
    

    """ def pedirVal(orden):
        for i in range(orden):
            lista.append(int(input("Valor :"+str(i+1)+" "))) """
        
    
    
    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.setStyleSheet(open("style.qss", "r").read())
    window.show()
    app.exec_()