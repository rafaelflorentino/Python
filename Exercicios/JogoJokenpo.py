# Objetivo: Crie um programa que jogue jokenpô(Pedra, Papel, Tesoura)com você.
# Entrada: Opção do jogador.
# Saida: Vitória, derrota ou empate.
# Autor: Rafael Florentino.

import random
from time import sleep

itens = ('Pedra','Papel','Tesoura')
computador = random.randint(0,2)

print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
''')
jogador = int(input('qual é a sua jogada? '))
print('-='*11)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-='*11)

print('Computador jogou: {}'.format(itens[computador]))
print('Voce jogou: {}'.format(itens[jogador]))
print('-='*11)

if computador == 0: # Pedra
    if jogador == 0:
        print('EMPATE.')
    elif jogador == 1:
        print('JOGADOR VOCÊ GANHOU!!!')
    elif jogador == 2:
        print('JOGADOR VOCÊ PERDEU.')
    else:
        print('Valor inválido, tente novamente.')

if computador == 1: # Papel
    if jogador == 1:
        print('EMPATE.')
    elif jogador == 2:
        print('JOGADOR VOCÊ GANHOU!!!')
    elif jogador == 0:
        print('JOGADOR VOCEÊ PERDEU.')
    else:
        print('Valor inválido, tente novamente.')

if computador == 2: # Tesoura
    if jogador == 2:
        print('EMPATE.')
    elif jogador == 0:
        print('JOGADOR VOCÊ GANHOU!!!')
    elif jogador == 1:
        print('JOGADOR VOCEÊ PERDEU.')
    else:
        print('Valor inválido, tente novamente.')
