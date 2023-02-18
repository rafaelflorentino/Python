# Objetivo: Receba as três bases/lados de um triangulo e diga se e possivel formar um triangulo, caso sim diga se ele e: equilátero, 
# isóceles ou escaleno.
# Entrada: Três lados do triângulo.
# Saida: Tipo de triângulo ou se não e é possível formar um triângulo.
# Autor: Rafael Florentino.

a = int(input('Digite o valor do lado A (Primeiro lado):  '))
b = int(input('Digite o valor do lado B (Segundo lado):  '))
c = int(input('Digite o valor do lado C (Terceiro lado):  '))

if (a + b) > c and (b + c) > a and (c + a) >b:
    if a == b == c: #a == b and a == c and c == b
        print('\nTRIANGULO EQUILÁTERO (Tem os 3 lados iguais)')
        print('Valores das retas A: {}, B: {}, C: {} '.format(a,b,c))
    elif a != b != c !=a :
        print('\nTRIANGULO ESCALENO (Tem todos os lados diferentes)')# a != b and b != c and a != c
        print('Valores das retas A: {}, B: {}, C: {} '.format(a,b,c))
    else: # (a == b and a != c and c != b) or (b == c and b != a and a != c) or (c == a and c != b and a != b):
        print('\nTRIANGULO ISÓCELES (Tem só 2 lados iguais)')
        print('Valores das retas A: {}, B: {}, C: {} '.format(a, b, c))
else:
    print('\nNÃO É POSSIVEL FORMAR UMA TRIÂNGULO!!!')
    print('Valores das retas A: {}, B: {}, C: {} '.format(a, b, c))
