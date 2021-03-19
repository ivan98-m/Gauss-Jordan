import sys,re
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDialog
from PyQt5 import QtWidgets
from interfaz.Comprobar_ui import Ui_Comprobar
import numpy as np

class Comprobar(QDialog):
    def __init__(self):
        super(Comprobar, self).__init__()
        self.soluciones =''
        self.lista_ecuaciones = ''
        self.ecua1=''
        self.ecua2=''
        self.ecua3=''
        self.ecua4=''
        self.ecua5=''
        self.resulado=''

    def abrir_interfaz_comprobar(self,list_ecuaciones, list_solucion):
        self.soluciones=list_solucion
        self.lista_ecuaciones=list_ecuaciones
        #self.soluciones =list(map(float,list_solucion))
        #self.lista_ecuaciones =list(map(float,list_ecuaciones))
        #cadena=",".join(map(str,list_solucion))
        print("estamos en comprobar ecuacion " + str(self.lista_ecuaciones))
        #print(type(self.lista_ecuaciones))
        print(str(self.soluciones))
        self.dialogo=QDialog()
        self.Ui_Comp=Ui_Comprobar()
        self.Ui_Comp.setupUi(self.dialogo)
        self.dialogo.show()

        if (len(list_ecuaciones) == 6):
            print("2x2")
            self.ecua1 = np.array(list_ecuaciones[:2], dtype='float')
            self.ecua2 = np.array(list_ecuaciones[3:5], dtype='float')
            print (self.ecua2)

        if (len(list_ecuaciones) == 12):
            print("3x3")
            self.Ui_Comp.ecuacion.addItem("Ecuacion 3")
            self.ecua1 = np.array(list_ecuaciones[:3], dtype='float')
            self.ecua2 = np.array(list_ecuaciones[4:7], dtype='float')
            self.ecua3 = np.array(list_ecuaciones[8:11], dtype='float')

        if (len(list_ecuaciones) == 20):
            print("4x4")
            self.Ui_Comp.ecuacion.addItem("Ecuacion 3")
            self.Ui_Comp.ecuacion.addItem("Ecuacion 4")
            self.ecua1 = np.array(list_ecuaciones[:4], dtype='float')
            self.ecua2 = np.array(list_ecuaciones[5:9], dtype='float')
            self.ecua3 = np.array(list_ecuaciones[10:14], dtype='float')
            self.ecua4 = np.array(list_ecuaciones[15:19], dtype='float')
        
        if (len(list_ecuaciones) == 30):
            print("5x5")
            self.Ui_Comp.ecuacion.addItem("Ecuacion 3")
            self.Ui_Comp.ecuacion.addItem("Ecuacion 4")
            self.Ui_Comp.ecuacion.addItem("Ecuacion 5")
            self.ecua1 = np.array(list_ecuaciones[:5], dtype='float')
            self.ecua2 = np.array(list_ecuaciones[6:11], dtype='float')
            self.ecua3 = np.array(list_ecuaciones[12:17], dtype='float')
            self.ecua4 = np.array(list_ecuaciones[18:23], dtype='float')
            self.ecua5 = np.array(list_ecuaciones[24:29], dtype='float')

        self.Ui_Comp.ecuacion.activated.connect(self.ecuacion)
        
    def ecuacion(self, i):
        #for cont in range (self.Ui_Comp.ecuacion.count()):
            #print (self.Ui_Comp.ecuacion.itemText(cont))
        #print ("el elemto seleccionado es "+ str(i) + " seleccion cambiada "+ self.Ui_Comp.ecuacion.currentText())
        if (self.Ui_Comp.ecuacion.currentText() == "Ecuacion 1"):
            print("ecuacion 1")
            lista_multiplicacion=self.ecua1 * self.soluciones
            l =len(lista_multiplicacion)
            self.resulado = np.sum(lista_multiplicacion)
            print(lista_multiplicacion)
            self.imprimir(l,"Ecuacion 1" )

        if (self.Ui_Comp.ecuacion.currentText() == "Ecuacion 2"):
            print("ecuacion 2")
            lista_multiplicacion=self.ecua2 * self.soluciones
            l =len(lista_multiplicacion)
            self.resulado = np.sum(lista_multiplicacion)
            print(lista_multiplicacion)
            self.imprimir(l,"Ecuacion 2" )

        if (self.Ui_Comp.ecuacion.currentText() == "Ecuacion 3"):
            print("ecuacion 3")
            lista_multiplicacion=self.ecua3 * self.soluciones
            l =len(lista_multiplicacion)
            self.resulado = np.sum(lista_multiplicacion)
            print(lista_multiplicacion)
            self.imprimir(l,"Ecuacion 3" )
        
        if (self.Ui_Comp.ecuacion.currentText() == "Ecuacion 4"):
            print("ecuacion 4")
            lista_multiplicacion=self.ecua4 * self.soluciones
            l =len(lista_multiplicacion)
            self.resulado = np.sum(lista_multiplicacion)
            print(lista_multiplicacion)
            self.imprimir(l,"Ecuacion 4" )
        
        if (self.Ui_Comp.ecuacion.currentText() == "Ecuacion 5"):
            print("ecuacion 5")
            lista_multiplicacion=self.ecua5 * self.soluciones
            l =len(lista_multiplicacion)
            self.resulado = np.sum(lista_multiplicacion)
            print(lista_multiplicacion)
            self.imprimir(l,"Ecuacion 5" )

    def imprimir(self, l, ecua):
        if (l == 2 and ecua == "Ecuacion 1"):
            cad=("("+ str(self.lista_ecuaciones[0]) + "*" + str((round(self.soluciones[0],2)))+")"+ " + "+
            "("+ str(self.lista_ecuaciones[1]) + "*" + str((round(self.soluciones[1],2))) + ")")
        elif(l == 2 and ecua == "Ecuacion 2"):
            cad=("("+ str(self.lista_ecuaciones[3]) + "*" + str((round(self.soluciones[0],2)))+")"+ " + "+
            "("+ str(self.lista_ecuaciones[4]) + "*" + str((round(self.soluciones[1],2)))+ ")")

        elif(l == 3 and ecua == "Ecuacion 1"):
            cad=("("+ str(self.lista_ecuaciones[0]) + "*" + str((round(self.soluciones[0],2)))+")"+ " + "+
            "("+ str(self.lista_ecuaciones[1]) + "*" + str((round(self.soluciones[1],2))) + ")" + " + "+
            "("+ str(self.lista_ecuaciones[2]) + "*" + str((round(self.soluciones[2],2))) + ")")
        elif(l == 3 and ecua == "Ecuacion 2"):
            cad=("("+ str(self.lista_ecuaciones[4]) + "*" + str((round(self.soluciones[0],2)))+")"+ " + "+
            "("+ str(self.lista_ecuaciones[5]) + "*" + str((round(self.soluciones[1],2))) + ")" + " + "+
            "("+ str(self.lista_ecuaciones[6]) + "*" + str((round(self.soluciones[2],2))) + ")")
        elif(l == 3 and ecua == "Ecuacion 3"):
            cad=("("+ str(self.lista_ecuaciones[8]) + "*" + str((round(self.soluciones[0],2)))+")"+ " + "+
            "("+ str(self.lista_ecuaciones[9]) + "*" + str((round(self.soluciones[1],2))) + ")" + " + "+
            "("+ str(self.lista_ecuaciones[10]) + "*" + str((round(self.soluciones[2],2))) + ")")
                                                    
        elif(l == 4 and ecua == "Ecuacion 1"):
            cad=("("+ str(self.lista_ecuaciones[0]) + "*" + str((round(self.soluciones[0],2)))+")"+ " + "+
            "("+ str(self.lista_ecuaciones[1]) + "*" + str((round(self.soluciones[1],2))) + ")" + " + "+
            "("+ str(self.lista_ecuaciones[2]) + "*" + str((round(self.soluciones[2],2))) + ")" + " + "+
            "("+ str(self.lista_ecuaciones[3]) + "*" + str((round(self.soluciones[3],2))) + ")")
        elif(l == 4 and ecua == "Ecuacion 2"):
            cad=("("+ str(self.lista_ecuaciones[5]) + "*" + str((round(self.soluciones[0],2)))+")"+ " + "+
            "("+ str(self.lista_ecuaciones[6]) + "*" + str((round(self.soluciones[1],2))) + ")" + " + "+
            "("+ str(self.lista_ecuaciones[7]) + "*" + str((round(self.soluciones[2],2))) + ")" + " + "+
            "("+ str(self.lista_ecuaciones[8]) + "*" + str((round(self.soluciones[3],2))) + ")")
        elif(l == 4 and ecua == "Ecuacion 3"):
            cad=("("+ str(self.lista_ecuaciones[10]) + "*" + str((round(self.soluciones[0],2)))+")"+ " + "+
            "("+ str(self.lista_ecuaciones[11]) + "*" + str((round(self.soluciones[1],2))) + ")" + " + "+
            "("+ str(self.lista_ecuaciones[12]) + "*" + str((round(self.soluciones[2],2))) + ")" + " + "+
            "("+ str(self.lista_ecuaciones[13]) + "*" + str((round(self.soluciones[3],2))) + ")")
        elif(l == 4 and ecua == "Ecuacion 4"):
            cad=("("+ str(self.lista_ecuaciones[15]) + "*" + str((round(self.soluciones[0],2)))+")"+ " + "+
            "("+ str(self.lista_ecuaciones[16]) + "*" + str((round(self.soluciones[1],2))) + ")" + " + "+
            "("+ str(self.lista_ecuaciones[17]) + "*" + str((round(self.soluciones[2],2))) + ")" + " + "+
            "("+ str(self.lista_ecuaciones[18]) + "*" + str((round(self.soluciones[3],2))) + ")")
        
        elif(l == 5 and ecua == "Ecuacion 1"):
            cad=("("+ str(self.lista_ecuaciones[0]) + "*" + str((round(self.soluciones[0],2)))+")"+ " + "+
            "("+ str(self.lista_ecuaciones[1]) + "*" + str((round(self.soluciones[1],2))) + ")" + " + "+
            "("+ str(self.lista_ecuaciones[2]) + "*" + str((round(self.soluciones[2],2))) + ")" + " + "+
            "("+ str(self.lista_ecuaciones[3]) + "*" + str((round(self.soluciones[3],2))) + ")" + " + "+ 
            "("+ str(self.lista_ecuaciones[4]) + "*" + str((round(self.soluciones[4],2))) + ")")
        elif(l == 5 and ecua == "Ecuacion 2"):
            cad=("("+ str(self.lista_ecuaciones[6]) + "*" + str((round(self.soluciones[0],2)))+")"+ " + "+
            "("+ str(self.lista_ecuaciones[7]) + "*" + str((round(self.soluciones[1],2))) + ")" + " + "+
            "("+ str(self.lista_ecuaciones[8]) + "*" + str((round(self.soluciones[2],2))) + ")" + " + "+
            "("+ str(self.lista_ecuaciones[9]) + "*" + str((round(self.soluciones[2],2))) + ")" + " + "+
            "("+ str(self.lista_ecuaciones[10]) + "*" + str((round(self.soluciones[3],2))) + ")")
        elif(l == 5 and ecua == "Ecuacion 3"):
            cad=("("+ str(self.lista_ecuaciones[12]) + "*" + str((round(self.soluciones[0],2)))+")"+ " + "+
            "("+ str(self.lista_ecuaciones[13]) + "*" + str((round(self.soluciones[1],2))) + ")" + " + "+
            "("+ str(self.lista_ecuaciones[14]) + "*" + str((round(self.soluciones[2],2))) + ")" + " + "+
            "("+ str(self.lista_ecuaciones[15]) + "*" + str((round(self.soluciones[2],2))) + ")" + " + "+
            "("+ str(self.lista_ecuaciones[16]) + "*" + str((round(self.soluciones[3],2))) + ")")
        elif(l == 5 and ecua == "Ecuacion 4"):
            cad=("("+ str(self.lista_ecuaciones[18]) + "*" + str((round(self.soluciones[0],2)))+")"+ " + "+
            "("+ str(self.lista_ecuaciones[19]) + "*" + str((round(self.soluciones[1],2))) + ")" + " + "+
            "("+ str(self.lista_ecuaciones[20]) + "*" + str((round(self.soluciones[2],2))) + ")" + " + "+
            "("+ str(self.lista_ecuaciones[21]) + "*" + str((round(self.soluciones[2],2))) + ")" + " + "+
            "("+ str(self.lista_ecuaciones[22]) + "*" + str((round(self.soluciones[3],2))) + ")")
        elif(l == 5 and ecua == "Ecuacion 5"):
            cad=("("+ str(self.lista_ecuaciones[24]) + "*" + str((round(self.soluciones[0],2)))+")"+ " + "+
            "("+ str(self.lista_ecuaciones[25]) + "*" + str((round(self.soluciones[1],2))) + ")" + " + "+
            "("+ str(self.lista_ecuaciones[26]) + "*" + str((round(self.soluciones[2],2))) + ")" + " + "+
            "("+ str(self.lista_ecuaciones[27]) + "*" + str((round(self.soluciones[2],2))) + ")" + " + "+
            "("+ str(self.lista_ecuaciones[28]) + "*" + str((round(self.soluciones[3],2))) + ")")
            
        self.Ui_Comp.operaciones.setText(cad)
        self.Ui_Comp.resultado.setText(str((round(self.resulado,2))))      