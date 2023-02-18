# Objetivo: Crie um programa que receba os dias e os kilometros do carro alugado e retorne o valor da conta.
# Entrada: Dias alugados, kilometros rodados.
# Saida: Total a pagar.
# Autor: Rafael Florentino.

dias = int(input('Quantos dias alugados? '))
kilometros = float(input('Quantos Kilometros rodados? '))
total = (dias * 60) + (kilometros * 0.15 )


print('o total a pagar é: R$ {:.2f}'.format(total))