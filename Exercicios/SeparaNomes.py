# Objetivo: Faça um programa que lleia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
# Entrada: Nome Completo.
# Saida: Primeiro e segundo nome separados.
# Autor: Rafael Florentino.

"""" Início do Programa """

nome = input('Digite o nomem completo: ').strip()
separado = nome.split()

print('Nome completo: {}'.format(nome))
print('Nome separado: {}'.format(separado))
print('Primeiro Nome: {}'.format(separado[0]))
ultima = int(len(separado))
print('Último Nome: {}'.format(separado[ultima - 1]))

"""" Início do Programa """