# Objetivo: Faça um programa que leia a distância de uma viajem em quilometros e diga o valor da passagem: até 200km a R$ 0,50 por km
# viajens com mais de 200km  R$ 0,45 por km.
# Entrada: Distância em quilômetros.
# Saida: Preço da passagem.
# Autor: Rafael Florentino.

distancia = int(input('Qual a distância da sua viajem em quilômetros? '))

print('Você esta prestes a começar uma viajem de {}km.'.format(distancia))

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45

"""if distancia <= 200:
    preço = distancia * 0.5
else:
    preço = distancia * 0.45"""
    
print('O preço da sua passagem é: {}'.format(preco))