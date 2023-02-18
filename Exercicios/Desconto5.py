# Objetivo: Crie um programa que receba o valor do produto e calcule quanto fica com 5% de desconto.
# Entrada: Valor do produto.
# Saida: Valor com desconto de 5%.
# Autor: Rafael Florentino.

valor = float(input('Digite o preço do produto: '))
desconto = valor - (valor * 5 / 100)

print('O valor do produto é: {} com 5% de desconto fica {} '.format(valor,desconto))