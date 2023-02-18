# Objetivo: Digite um programa que leia um número e diga se ele e ímpar ou par.
# Entrada: Um número.
# Saida: Mensagem de Impar ou Par.
# Autor: Rafael Florentino.

"""" Início do Programa """

numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print('O número: {} é PAR '.format(numero))
else:
    print('O número: {} é ÍMPAR '.format(numero))


"""" Fim do Programa """
