# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Principal1.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(741, 543)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gaussjordan = QtWidgets.QRadioButton(self.centralwidget)
        self.gaussjordan.setObjectName("gaussjordan")
        self.verticalLayout.addWidget(self.gaussjordan)
        self.otrometodo = QtWidgets.QRadioButton(self.centralwidget)
        self.otrometodo.setObjectName("otrometodo")
        self.verticalLayout.addWidget(self.otrometodo)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 305, 102))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textecuaciones = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_4)
        self.textecuaciones.setEnabled(False)
        self.textecuaciones.setStyleSheet("QTextEdit{border:2px groove #242424;}")
        self.textecuaciones.setObjectName("textecuaciones")
        self.horizontalLayout_2.addWidget(self.textecuaciones)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout.addWidget(self.scrollArea_3)
        self.graficar = QtWidgets.QPushButton(self.centralwidget)
        self.graficar.setEnabled(False)
        self.graficar.setObjectName("graficar")
        self.verticalLayout.addWidget(self.graficar)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 305, 102))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textsolucion = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textsolucion.setEnabled(False)
        self.textsolucion.setStyleSheet("QTextEdit{border:2px groove #242424;}")
        self.textsolucion.setObjectName("textsolucion")
        self.horizontalLayout_3.addWidget(self.textsolucion)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 306, 403))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.textproceso = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textproceso.setEnabled(False)
        self.textproceso.setStyleSheet("QTextEdit{border:2px groove #242424;}")
        self.textproceso.setObjectName("textproceso")
        self.verticalLayout_2.addWidget(self.textproceso)
        self.guardar = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.guardar.setEnabled(False)
        self.guardar.setObjectName("guardar")
        self.verticalLayout_2.addWidget(self.guardar)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Metodos Numericos"))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p>Metodo</p></body></html>"))
        self.label.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">Metodo</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">Metodo</span></p></body></html>"))
        self.gaussjordan.setText(_translate("MainWindow", "Gauss_Jordan"))
        self.otrometodo.setText(_translate("MainWindow", "otro metoddo"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">Dimension</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "2x2"))
        self.comboBox.setItemText(1, _translate("MainWindow", "3x3"))
        self.comboBox.setItemText(2, _translate("MainWindow", "4x4"))
        self.comboBox.setItemText(3, _translate("MainWindow", "5x5"))
        self.label_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Metodo</p></body></html>"))
        self.label_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">Metodo</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">Sistema de Ecuaciones</span></p></body></html>"))
        self.graficar.setToolTip(_translate("MainWindow", "Graficar ecuaciones 2x2 o 3x3"))
        self.graficar.setText(_translate("MainWindow", "Graficar"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">Solucion</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">Procedimiento</span></p></body></html>"))
        self.guardar.setToolTip(_translate("MainWindow", "Guarde el proceso obtenido"))
        self.guardar.setText(_translate("MainWindow", "Guardar"))

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
"""
