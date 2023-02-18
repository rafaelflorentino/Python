# Objetivo: Crie um programa que receba a largura e a altura da parede e diga qual é a dimensão da parede, área, m2, tinta nessecária.
# Entrada: Valor em real.
# Saida: Valor convertido em dolar.
# Autor: Rafael Florentino.

largura = float(input('Digite quantos metros de largura tem a parede: '))
altura = float(input('Digite quantos metros de  altura tem a parede: '))

area = largura * altura
quantidade = area / 2

print('A dimensão da parede é: {:.1f}x{:.1f}; a área da parede é igual a: {}m2; serão necessários: {:.1f} litros de tinta para pintar a parede'.format(largura,altura,area,quantidade))