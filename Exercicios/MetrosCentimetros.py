# Objetivo: Escreva um programa que receba a quanidade em metros e converta em centimetros, 
# milimetros, decimetro, decametro, hectometro, kilometro.
# Entrada: Quantidade de metros.
# Saida: metros, centimetros, milimetros, decimetros, decametros, hectometros, kilometro.
# Autor: Rafael Florentino.

metros = float(input('Digite a quatidade de metros: '))
centimetros = metros * 100
milimetros = metros * 1000
decimetro = metros * 10
decametro = metros / 10
hectometro = metros / 100
kilometro = metros / 1000

print('Metros: {}; Centimetros: {:.0f}; Milimetros: {:.0f}'.format(metros, centimetros, milimetros))
print('Decimetros: {}; decâmetros: {}; hectômetros: {}; Kilometros: {}'.format(decimetro, decametro, hectometro,kilometro))