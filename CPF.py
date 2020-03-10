import sys
from principal import *
from validar import *
from gerador import *
from CalculoCPF import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox


class Principal(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=None)
        super().setupUi(self)
        self.btn_Verificar.clicked.connect(self.janela_validar)
        self.btn_Gerar.clicked.connect(self.janela_gerar)

    def janela_validar(self):
        self.validar = Validar()
        self.validar.show()
        self.close()

    def janela_gerar(self):
        self.gerar = Gerador()
        self.gerar.show()
        self.close()

class Validar(QMainWindow, Ui_Validar):
    def __init__(self, parent=None):
        super().__init__(parent=None)
        super().setupUi(self)
        self.btn_Voltar.clicked.connect(self.janela_principal)
        self.btn_Validar.clicked.connect(self.validar)

    def validar(self):
        cpf_validar = self.cpf_input.text()
        if validar(cpf_validar):
            self.cpf_output.setText(f'CPF VÁLIDO!!!')
        else:
            self.cpf_output.setText(f'CPF INVÁLIDO')

    def janela_principal(self):
        self.principal = Principal()
        self.principal.show()
        self.close()

class Gerador(QMainWindow, Ui_Gerador):
    def __init__(self, parent=None):
        super().__init__(parent=None)
        super().setupUi(self)
        self.btn_Voltar.clicked.connect(self.janela_principal)
        self.btn_Gerar.clicked.connect(self.gerar)

    def janela_principal(self):
        self.principal = Principal()
        self.principal.show()
        self.close()

    def gerar(self):
        cpf_gerado = gerar()
        self.cpf_gerado.setText(f'{cpf_gerado[0:3]}.{cpf_gerado[3:6]}.{cpf_gerado[6:9]}-{cpf_gerado[9:]}')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    principal = Principal()
    principal.show()
    qt.exec()
