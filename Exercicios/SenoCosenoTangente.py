# Objetivo: Faça um programa que receba um angulo, e retorne o seno, coseno e tangente.
# Entrada: Angulo.
# Saida: Seno, Coseno, Tangente.
# Autor: Rafael Florentino.

#import math
from math import radians, sin, cos, tan

angulo = float(input('Digite o valor do ângulo: '))
seno = sin(radians(angulo)) # Tem que converter o angulo para radianos primeiro

print('O valor do Seno e igual a: {:.2f}'.format(seno))
print('O valor do Coseno e igual a: {:.2f}'.format(cos(radians(angulo))))
print('O valor da Tangente e igual a: {:.2f}'.format(tan(radians(angulo))))