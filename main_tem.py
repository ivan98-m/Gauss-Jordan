import sys
from PyQt5.QtWidgets  import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCloseEvent

from interfaz.Principal11_ui import *
from pythonsrc.validar_campos import Validar
from pythonsrc.graficar_2D import graficar_2d
from pythonsrc.graficar_3D import graficar_3d

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.validar=Validar(self.imprimir_ecuaciones)
        self.lista= self.validar.lista2
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.gaussjordan.clicked.connect(lambda:self.seleccion(self.gaussjordan))#envia el nombre del boton selccionado
        #self.otrometodo.clicked.connect(lambda:self.seleccion(self.otrometodo))
        #self.abrir_2x2()
    
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
            self.abrir_4x4()
        elif (text == "5x5"):
            print("5x5")

    def abrir_2x2(self):
        print("2x2")
        self.validar.abrir_interfaz_2x2()
        self.textsolucion.setText("DOBLE CLICKkkk")
        #self.textecuaciones.setText(str(matriz))
        #self.imprimir_ecuaciones()
        #self.validar.dialogo.cl
        self.graficar.setEnabled(True)
        self.graficar.clicked.connect(self.graficar_ecuaciones_2d)
        btn=self.metodo
        #self.textecuaciones.setEnabled(True)
        #ecuaciones="2 + 4 = 8 \n5 - 6 = 9"
        #self.textecuaciones.setPlainText(ecuaciones)
        if(btn == "Gauss Jordan"):
            print(btn+" seleccionado")
        elif(btn == "Otro metodo"):
            print(btn+" seleccionado")

    def abrir_3x3(self):
        print("#Dimencion de matriz 3x3")
        self.validar.abrir_interfaz_3x3()
        self.textsolucion.setText("SOLUCION 3 VAR 3 INCOG")
        #self.graficar.setEnabled(True)
        self.graficar.setEnabled(True)
        self.graficar.clicked.connect(self.graficar_ecuaciones_3d)

    def abrir_4x4(self):
        self.graficar.setEnabled(False)
        print("#Dimencion de matriz 4x4")

    def imprimir_ecuaciones(self):
        cad=""
        for i in self.validar.lista2:
            if i == self.validar.lista2[2] or i == self.validar.lista2[5]:
                cad +=" = "+ i
            else: 
                cad +=i+" + "
        stra="".join(map(str, self.validar.lista2))
        self.textecuaciones.setText(stra)

    def graficar_ecuaciones_2d(self):
        print("valores mandados para graficar")
        for i in self.validar.lista2:
            print(i)
        graficar_2d(self.validar.lista2)

    def graficar_ecuaciones_3d(self):
        print("valores mandados para graficar")
        for i in self.validar.lista2:
            print(i)
        graficar_3d(self.validar.lista2)

    def limpiar(self):
        self.textecuaciones.clear()
        self.textsolucion.clear()
    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.setStyleSheet(open("style.qss", "r").read())
    window.show()
    app.exec_()