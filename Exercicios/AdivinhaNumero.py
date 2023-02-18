# Objetivo: Faça um Programa que gere um número aleatório, o usuário tem 5 tentaivas de adivinha, a cada tentativa errada o
# programa avisa se o número zerado e maior ou menor.
# Entrada: Palpite do número.
# Saida:  Mensagem de maior ou menor, mensagem de acerto com a quantidade de tentativas ou mensagem perda.
# Autor: Rafael Florentino.

# random e break
import random
numero = random.randint(1, 25)
nr_tentativa = 0
while nr_tentativa < 5:
    print('Adivinhe um número entre 1 e 25:')
    chute = input()
    chute = int(chute)
    nr_tentativa += 1
    if chute < numero:
        print('Seu palpite é muito baixo')
    if chute > numero:
        print('Seu palpite é muito alto')
    if chute == numero:
        break
if chute == numero:
    print('Você adivinhou o número em ' + str(nr_tentativa) + ' tentativas!')
else:
    print('Você não adivinhou o número. Era ' + str(numero))
