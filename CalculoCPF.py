import re
from validar import *
from CPF import *
from random import randint

C = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]


def regex_validar(cpf):
    regex = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    if re.findall(regex, cpf):
        return re.sub(r'[^\d]', '', cpf)
    else:
        return False


def calcular_digito(cpf):
    if len(cpf) == 9:
        c = C[1:]
    elif len(cpf) == 10:
        c = C

    total = 0
    for indice, i in enumerate(c):
        total += int(cpf[indice]) * i

    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0
    cpf += str(digito)

    return cpf


def validar(cpf):
    if regex_validar(cpf):
        cpf = regex_validar(cpf)
        cpf_validar = cpf[:-2]
        cpf_repeticao = cpf[0] * 11

        novo_cpf = calcular_digito(cpf_validar)
        novo_cpf = calcular_digito(novo_cpf)

        if cpf == cpf_repeticao:
            return False
        elif cpf == novo_cpf:
            return True
        else:
            return False
    else:
        return False


def gerar():
    cpf_gerar = str(randint(100000000, 999999999))
    cpf_gerado = calcular_digito(cpf_gerar)
    cpf_gerado = calcular_digito(cpf_gerado)

    return cpf_gerado
