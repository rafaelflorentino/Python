# Objetivo: fala um programa que receba o cateto oposto de um triangulo e o cateto adjacente e calcule a hipotenusa.
# Entrada: Cateto oposto, cateto adjacente.
# Saida: Hipotenusa.
# Autor: Rafael Florentino.

from math import hypot

oposto = float(input('Digite o valor do cateto oposto de um triângulo retângulo: '))
adjascente = float(input('Digite o valor do cateto adjascente de um triângulo retângulo: '))

hipoteusa = ( oposto ** 2 + adjascente ** 2 ) ** (1/2)

print('O valor da hipotenusa e igual a: {}'.format(hipoteusa))
print('O valor da hipotenusa e igual a: {}'.format(hypot(oposto,adjascente)))