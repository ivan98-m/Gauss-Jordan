import sys
import numpy as np
from PyQt5.QtWidgets  import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCloseEvent
import matplotlib.pyplot as plt

from interfaz.Principal11_ui import *
from pythonsrc.validar_campos import Validar
from pythonsrc.graficar_2D import graficar_2d
from pythonsrc.graficar_3D import graficar_3d
from pythonsrc.imprimir import imprimir_txt_ecuaciones
from pythonsrc.gauusj import gaussJordan2, lista_inicial
from pythonsrc.comprobar_ecua import Comprobar

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.validar=Validar(self.imprimir)
        self.lista= self.validar.lista2
        self.prueba = Comprobar()
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.gaussjordan.clicked.connect(lambda:self.seleccion(self.gaussjordan))#envia el nombre del boton selccionado
        #self.otrometodo.clicked.connect(lambda:self.seleccion(self.otrometodo))
        #self.abrir_2x2()
        #self.otrometodo.setEnabled(False)
        self.otrometodo.clicked.connect(lambda:self.seleccion(self.otrometodo))
    
    def seleccion(self, nom):
        self.metodo = nom.text()
        print(self.metodo)
        self.comboBox.activated[str].connect(self.validar_dimension_matriz)#envia el nombre de el item seleccionado

    def validar_dimension_matriz(self, text):
        if (text == "2x2"):
            self.limpiar()
            self.abrir_2x2()
        elif (text == "3x3"):
            self.limpiar()
            self.abrir_3x3()
        elif (text == "4x4"):
            self.limpiar()
            self.abrir_4x4()
        elif (text == "5x5"):
            self.limpiar()
            self.abrir_5x5()

    def abrir_2x2(self):
        print("2x2")
        #self.graficar = QPushButton('Clear', self)
        self.validar.abrir_interfaz_2x2()
        self.textsolucion.setText("DOBLE CLICKkkk")
        #self.textecuaciones.setText(str(matriz))
        #self.imprimir_ecuaciones()
        #self.validar.dialogo.cl
        self.graficar.setEnabled(True)
        self.graficar.clicked.connect(self.graficar_ecuaciones_dosd)
        btn=self.metodo
        #self.textecuaciones.setEnabled(True)
        #ecuaciones="2 + 4 = 8 \n5 - 6 = 9"
        #self.textecuaciones.setPlainText(ecuaciones)
        if(btn == "Gauss Jordan"):
            print(btn+" seleccionado")
        elif(btn == "Otro metodo"):
            print(btn+" seleccionado")
            #self.gaussJordan2()
            
    def graficar_ecuaciones_2d(self):
        print("valores mandados para graficar")
        for i in self.validar.lista2:
            print(i)
        graficar_2d(self.validar.lista2)

    def abrir_3x3(self):
        print("#Dimencion de matriz 3x3")
        self.validar.abrir_interfaz_3x3()
        self.textsolucion.setText("SOLUCION 3 VAR 3 INCOG")
        #self.graficar.setEnabled(True)
        self.graficar.setEnabled(True)
        self.graficar.clicked.connect(self.graficar_ecuaciones_tresd)

    def abrir_4x4(self):
        print("#Dimencion de matriz 4x4")
        self.graficar.setEnabled(False)
        self.validar.abrir_interfaz_4x4()
        self.textsolucion.setText("SOLUCION MATIRCES 4 INCOG")
       
    def abrir_5x5(self):
        print("#Dimencion de matriz 5x5")
        self.graficar.setEnabled(False)
        self.validar.abrir_interfaz_5x5()
        self.textsolucion.setText("SOLUCION MATIRCES 5 INCOG")

    def imprimir(self):
        txt_ecuaciones=imprimir_txt_ecuaciones(self.validar.lista2)
        self.textecuaciones.setText(txt_ecuaciones)
        print(self.metodo)
        if(self.metodo=="Gauss_Jordan"):
            X,A,txtsol=lista_inicial(self.validar.lista2,True)
            self.textproceso.setText(txtsol)
            self.textsolucion.setText("Matriz de coeficientes"+"\n"+str(A)+"\n"
                                        "Solucion: "+"\n"+str(X))
            self.comprobar.setEnabled(True)
            self.comprobar.clicked.connect(lambda:self.comprobar_soluciones(X))
        else:
            X,A,txtsol=lista_inicial(self.validar.lista2,False)
            self.textproceso.setText(txtsol)
            self.textsolucion.setText("Matriz de coeficientes"+"\n"+str(A)+"\n"
                                        "Solucion: "+"\n"+str(X))
            """ cadena="-".join(map(str,self.validar.lista2))
            self.textecuaciones.setText(cadena) """

    def comprobar_soluciones(self, vec_solucion):
        self.prueba.abrir_interfaz_comprobar(self.validar.lista2, vec_solucion)

    def graficar_ecuaciones_dosd(self):
        plt.close("all")
        print("valores mandados para graficar 2d")
        if len(self.validar.lista2) !=0:
            for i in self.validar.lista2:
                print(i)
            graficar_2d(self.validar.lista2)
        else:
            QMessageBox.warning(self, "Formulario incorrecto", "validacion incorrecta", QMessageBox.Discard)

    def graficar_ecuaciones_tresd(self):
        plt.close("all")
        print("valores mandados para graficar 3d")
        if len(self.validar.lista2) !=0:
            for i in self.validar.lista2:
                print(i)
            graficar_3d(self.validar.lista2)
        else:
            QMessageBox.warning(self, "Formulario incorrecto", "validacion incorrecta", QMessageBox.Discard)   

    def limpiar(self):
        self.textecuaciones.clear()
        self.textsolucion.clear()

    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.setStyleSheet(open("style.qss", "r").read())
    window.show()
    app.exec_()