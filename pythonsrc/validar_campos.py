import sys,re
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDialog
from PyQt5 import QtWidgets

from interfaz.Principal11_ui import Ui_MainWindow
from interfaz.DosVar_ui import Ui_DosVariables
from interfaz.TresVar_ui import Ui_TresVariables
from interfaz.CuatroVar_ui import Ui_CuatroVariables
from interfaz.CincoVar_ui import Ui_CincoVariables
from pythonsrc.graficar_2D import graficar_2d

import numpy as np

class Validar(QDialog):
    def __init__(self, evento_cierre):
        super(Validar, self).__init__()
        self.matriz = [[]]
        self.lista2 = []
        #self.lista3 = []
        self.dimencion=""
	# eevento_cierre para imprimir las ecuaciones     	
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
    
    def abrir_interfaz_4x4(self):
        self.dialogo=QDialog()
        self.ui_cuatro=Ui_CuatroVariables()
        self.ui_cuatro.setupUi(self.dialogo)
        self.dialogo.show()
        self.dimencion="4x4"

        self.tam= self.ui_cuatro
        self.ui_cuatro.x1.textChanged.connect(self.validar_x1)
        self.ui_cuatro.y1.textChanged.connect(self.validar_y1)
        self.ui_cuatro.z1.textChanged.connect(self.validar_z1)
        self.ui_cuatro.w1.textChanged.connect(self.validar_w1)
        self.ui_cuatro.x.textChanged.connect(self.validar_x)
        self.ui_cuatro.x2.textChanged.connect(self.validar_x2)
        self.ui_cuatro.y2.textChanged.connect(self.validar_y2)
        self.ui_cuatro.z2.textChanged.connect(self.validar_z2)
        self.ui_cuatro.w2.textChanged.connect(self.validar_w2)
        self.ui_cuatro.y.textChanged.connect(self.validar_y)
        self.ui_cuatro.x3.textChanged.connect(self.validar_x3)
        self.ui_cuatro.y3.textChanged.connect(self.validar_y3)
        self.ui_cuatro.z3.textChanged.connect(self.validar_z3)
        self.ui_cuatro.w3.textChanged.connect(self.validar_z3)
        self.ui_cuatro.z.textChanged.connect(self.validar_z)
        self.ui_cuatro.x4.textChanged.connect(self.validar_x4)
        self.ui_cuatro.y4.textChanged.connect(self.validar_y4)
        self.ui_cuatro.z4.textChanged.connect(self.validar_z4)
        self.ui_cuatro.w4.textChanged.connect(self.validar_w4)
        self.ui_cuatro.w.textChanged.connect(self.validar_w)

        self.ui_cuatro.calcular.clicked.connect(self.validar_formulario4)

    def abrir_interfaz_5x5(self):
        self.dialogo=QDialog()
        self.ui_cinco=Ui_CincoVariables()
        self.ui_cinco.setupUi(self.dialogo)
        self.dialogo.show()
        self.dimencion="5x5"

        self.tam= self.ui_cinco
        self.ui_cinco.x1.textChanged.connect(self.validar_x1)
        self.ui_cinco.y1.textChanged.connect(self.validar_y1)
        self.ui_cinco.z1.textChanged.connect(self.validar_z1)
        self.ui_cinco.w1.textChanged.connect(self.validar_w1)
        self.ui_cinco.v1.textChanged.connect(self.validar_v1)
        self.ui_cinco.x.textChanged.connect(self.validar_x)
        self.ui_cinco.x2.textChanged.connect(self.validar_x2)
        self.ui_cinco.y2.textChanged.connect(self.validar_y2)
        self.ui_cinco.z2.textChanged.connect(self.validar_z2)
        self.ui_cinco.w2.textChanged.connect(self.validar_w2)
        self.ui_cinco.v2.textChanged.connect(self.validar_v2)
        self.ui_cinco.y.textChanged.connect(self.validar_y)
        self.ui_cinco.x3.textChanged.connect(self.validar_x3)
        self.ui_cinco.y3.textChanged.connect(self.validar_y3)
        self.ui_cinco.z3.textChanged.connect(self.validar_z3)
        self.ui_cinco.w3.textChanged.connect(self.validar_z3)
        self.ui_cinco.v3.textChanged.connect(self.validar_v3)
        self.ui_cinco.z.textChanged.connect(self.validar_z)
        self.ui_cinco.x4.textChanged.connect(self.validar_x4)
        self.ui_cinco.y4.textChanged.connect(self.validar_y4)
        self.ui_cinco.z4.textChanged.connect(self.validar_z4)
        self.ui_cinco.w4.textChanged.connect(self.validar_w4)
        self.ui_cinco.v4.textChanged.connect(self.validar_v4)
        self.ui_cinco.w.textChanged.connect(self.validar_w)
        self.ui_cinco.x5.textChanged.connect(self.validar_x5)
        self.ui_cinco.y5.textChanged.connect(self.validar_y5)
        self.ui_cinco.z5.textChanged.connect(self.validar_z5)
        self.ui_cinco.w5.textChanged.connect(self.validar_w5)
        self.ui_cinco.v5.textChanged.connect(self.validar_v5)
        self.ui_cinco.v.textChanged.connect(self.validar_v)

        self.ui_cinco.calcular.clicked.connect(self.validar_formulario5)

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

    def validar_w1(self):
        w1=self.tam.w1.text()
        if w1 == "":
            self.tam.w1.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.w1.setStyleSheet("border: 1px solid green;")
            return True

    def validar_v1(self):
        v1=self.tam.v1.text()
        if v1 == "":
            self.tam.v1.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.v1.setStyleSheet("border: 1px solid green;")
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
    
    def validar_w2(self):
        w2=self.tam.w2.text()
        if w2 == "":
            self.tam.w2.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.w2.setStyleSheet("border: 1px solid green;")
            return True

    def validar_v2(self):
        v2=self.tam.v2.text()
        if v2 == "":
            self.tam.v2.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.v2.setStyleSheet("border: 1px solid green;")
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

    def validar_w3(self):
        w3=self.tam.w3.text()
        if w3 == "":
            self.tam.w3.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.w3.setStyleSheet("border: 1px solid green;")
            return True
        
    def validar_v3(self):
        v3=self.tam.v3.text()
        if v3 == "":
            self.tam.v3.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.v3.setStyleSheet("border: 1px solid green;")
            return True

    def validar_z(self):
        z=self.tam.z.text()
        if z == "":
            self.tam.z.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.z.setStyleSheet("border: 1px solid green;")
            return True

    def validar_x4(self):
        x4=self.tam.x4.text()
        if x4 == "":
            self.tam.x4.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.x4.setStyleSheet("border: 1px solid green;")
            return True

    def validar_y4(self):
        y4=self.tam.y4.text()
        if y4 == "":
            self.tam.y4.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.y4.setStyleSheet("border: 1px solid green;")
            return True

    def validar_z4(self):
        z4=self.tam.z4.text()
        if z4 == "":
            self.tam.z4.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.z4.setStyleSheet("border: 1px solid green;")
            return True

    def validar_w4(self):
        w4=self.tam.w4.text()
        if w4 == "":
            self.tam.w4.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.w4.setStyleSheet("border: 1px solid green;")
            return True

    def validar_v4(self):
        v4=self.tam.v4.text()
        if v4 == "":
            self.tam.v4.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.v4.setStyleSheet("border: 1px solid green;")
            return True

    def validar_w(self):
        w=self.tam.w.text()
        if w == "":
            self.tam.w.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.w.setStyleSheet("border: 1px solid green;")
            return True 
