# Objetivo: Faça um Programa que o usuário tenha que adivinhar qual número o programa gerou aleatoriamente entre 0 e 5.
# Entrada: Um número.
# Saida: Mensagem de Acerto ou erro.
# Autor: Rafael Florentino.

import random
from time import sleep

computador = random.randint(0,5)  # Gera números aleatórios entre 0 e 5.
jogador = int((input('Vou pensar em um número entre 0 e 5 Tente adivinhar: ')))
print('PROCESSANDO...')
sleep(3) # Pausa o programa por 3 segundos.

print('-=-' * 20) # multiplica os caracteres -=- 20 vezes.

if jogador == computador:
    print('PARABÉNS VOCÊ VENCEU!!! O número que eu pensei foi {}, é você escolheu: {}'.format(computador,jogador))
else:
    print('QUE PENA VOCÊ PERDEU!!! O número que eu pensei foi {}, é você escolheu: {}'.format(computador, jogador))