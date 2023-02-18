# Objetivo: Escreva um programa que imprima uma mensagem com nome colorido, e fundo colorido.
# Entrada: Sem entrada.
# Saida: Mensagem com nome colorido.
# Autor: Rafael Florentino.

print('\033[0;33;44m teste Azul')
print('\033[0;30;41m teste Vermelho')
print('\033[4;33;44m teste Azul')
print('\033[1;35;43m teste Amarelo')
print('\033[30;42m teste Verde')
print('\033[m teste Preto')
print('\033[4;31;43m Hello World!\033[m')
a = 5
b = 3
nome = 'Rafael'

print('O valor de A é:\033[32m{}\033[m o valor de B é: \033[31m{}\033[m !!!'.format(a,b))
print('Olá ! Muito prazer em te conhecer {} {} {}'.format('\033[4;35m',nome,'\033[m'))

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print('\nOlá ! Muito prazer em te conhecer {} {} {}'.format(cores['amarelo'],nome,cores['limpa']))
print('Olá ! Muito prazer em te conhecer {} {} {}'.format(cores['azul'],nome,cores['limpa']))
print('Olá ! Muito prazer em te conhecer {} {} {}'.format(cores['pretoebranco'],nome,cores['limpa']))