# Objetivo: Crie um programa que leia um ano e diga se esse ano e bissexto.
# Entrada: Ano.
# Saida: Mensagem dizendo se o ano e bissexto ou não.
# Autor: Rafael Florentino.

ano = int(input('Digite um ano: ').strip())

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('O ano: {} é bissexto'.format(ano))
else:
    print('O ano: {} não é bissexto'.format(ano))