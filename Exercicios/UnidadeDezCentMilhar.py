# Objetivo: Faça um programa que lei um número de 0 ate 9999 e mostre na tela os números separados.
# Entrada: Número.
# Saida: Número dividido, em unidade, dezena , centena, milhar.
# Autor: Rafael Florentino.

numero = int(input('Digíte um número de 0 até 9999: '))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print("Unidade: {} \nDezana: {} \nCentena: {}\nMilhar: {}".format(unidade,dezena,centena,milhar))
