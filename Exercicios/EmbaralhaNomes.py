# Objetivo: Faça um programa que receba o nome de 4 alunos embaralhe a ordem e imprima na tela a array.
# Entrada: Nomes dos alunos.
# Saida: Aluno sorteado.
# Autor: Rafael Florentino.

import random

nomes = [str(input('Digite o nome do 1° Aluno: ')), str(input('Digite o nome do 2° Aluno: ')),str(input('Digite o nome do 3° Aluno: ')),str(input('Digite o nome do 4° Aluno: '))]
random.shuffle(nomes)

print('A ordem de apresentação sera: ')
print(nomes)