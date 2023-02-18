# Objetivo: Faça um programa que receba o nome de 4 alunos e sorteie o aluno para apagar o quadro.
# Entrada: Nomes dos alunos.
# Saida: Aluno sorteado.
# Autor: Rafael Florentino.

from random import choice

nome = [input('Digite o nome do 1° Aluno: '),input('Digite o nome do 2° Aluno: '),input('Digite o nome do 3° Aluno: '),
input('Digite o nome do 4° Aluno: ')]

print('O Aluno sorteado para apagar o quadro foi: {}'.format(choice(nome)))
