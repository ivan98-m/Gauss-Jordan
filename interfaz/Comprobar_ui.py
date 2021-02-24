# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Comprobar.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Comprobar(object):
    def setupUi(self, Comprobar):
        Comprobar.setObjectName("Comprobar")
        Comprobar.resize(407, 127)
        Comprobar.setStyleSheet("QWidget\n"
"{\n"
"    background-color: #e4e4e4;\n"
"    color: #000;\n"
"    selection-background-color: #46a2da;\n"
"    selection-color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #000;\n"
"\n"
"}\n"
"QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184, 184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"    color: #000;\n"
"    min-width: 80px;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: #051a39;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::flat\n"
"{\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"    background-color: #606060;\n"
"    color: #959595;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"    background-color: rgba(70,162,218,50%);\n"
"    border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(174, 174, 174, 255),stop:1 rgba(149, 149, 149, 255));\n"
"    border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::checked\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(174, 174, 174, 255),stop:1 rgba(149, 149, 149, 255));\n"
"    border: 1px solid #222;\n"
"\n"
"}\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"    background-color: #f6f6f6;\n"
"    color : #000;\n"
"    border: 1px solid #343434;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"\n"
"}\n"
"/*-----QComboBox-----*/\n"
"QComboBox\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184, 184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"    border: 1px solid #000;\n"
"    padding-left: 6px;\n"
"    color: #000;\n"
"    height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #46a2da;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #383838;\n"
"    color: #ffffff;\n"
"    border: 1px solid black;\n"
"    selection-background-color: #46a2da;\n"
"    outline: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.resultado = QtWidgets.QLineEdit(Comprobar)
        self.resultado.setGeometry(QtCore.QRect(320, 70, 71, 24))
        self.resultado.setReadOnly(True)
        self.resultado.setObjectName("resultado")
        self.ecuacion = QtWidgets.QComboBox(Comprobar)
        self.ecuacion.setGeometry(QtCore.QRect(215, 30, 181, 22))
        self.ecuacion.setObjectName("ecuacion")
        self.ecuacion.addItem("")
        self.ecuacion.addItem("")
        self.label = QtWidgets.QLabel(Comprobar)
        self.label.setGeometry(QtCore.QRect(9, 30, 192, 16))
        self.label.setObjectName("label")
        self.operaciones = QtWidgets.QLineEdit(Comprobar)
        self.operaciones.setGeometry(QtCore.QRect(9, 70, 281, 24))
        self.operaciones.setText("")
        self.operaciones.setReadOnly(True)
        self.operaciones.setObjectName("operaciones")
        self.label_2 = QtWidgets.QLabel(Comprobar)
        self.label_2.setGeometry(QtCore.QRect(300, 70, 16, 23))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Comprobar)
        QtCore.QMetaObject.connectSlotsByName(Comprobar)

    def retranslateUi(self, Comprobar):
        _translate = QtCore.QCoreApplication.translate
        Comprobar.setWindowTitle(_translate("Comprobar", "Comprobar Ecuaciones"))
        self.ecuacion.setItemText(0, _translate("Comprobar", "Ecuacion 1"))
        self.ecuacion.setItemText(1, _translate("Comprobar", "Ecuacion 2"))
        self.label.setText(_translate("Comprobar", "<html><head/><body><p><span style=\" font-size:10pt;\">Seleccione ecuacion a comprobar</span></p></body></html>"))
        self.label_2.setText(_translate("Comprobar", "<html><head/><body><p><span style=\" font-size:14pt;\">=</span></p></body></html>"))