# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gerador.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Gerador(object):
    def setupUi(self, Gerador):
        Gerador.setObjectName("Gerador")
        Gerador.resize(212, 112)
        self.cpf_gerado = QtWidgets.QLineEdit(Gerador)
        self.cpf_gerado.setGeometry(QtCore.QRect(10, 30, 181, 20))
        self.cpf_gerado.setReadOnly(True)
        self.cpf_gerado.setObjectName("cpf_gerado")
        self.btn_Gerar = QtWidgets.QPushButton(Gerador)
        self.btn_Gerar.setGeometry(QtCore.QRect(10, 60, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_Gerar.setFont(font)
        self.btn_Gerar.setObjectName("btn_Gerar")
        self.btn_Voltar = QtWidgets.QPushButton(Gerador)
        self.btn_Voltar.setGeometry(QtCore.QRect(120, 60, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_Voltar.setFont(font)
        self.btn_Voltar.setObjectName("btn_Voltar")

        self.retranslateUi(Gerador)
        QtCore.QMetaObject.connectSlotsByName(Gerador)

    def retranslateUi(self, Gerador):
        _translate = QtCore.QCoreApplication.translate
        Gerador.setWindowTitle(_translate("Gerador", "CPF"))
        self.btn_Gerar.setText(_translate("Gerador", "Gerar"))
        self.btn_Voltar.setText(_translate("Gerador", "Voltar"))
