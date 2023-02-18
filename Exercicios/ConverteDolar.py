# Objetivo: Crie um programa converta real em dolar.
# Entrada: Valor em real.
# Saida: Valor convertido em dolar.
# Autor: Rafael Florentino.

reais = float(input('Digite quantos reais voce tem na carteira: R$'))
dolar = float(reais / 3.27)

print('R${} reais = U${:.2f} dolares'.format(reais, dolar))