#

    def validar_x5(self):
        x5=self.tam.x5.text()
        if x5 == "":
            self.tam.x5.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.x5.setStyleSheet("border: 1px solid green;")
            return True

    def validar_y5(self):
        y5=self.tam.y5.text()
        if y5 == "":
            self.tam.y5.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.y5.setStyleSheet("border: 1px solid green;")
            return True

    def validar_z5(self):
        z5=self.tam.z5.text()
        if z5 == "":
            self.tam.z5.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.z5.setStyleSheet("border: 1px solid green;")
            return True

    def validar_w5(self):
        w5=self.tam.w5.text()
        if w5 == "":
            self.tam.w5.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.w5.setStyleSheet("border: 1px solid green;")
            return True

    def validar_v5(self):
        v5=self.tam.v5.text()
        if v5 == "":
            self.tam.v5.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.v5.setStyleSheet("border: 1px solid green;")
            return True

    def validar_v(self):
        v=self.tam.v.text()
        if v == "":
            self.tam.v.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.tam.v.setStyleSheet("border: 1px solid green;")
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

    def validar_formulario4(self):
        if (self.validar_x1() and self.validar_y1() and self.validar_z1() and self.validar_w1() and self.validar_x() and 
            self.validar_x2() and self.validar_y2() and self.validar_z2() and self.validar_w2() and self.validar_y() and
            self.validar_x3() and self.validar_y3() and self.validar_z3() and self.validar_w3() and self.validar_z() and
            self.validar_x4() and self.validar_y4() and self.validar_z4() and self.validar_w4() and self.validar_w()):
            QMessageBox.information(self, "Formulario correcto", "Validacion correcta", QMessageBox.Discard)
            self.capturavalores()
        else:
            QMessageBox.warning(self, "Formulario incorrecto", "validacion incorrecta", QMessageBox.Discard)

    def validar_formulario5(self):
        if (self.validar_x1() and self.validar_y1() and self.validar_z1() and self.validar_w1() and self.validar_v1() and self.validar_x() and 
            self.validar_x2() and self.validar_y2() and self.validar_z2() and self.validar_w2() and self.validar_v2() and self.validar_y() and
            self.validar_x3() and self.validar_y3() and self.validar_z3() and self.validar_w3() and self.validar_v3() and self.validar_z() and
            self.validar_x4() and self.validar_y4() and self.validar_z4() and self.validar_w4() and self.validar_v4() and self.validar_w() and
            self.validar_x5() and self.validar_y5() and self.validar_z5() and self.validar_w5() and self.validar_v5() and self.validar_v()):
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
            print("se guardan valores 2x2")
            self.lista2.append(self.ui_dos.x1.text())
            self.lista2.append(self.ui_dos.y1.text())
            self.lista2.append(self.ui_dos.x.text())
            self.lista2.append(self.ui_dos.x2.text())
            self.lista2.append(self.ui_dos.y2.text())
            self.lista2.append(self.ui_dos.y.text())

        elif self.dimencion == "3x3":
            print("se guardan valores 3x3")
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

        elif self.dimencion == "4x4":
            print("se guardan valores 4x4")
            self.lista2.append(self.ui_cuatro.x1.text())
            self.lista2.append(self.ui_cuatro.y1.text())
            self.lista2.append(self.ui_cuatro.z1.text())
            self.lista2.append(self.ui_cuatro.w1.text())
            self.lista2.append(self.ui_cuatro.x.text())
            self.lista2.append(self.ui_cuatro.x2.text())
            self.lista2.append(self.ui_cuatro.y2.text())
            self.lista2.append(self.ui_cuatro.z2.text())
            self.lista2.append(self.ui_cuatro.w2.text())
            self.lista2.append(self.ui_cuatro.y.text())
            self.lista2.append(self.ui_cuatro.x3.text())
            self.lista2.append(self.ui_cuatro.y3.text())
            self.lista2.append(self.ui_cuatro.z3.text())
            self.lista2.append(self.ui_cuatro.w3.text())
            self.lista2.append(self.ui_cuatro.z.text())
            self.lista2.append(self.ui_cuatro.x4.text())
            self.lista2.append(self.ui_cuatro.y4.text())
            self.lista2.append(self.ui_cuatro.z4.text())
            self.lista2.append(self.ui_cuatro.w4.text())
            self.lista2.append(self.ui_cuatro.w.text())

        elif self.dimencion == "5x5":
            print("se guardan valores 5x5")
            self.lista2.append(self.ui_cinco.x1.text())
            self.lista2.append(self.ui_cinco.y1.text())
            self.lista2.append(self.ui_cinco.z1.text())
            self.lista2.append(self.ui_cinco.w1.text())
            self.lista2.append(self.ui_cinco.v1.text())
            self.lista2.append(self.ui_cinco.x.text())
            self.lista2.append(self.ui_cinco.x2.text())
            self.lista2.append(self.ui_cinco.y2.text())
            self.lista2.append(self.ui_cinco.z2.text())
            self.lista2.append(self.ui_cinco.w2.text())
            self.lista2.append(self.ui_cinco.v2.text())
            self.lista2.append(self.ui_cinco.y.text())
            self.lista2.append(self.ui_cinco.x3.text())
            self.lista2.append(self.ui_cinco.y3.text())
            self.lista2.append(self.ui_cinco.z3.text())
            self.lista2.append(self.ui_cinco.w3.text())
            self.lista2.append(self.ui_cinco.v3.text())
            self.lista2.append(self.ui_cinco.z.text())
            self.lista2.append(self.ui_cinco.x4.text())
            self.lista2.append(self.ui_cinco.y4.text())
            self.lista2.append(self.ui_cinco.z4.text())
            self.lista2.append(self.ui_cinco.w4.text())
            self.lista2.append(self.ui_cinco.v4.text())
            self.lista2.append(self.ui_cinco.w.text())
            self.lista2.append(self.ui_cinco.x5.text())
            self.lista2.append(self.ui_cinco.y5.text())
            self.lista2.append(self.ui_cinco.z5.text())
            self.lista2.append(self.ui_cinco.w5.text())
            self.lista2.append(self.ui_cinco.v5.text())
            self.lista2.append(self.ui_cinco.v.text())
            
        #matriz=np.array(self.lista2).reshape(3,2)
        #self.matriz=matriz
        #print(self.matriz)
        #stra="".join(map(str, self.lista2))
        self.dialogo.close()
        self.evento_cierre()
        
        #self.gaussjordan.setCheckable(True)
    
        
    


        
