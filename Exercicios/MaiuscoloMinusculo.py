# Objetivo: Crie um programa que leia o nome completo de uma pessoa e mostre: nome com todas letras maiusculas, nome com todas as 
# letras minusculas, quantas letras tem no total(sem espaço), quantas letras tem no primeiro nome.
# Entrada: Sem entrada.
# Saida: String frase.
# Autor: Rafael Florentino.

""" Início do Programa """

nome = input('Digite o nome completo: ').strip()

print('Nome Maiúsculo: ',nome.upper())# 1

print('Nome Minúsculo: ',nome.lower())# 2

print('Quantidade de Letras sem espaços: {}'.format(len(nome) - nome.count(' ')))
print('Quantidade de Letras sem espaços: ',len(nome.replace(' ',''))) # 3 ou


nome2 = nome.split()
print('Quantidade de letras do primeiro nome: ',len(nome2[0]))# 4)
print('primeiro nome: {} Quantidade de letras do primeiro nome: {}'.format(nome2[0], nome.find(' '))) # retorna a posição do 1 espaço, 1 nome ven antes

""" Fim do Programa """