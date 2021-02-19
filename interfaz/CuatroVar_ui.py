# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CuatroVar.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CuatroVariables(object):
    def setupUi(self, CuatroVariables):
        CuatroVariables.setObjectName("CuatroVariables")
        CuatroVariables.resize(504, 173)
        CuatroVariables.setStyleSheet("QWidget\n"
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
        self.gridLayout = QtWidgets.QGridLayout(CuatroVariables)
        self.gridLayout.setObjectName("gridLayout")
        self.x1 = QtWidgets.QLineEdit(CuatroVariables)
        self.x1.setObjectName("x1")
        self.gridLayout.addWidget(self.x1, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(CuatroVariables)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.y1 = QtWidgets.QLineEdit(CuatroVariables)
        self.y1.setObjectName("y1")
        self.gridLayout.addWidget(self.y1, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(CuatroVariables)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.z1 = QtWidgets.QLineEdit(CuatroVariables)
        self.z1.setObjectName("z1")
        self.gridLayout.addWidget(self.z1, 0, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(CuatroVariables)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 5, 1, 1)
        self.w1 = QtWidgets.QLineEdit(CuatroVariables)
        self.w1.setObjectName("w1")
        self.gridLayout.addWidget(self.w1, 0, 6, 1, 1)
        self.label_12 = QtWidgets.QLabel(CuatroVariables)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 7, 1, 1)
        self.x = QtWidgets.QLineEdit(CuatroVariables)
        self.x.setObjectName("x")
        self.gridLayout.addWidget(self.x, 0, 8, 1, 1)
        self.x2 = QtWidgets.QLineEdit(CuatroVariables)
        self.x2.setObjectName("x2")
        self.gridLayout.addWidget(self.x2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(CuatroVariables)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.y2 = QtWidgets.QLineEdit(CuatroVariables)
        self.y2.setObjectName("y2")
        self.gridLayout.addWidget(self.y2, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(CuatroVariables)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 3, 1, 1)
        self.z2 = QtWidgets.QLineEdit(CuatroVariables)
        self.z2.setObjectName("z2")
        self.gridLayout.addWidget(self.z2, 1, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(CuatroVariables)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 5, 1, 1)
        self.w2 = QtWidgets.QLineEdit(CuatroVariables)
        self.w2.setObjectName("w2")
        self.gridLayout.addWidget(self.w2, 1, 6, 1, 1)
        self.label_10 = QtWidgets.QLabel(CuatroVariables)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 7, 1, 1)
        self.y = QtWidgets.QLineEdit(CuatroVariables)
        self.y.setObjectName("y")
        self.gridLayout.addWidget(self.y, 1, 8, 1, 1)
        self.x3 = QtWidgets.QLineEdit(CuatroVariables)
        self.x3.setObjectName("x3")
        self.gridLayout.addWidget(self.x3, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(CuatroVariables)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
        self.y3 = QtWidgets.QLineEdit(CuatroVariables)
        self.y3.setObjectName("y3")
        self.gridLayout.addWidget(self.y3, 2, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(CuatroVariables)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 3, 1, 1)
        self.z3 = QtWidgets.QLineEdit(CuatroVariables)
        self.z3.setObjectName("z3")
        self.gridLayout.addWidget(self.z3, 2, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(CuatroVariables)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 5, 1, 1)
        self.w3 = QtWidgets.QLineEdit(CuatroVariables)
        self.w3.setObjectName("w3")
        self.gridLayout.addWidget(self.w3, 2, 6, 1, 1)
        self.label_11 = QtWidgets.QLabel(CuatroVariables)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 7, 1, 1)
        self.z = QtWidgets.QLineEdit(CuatroVariables)
        self.z.setObjectName("z")
        self.gridLayout.addWidget(self.z, 2, 8, 1, 1)
        self.x4 = QtWidgets.QLineEdit(CuatroVariables)
        self.x4.setObjectName("x4")
        self.gridLayout.addWidget(self.x4, 3, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(CuatroVariables)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 3, 1, 1, 1)
        self.y4 = QtWidgets.QLineEdit(CuatroVariables)
        self.y4.setObjectName("y4")
        self.gridLayout.addWidget(self.y4, 3, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(CuatroVariables)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 3, 3, 1, 1)
        self.z4 = QtWidgets.QLineEdit(CuatroVariables)
        self.z4.setObjectName("z4")
        self.gridLayout.addWidget(self.z4, 3, 4, 1, 1)
        self.label_13 = QtWidgets.QLabel(CuatroVariables)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 3, 5, 1, 1)
        self.w4 = QtWidgets.QLineEdit(CuatroVariables)
        self.w4.setObjectName("w4")
        self.gridLayout.addWidget(self.w4, 3, 6, 1, 1)
        self.label_16 = QtWidgets.QLabel(CuatroVariables)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 3, 7, 1, 1)
        self.w = QtWidgets.QLineEdit(CuatroVariables)
        self.w.setObjectName("w")
        self.gridLayout.addWidget(self.w, 3, 8, 1, 1)
        self.calcular = QtWidgets.QPushButton(CuatroVariables)
        self.calcular.setObjectName("calcular")
        self.gridLayout.addWidget(self.calcular, 4, 8, 1, 1)

        self.retranslateUi(CuatroVariables)
        QtCore.QMetaObject.connectSlotsByName(CuatroVariables)

    def retranslateUi(self, CuatroVariables):
        _translate = QtCore.QCoreApplication.translate
        CuatroVariables.setWindowTitle(_translate("CuatroVariables", "4x4"))
        self.label.setText(_translate("CuatroVariables", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#0000ff;\">x </span><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">+</span></p></body></html>"))
        self.label_2.setText(_translate("CuatroVariables", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#0000ff;\">y </span><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">+</span></p></body></html>"))
        self.label_5.setText(_translate("CuatroVariables", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#0000ff;\">z </span><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">+</span></p></body></html>"))
        self.label_12.setText(_translate("CuatroVariables", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#0000ff;\">w </span><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">=</span></p></body></html>"))
        self.label_4.setText(_translate("CuatroVariables", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#0000ff;\">x </span><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">+</span></p></body></html>"))
        self.label_3.setText(_translate("CuatroVariables", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#0000ff;\">y </span><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">+</span></p></body></html>"))
        self.label_6.setText(_translate("CuatroVariables", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#0000ff;\">z </span><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">+</span></p></body></html>"))
        self.label_10.setText(_translate("CuatroVariables", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#0000ff;\">w </span><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">=</span></p></body></html>"))
        self.label_7.setText(_translate("CuatroVariables", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#0000ff;\">x </span><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">+</span></p></body></html>"))
        self.label_9.setText(_translate("CuatroVariables", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#0000ff;\">y </span><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">+</span></p></body></html>"))
        self.label_8.setText(_translate("CuatroVariables", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#0000ff;\">z </span><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">+</span></p></body></html>"))
        self.label_11.setText(_translate("CuatroVariables", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#0000ff;\">w </span><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">=</span></p></body></html>"))
        self.label_14.setText(_translate("CuatroVariables", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#0000ff;\">x </span><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">+</span></p></body></html>"))
        self.label_15.setText(_translate("CuatroVariables", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#0000ff;\">y </span><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">+</span></p></body></html>"))
        self.label_13.setText(_translate("CuatroVariables", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#0000ff;\">z </span><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">+</span></p></body></html>"))
        self.label_16.setText(_translate("CuatroVariables", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#0000ff;\">w </span><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">=</span></p></body></html>"))
        self.calcular.setText(_translate("CuatroVariables", "Calcular"))