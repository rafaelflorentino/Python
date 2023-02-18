# Objetivo: Crie um programa que receba um float e retorne apenas a parte inteira do número.
# Entrada: Número float.
# Saida: Número inteiro.
# Autor: Rafael Florentino.

import math

numero = float(input("Digite um número: "))
print('A porção inteira do numero {} é : {}'.format(numero, int(numero)))
print(math.trunc(numero))