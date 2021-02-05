import sys,re
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDialog
from PyQt5 import QtWidgets

from interfaz.Principal11_ui import *
from interfaz.DosVar_ui import Ui_DosVariables
from interfaz.TresVar_ui import Ui_TresVariables
from pythonsrc.graficar_2D import graficar_2d

import numpy as np

class Validar(QDialog):
    def __init__(self, evento_cierre):
        super(Validar, self).__init__()
        self.matriz = [[]]
        self.lista2 = []
        self.prueba="siii"
        self.evento_cierre=evento_cierre
        #QtWidgets.QMainWindow.__init__(self)# para intasia ventana principal 
        #self.setupUi(self)
        #Ui_MainWindow.textecuaciones

    def valores_interfaz(self):
        self.abrir_interfaz_2x2()
        #print(self.matriz)

    def abrir_interfaz_2x2(self):
        self.dialogo=QDialog()
        self.ui_dos=Ui_DosVariables()
        self.ui_dos.setupUi(self.dialogo)
        self.dialogo.show()

        self.tam= self.ui_dos

        self.ui_dos.x1.textChanged.connect(self.validar_x1)
        self.ui_dos.y1.textChanged.connect(self.validar_y1)
        self.ui_dos.x.textChanged.connect(self.validar_x)
        self.ui_dos.x2.textChanged.connect(self.validar_x2)
        self.ui_dos.y2.textChanged.connect(self.validar_y2)
        self.ui_dos.y.textChanged.connect(self.validar_y)
       
        self.ui_dos.calcular.clicked.connect(self.validad_formulario)

    def validar_x1(self):
        x1=self.tam.x1.text()
        if x1 == "":
            self.tam.x1.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.x1.setStyleSheet("border: 1px solid green;")
            return True

    def validar_y1(self):
        y1=self.tam.y1.text()
        if y1 == "":
            self.tam.y1.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.y1.setStyleSheet("border: 1px solid green;")
            return True

    def validar_x(self):
        x=self.tam.x.text()
        if x == "":
            self.tam.x.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.x.setStyleSheet("border: 1px solid green;")
            return True

    def validar_x2(self):
        x2=self.tam.x2.text()
        if x2 == "":
            self.tam.x2.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.x2.setStyleSheet("border: 1px solid green;")
            return True

    def validar_y2(self):
        y2=self.tam.y2.text()
        if y2 == "":
            self.tam.y2.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.y2.setStyleSheet("border: 1px solid green;")
            return True

    def validar_y(self):
        y=self.tam.y.text()
        if y == "":
            self.tam.y.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.y.setStyleSheet("border: 1px solid green;")
            return True
    
    def validad_formulario(self):
        if (self.validar_x1() and self.validar_y1() and self.validar_x() and 
            self.validar_x2() and self.validar_y2() and self.validar_y()):
            QMessageBox.information(self, "Formulario correcto", "Validacion correcta", QMessageBox.Discard)
            self.capturavalores()
        else:
            QMessageBox.warning(self, "Formulario incorrecto", "validacion incorrecta", QMessageBox.Discard)

    def capturavalores(self):
        self.lista2.clear()
        print("valores borrados---->")
        for i in self.lista2:
            print(i)
        self.lista2.append(self.ui_dos.x1.text())
        self.lista2.append(self.ui_dos.y1.text())
        self.lista2.append(self.ui_dos.x.text())
        self.lista2.append(self.ui_dos.x2.text())
        self.lista2.append(self.ui_dos.y2.text())
        self.lista2.append(self.ui_dos.y.text())

        #matriz=np.array(self.lista2).reshape(3,2)
        #self.matriz=matriz
        #print(self.matriz)
        stra="".join(map(str, self.lista2))
        self.dialogo.close()
        self.evento_cierre()
        
        
        #self.gaussjordan.setCheckable(True)
    
        
    


        
