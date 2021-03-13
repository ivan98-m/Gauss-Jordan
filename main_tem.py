import sys
from PyQt5.QtWidgets  import QApplication, QWidget, QPushButton, QMessageBox, QFileDialog, QPlainTextEdit
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCloseEvent, QIcon
from PyQt5.QtCore import pyqtSlot
import matplotlib.pyplot as plt
#numpy
from datetime import datetime
from interfaz.Principal11_ui import *
from pythonsrc.validar_campos import Validar
from pythonsrc.graficar_2D import graficar_2d
from pythonsrc.graficar_3D import graficar_3d
from pythonsrc.imprimir import imprimir_ecuaciones, imprimir_soluciones
from pythonsrc.gauusj import gaussJordan2, lista_inicial
from pythonsrc.comprobar_ecua import Comprobar

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.validar=Validar(self.imprimir)
        self.lista= self.validar.lista2
        self.prueba = Comprobar()
        self.path = None
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.gaussjordan.clicked.connect(lambda:self.seleccion(self.gaussjordan))#envia el nombre del boton selccionado
        #self.otrometodo.clicked.connect(lambda:self.seleccion(self.otrometodo))
        #self.abrir_2x2()
        #self.otrometodo.setEnabled(False)
        self.otrometodo.clicked.connect(lambda:self.seleccion(self.otrometodo))
    """@pyqtSlot()
    def on_click(self):#Slot creado para el boton
        fecha=datetime.now()
        file=open("Procedimiento con\n"+str(self.metodo)+str(" ")+str(fecha),"w")
        file.write(self.textproceso.toPlainText())
        file.close()"""
        
    def seleccion(self, nom):
        self.metodo = nom.text()
        print(self.metodo)
        self.comboBox.activated[str].connect(self.validar_dimension_matriz)#envia el nombre de el item seleccionado

    def validar_dimension_matriz(self, text):
        if (text == "2x2"):
            self.desactivar_botones()
            self.limpiar()
            self.abrir_2x2()
        elif (text == "3x3"):
            self.desactivar_botones()
            self.limpiar()
            self.abrir_3x3()
        elif (text == "4x4"):
            self.desactivar_botones()
            self.limpiar()
            self.abrir_4x4()
        elif (text == "5x5"):
            self.desactivar_botones()
            self.limpiar()
            self.abrir_5x5()

    def abrir_2x2(self):
        self.validar.lista2.clear()
        print("2x2")
        plt.close()
        self.validar.abrir_interfaz_2x2()
        #self.textsolucion.setText("DOBLE CLICKkkk")
        self.graficar.setEnabled(True)
        self.graficar.clicked.connect(self.graficar_ecuaciones_dosd)

        btn=self.metodo
        if(btn == "Gauss Jordan"):
            print(btn+" seleccionado")
        elif(btn == "Otro metodo"):
            print(btn+" seleccionado")
            #self.gaussJordan2()

    def abrir_3x3(self):
        self.validar.lista2.clear()
        plt.close()
        print("#Dimencion de matriz 3x3")
        self.validar.abrir_interfaz_3x3()
        #self.textsolucion.setText("SOLUCION 3 VAR 3 INCOG")
        self.graficar.setEnabled(True)
        self.graficar.clicked.connect(self.graficar_ecuaciones_tresd)

    def abrir_4x4(self):
        print("#Dimencion de matriz 4x4")
        self.graficar.setEnabled(False)
        self.validar.abrir_interfaz_4x4()
        #self.textsolucion.setText("SOLUCION MATIRCES 4 INCOG")
       
    def abrir_5x5(self):
        print("#Dimencion de matriz 5x5")
        self.graficar.setEnabled(False)
        self.validar.abrir_interfaz_5x5()
        #self.textsolucion.setText("SOLUCION MATIRCES 5 INCOG")

    def imprimir(self):
        self.guardar.setEnabled(True)
        txt_ecuaciones=imprimir_ecuaciones(self.validar.lista2)
        self.textecuaciones.setText(txt_ecuaciones)
        print(self.metodo)
        if(self.metodo=="Gauss-Jordan"):
            X,A,txtsol=lista_inicial(self.validar.lista2,True)
            self.textproceso.setText(txtsol)
            sol=imprimir_soluciones(X)
            print(sol)
            #self.textsolucion.setText("Matriz de coeficientes"+"\n"+str(A)+"\n" + "Solucion: "+"\n"+str(sol))
            self.textsolucion.setText(sol)
            self.comprobar.setEnabled(True)
            self.comprobar.clicked.connect(lambda:self.comprobar_soluciones(X))
        else:
            X,A,txtsol=lista_inicial(self.validar.lista2,False)
            self.textproceso.setText(txtsol)
            sol=imprimir_soluciones(X)
            print(sol)
            self.textsolucion.setText(sol)
            self.comprobar.setEnabled(True)
            self.comprobar.clicked.connect(lambda:self.comprobar_soluciones(X))
            #self.textsolucion.setText("Matriz de coeficientes"+"\n"+str(A)+"\n"+"Solucion: "+"\n"+str(X))
            
        self.guardar.clicked.connect(lambda:self.guardar_archivo(sol))

    def comprobar_soluciones(self, vec_solucion):
        self.prueba.abrir_interfaz_comprobar(self.validar.lista2, vec_solucion)

    def guardar_archivo(self, solucion):
        ventanaqt = QFileDialog.Options()
        ventanaqt |= QFileDialog.DontUseNativeDialog
        ruta_nombre, _ = QFileDialog.getSaveFileName(self, "Guardar Archivo...", "", "Text documents (*.txt)", options=ventanaqt)

        try:
            with open(ruta_nombre, 'wt') as f:
                fecha=datetime.now()
                soluciones="\n"+"\n"+"SOLUCION DEL SISTEMA DE ECUACIONES: "+"\n"+solucion
                cabecera ="Procedimiento con el metodo de: "+str(self.metodo)+" fecha: "+str(fecha)+"\n"+"\n"
                f.write(cabecera+self.textproceso.toPlainText()+soluciones)
            
            QMessageBox.information(self, "Guardar archivo", "Archivo guardado", QMessageBox.Discard)
        except:
            QMessageBox.warning(self, "Guardar archivo", "Archivo no guardado", QMessageBox.Discard)


    def graficar_ecuaciones_dosd(self):
        print("valores mandados para graficar 2d")
        if len(self.validar.lista2) !=0:
            for i in self.validar.lista2:
                print(i)
            graficar_2d(self.validar.lista2)
        else:
            QMessageBox.warning(self, "Formulario incorrecto", "Se deben llenar los campos", QMessageBox.Discard)

    def graficar_ecuaciones_tresd(self):
        print("valores mandados para graficar 3d")
        if len(self.validar.lista2) !=0:
            for i in self.validar.lista2:
                print(i)
            graficar_3d(self.validar.lista2)
        else:
            QMessageBox.warning(self, "Formulario incorrecto", "Se deben llenar los campos", QMessageBox.Discard)   

    def limpiar(self):
        self.textecuaciones.clear()
        self.textsolucion.clear()
        self.textproceso.clear()

    def desactivar_botones(self):
        self.graficar.setEnabled(False)
        self.comprobar.setEnabled(False)
        self.guardar.setEnabled(False)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.setStyleSheet(open("style.qss", "r").read())
    window.show()
    app.exec_()