# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'validar.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Validar(object):
    def setupUi(self, Validar):
        Validar.setObjectName("Validar")
        Validar.resize(209, 114)
        self.btn_Validar = QtWidgets.QPushButton(Validar)
        self.btn_Validar.setGeometry(QtCore.QRect(10, 80, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_Validar.setFont(font)
        self.btn_Validar.setObjectName("btn_Validar")
        self.btn_Voltar = QtWidgets.QPushButton(Validar)
        self.btn_Voltar.setGeometry(QtCore.QRect(110, 80, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_Voltar.setFont(font)
        self.btn_Voltar.setObjectName("btn_Voltar")
        self.cpf_input = QtWidgets.QLineEdit(Validar)
        self.cpf_input.setGeometry(QtCore.QRect(10, 20, 181, 20))
        self.cpf_input.setObjectName("cpf_input")
        self.cpf_output = QtWidgets.QLineEdit(Validar)
        self.cpf_output.setGeometry(QtCore.QRect(10, 50, 181, 20))
        self.cpf_output.setReadOnly(True)
        self.cpf_output.setObjectName("cpf_output")

        self.retranslateUi(Validar)
        QtCore.QMetaObject.connectSlotsByName(Validar)

    def retranslateUi(self, Validar):
        _translate = QtCore.QCoreApplication.translate
        Validar.setWindowTitle(_translate("Validar", "CPF"))
        self.btn_Validar.setText(_translate("Validar", "Validar"))
        self.btn_Voltar.setText(_translate("Validar", "Voltar"))
