# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DosVar.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui  import QDoubleValidator

class Ui_DosVariables(object):
    def setupUi(self, DosVariables):
        DosVariables.setObjectName("DosVariables")
        DosVariables.resize(344, 143)
        DosVariables.setStyleSheet("QWidget\n"
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
"    color: #fff;\n"
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
"}")
        self.gridLayout = QtWidgets.QGridLayout(DosVariables)
        self.gridLayout.setObjectName("gridLayout")
        self.x1 = QtWidgets.QLineEdit(DosVariables)
        self.x1.setObjectName("x1")
        self.x1.setValidator(QDoubleValidator())
        self.gridLayout.addWidget(self.x1, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(DosVariables)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.y1 = QtWidgets.QLineEdit(DosVariables)
        self.y1.setObjectName("y1")
        self.y1.setValidator(QDoubleValidator())
        self.gridLayout.addWidget(self.y1, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(DosVariables)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.x = QtWidgets.QLineEdit(DosVariables)
        self.x.setObjectName("x")
        self.x.setValidator(QDoubleValidator())
        self.gridLayout.addWidget(self.x, 0, 4, 1, 1)
        self.x2 = QtWidgets.QLineEdit(DosVariables)
        self.x2.setObjectName("x2")
        self.x2.setValidator(QDoubleValidator())
        self.gridLayout.addWidget(self.x2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(DosVariables)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.y2 = QtWidgets.QLineEdit(DosVariables)
        self.y2.setObjectName("y2")
        self.y2.setValidator(QDoubleValidator())
        self.gridLayout.addWidget(self.y2, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(DosVariables)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 3, 1, 1)
        self.y = QtWidgets.QLineEdit(DosVariables)
        self.y.setObjectName("y")
        self.y.setValidator(QDoubleValidator())
        self.gridLayout.addWidget(self.y, 1, 4, 1, 1)
        self.calcular = QtWidgets.QPushButton(DosVariables)
        self.calcular.setObjectName("calcular")
        self.gridLayout.addWidget(self.calcular, 2, 4, 1, 1)

        self.retranslateUi(DosVariables)
        QtCore.QMetaObject.connectSlotsByName(DosVariables)

    def retranslateUi(self, DosVariables):
        _translate = QtCore.QCoreApplication.translate
        DosVariables.setWindowTitle(_translate("DosVariables", "2x2"))
        self.label.setText(_translate("DosVariables", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#0000ff;\">x </span><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">+</span></p></body></html>"))
        self.label_2.setText(_translate("DosVariables", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#0000ff;\">y </span><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">=</span></p></body></html>"))
        self.label_4.setText(_translate("DosVariables", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#0000ff;\">x </span><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">+</span></p></body></html>"))
        self.label_3.setText(_translate("DosVariables", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#0000ff;\">y </span><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">=</span></p></body></html>"))
        self.calcular.setText(_translate("DosVariables", "Calcular"))
