# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(169, 150)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_Verificar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Verificar.setGeometry(QtCore.QRect(30, 30, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Verificar.setFont(font)
        self.btn_Verificar.setObjectName("btn_Verificar")
        self.btn_Gerar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Gerar.setGeometry(QtCore.QRect(30, 80, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Gerar.setFont(font)
        self.btn_Gerar.setObjectName("btn_Gerar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CPF"))
        self.btn_Verificar.setText(_translate("MainWindow", "Verificar CPF"))
        self.btn_Gerar.setText(_translate("MainWindow", "Gerar CPF"))
