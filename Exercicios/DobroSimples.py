# Objetivo: Faça um Programa que receba um número, duplique triplique e tire a raiz do valor.
# Entrada: Um números.
# Saida: Dobro, triplo e raiz do valor.
# Autor: Rafael Florentino.

numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)
raiz2 =  pow(numero, 1/2)

print('O numero: {}, O dobro: {}, O triplo: {}, A raiz quadrada: {:.2f}'.format(numero, dobro, triplo, raiz2))
