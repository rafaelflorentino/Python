# Objetivo: Escreva um programa que receba um nome e verificuqe se e comum ou não.
# Entrada: Nome.
# Saida: Nome, mensagem.
# Autor: Rafael Florentino.
nome = str(input('Digite o seu nome: '))

# Estrutura Condicional Aninhada
if nome == 'rafael' :
    print('Seu nome é, muito bonito!')
elif nome == 'maria' or nome == 'pedro' or nome == 'joao' :
    print('Seu nome e bem popular no Brasil!')
elif nome in ('ana claudia jessica juliana'):
    print('Belo nome femenino.')
else:
    print('Seu nome e bem normal.')

print('Tenha um bom dia {}.'.format(nome))