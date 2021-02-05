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
        self.dimencion=""
        self.evento_cierre=evento_cierre
    
    def abrir_interfaz_2x2(self):
        self.dialogo=QDialog()
        self.ui_dos=Ui_DosVariables()
        self.ui_dos.setupUi(self.dialogo)
        self.dialogo.show()
        self.dimencion="2x2"

        self.tam= self.ui_dos
        self.ui_dos.x1.textChanged.connect(self.validar_x1)
        self.ui_dos.y1.textChanged.connect(self.validar_y1)
        self.ui_dos.x.textChanged.connect(self.validar_x)
        self.ui_dos.x2.textChanged.connect(self.validar_x2)
        self.ui_dos.y2.textChanged.connect(self.validar_y2)
        self.ui_dos.y.textChanged.connect(self.validar_y)
       
        self.ui_dos.calcular.clicked.connect(self.validad_formulario2)

    def abrir_interfaz_3x3(self):
        self.dialogo=QDialog()
        self.ui_tres=Ui_TresVariables()
        self.ui_tres.setupUi(self.dialogo)
        self.dialogo.show()
        self.dimencion="3x3"

        self.tam= self.ui_tres
        self.ui_tres.x1.textChanged.connect(self.validar_x1)
        self.ui_tres.y1.textChanged.connect(self.validar_y1)
        self.ui_tres.z1.textChanged.connect(self.validar_z1)
        self.ui_tres.x.textChanged.connect(self.validar_x)
        self.ui_tres.x2.textChanged.connect(self.validar_x2)
        self.ui_tres.y2.textChanged.connect(self.validar_y2)
        self.ui_tres.z2.textChanged.connect(self.validar_z2)
        self.ui_tres.y.textChanged.connect(self.validar_y)
        self.ui_tres.x3.textChanged.connect(self.validar_x3)
        self.ui_tres.y3.textChanged.connect(self.validar_y3)
        self.ui_tres.z3.textChanged.connect(self.validar_z3)
        self.ui_tres.z.textChanged.connect(self.validar_z)
       
        self.ui_tres.calcular.clicked.connect(self.validar_formulario3)

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

    def validar_z1(self):
        z1=self.tam.z1.text()
        if z1 == "":
            self.tam.z1.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.z1.setStyleSheet("border: 1px solid green;")
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

    def validar_z2(self):
        z2=self.tam.z2.text()
        if z2 == "":
            self.tam.z2.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.z2.setStyleSheet("border: 1px solid green;")
            return True

    def validar_y(self):
        y=self.tam.y.text()
        if y == "":
            self.tam.y.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.y.setStyleSheet("border: 1px solid green;")
            return True

    def validar_x3(self):
        x3=self.tam.x3.text()
        if x3 == "":
            self.tam.x3.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.x3.setStyleSheet("border: 1px solid green;")
            return True

    def validar_y3(self):
        y3=self.tam.y3.text()
        if y3 == "":
            self.tam.y3.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.y3.setStyleSheet("border: 1px solid green;")
            return True

    def validar_z3(self):
        z3=self.tam.z3.text()
        if z3 == "":
            self.tam.z3.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.z3.setStyleSheet("border: 1px solid green;")
            return True

    def validar_z(self):
        z=self.tam.z.text()
        if z == "":
            self.tam.z.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.z.setStyleSheet("border: 1px solid green;")
            return True
    
    def validad_formulario2(self):
        if (self.validar_x1() and self.validar_y1() and self.validar_x() and 
            self.validar_x2() and self.validar_y2() and self.validar_y()):
            QMessageBox.information(self, "Formulario correcto", "Validacion correcta", QMessageBox.Discard)
            self.capturavalores()
        else:
            QMessageBox.warning(self, "Formulario incorrecto", "validacion incorrecta", QMessageBox.Discard)
        
    def validar_formulario3(self):
        if (self.validar_x1() and self.validar_y1() and self.validar_z1() and self.validar_x() and 
            self.validar_x2() and self.validar_y2() and self.validar_z2() and self.validar_y() and
            self.validar_x3() and self.validar_y3() and self.validar_z3() and self.validar_z()):
            QMessageBox.information(self, "Formulario correcto", "Validacion correcta", QMessageBox.Discard)
            self.capturavalores()
        else:
            QMessageBox.warning(self, "Formulario incorrecto", "validacion incorrecta", QMessageBox.Discard)

    def capturavalores(self):
        self.lista2.clear()
        print("valores borrados---->")
        for i in self.lista2:
            print(i)
        if self.dimencion == "2x2":
            self.lista2.append(self.ui_dos.x1.text())
            self.lista2.append(self.ui_dos.y1.text())
            self.lista2.append(self.ui_dos.x.text())
            self.lista2.append(self.ui_dos.x2.text())
            self.lista2.append(self.ui_dos.y2.text())
            self.lista2.append(self.ui_dos.y.text())
        elif self.dimencion == "3x3":
            self.lista2.append(self.ui_tres.x1.text())
            self.lista2.append(self.ui_tres.y1.text())
            self.lista2.append(self.ui_tres.z1.text())
            self.lista2.append(self.ui_tres.x.text())
            self.lista2.append(self.ui_tres.x2.text())
            self.lista2.append(self.ui_tres.y2.text())
            self.lista2.append(self.ui_tres.z2.text())
            self.lista2.append(self.ui_tres.y.text())
            self.lista2.append(self.ui_tres.x3.text())
            self.lista2.append(self.ui_tres.y3.text())
            self.lista2.append(self.ui_tres.z3.text())
            self.lista2.append(self.ui_tres.z.text())
        #matriz=np.array(self.lista2).reshape(3,2)
        #self.matriz=matriz
        #print(self.matriz)
        stra="".join(map(str, self.lista2))
        self.dialogo.close()
        self.evento_cierre()
        
        
        #self.gaussjordan.setCheckable(True)
    
        
    


        
