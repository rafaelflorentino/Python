# Objetivo: Escreva um programa que Receba o valor de três retas, e informe se é possível formar um triângulo.
# Entrada: Três retas.
# Saida: Mensagem se é possível ou não formar um triangulo.
# Autor: Rafael Florentino.

"""" Início do Programa """

a = int(input('Digite o Valor da reta A: '))
b = int(input('Digite o Valor reta B: '))
c = int(input('Digite o Valor da reta C: '))

if (a + b) > c and (b + c) > a and (a + c) > b :
    print('Valores das retas A: {}, B: {}, C: {}, É POSSIVEL FORMAR UMA TRIÂNGULO!!!'.format(a,b,c))
else:
    print('Valores das retas A: {}, B: {}, C: {}, NÃO É POSSIVEL FORMAR UMA TRIÂNGULO!!!'.format(a,b,c))

"""" Fim do Programa """