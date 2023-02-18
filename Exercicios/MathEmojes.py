# Objetivo: Faça um Programa que receba realize operações usando math, raiz, gerar numero aleatório, imprimir emojes.
# Entrada: Dois números.
# Saida: Mensagem contendo o resultado das operações.
# Autor: Rafael Florentino.

from math import sqrt, floor, ceil
import random
import emoji

num = int(input('informe um número: '))
raiz = sqrt(num)

print(' A raiz de {} e igual: {}'.format(num, ceil(raiz)))
print(' A raiz de {} e igual: {}'.format(num, floor(raiz)))

aleatorio = random.random()
print('\nNúmero aleatorio: {}'.format(aleatorio))
print('\nNúmero aleatorio Inteiro: {}'.format(random.randint(1, 10)))

# Emojes
print(emoji.emojize("\nPython is fun :red_heart:", variant="emoji_type"))
print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.emojize('Python is :thumbsup:', language='alias'))
print(emoji.demojize('Python is 👍'))
print(emoji.is_emoji("👍"))