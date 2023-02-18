# Objetivo: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento: salários que são 
# superiores a 1250,00 tem aumento 10%; para salários igual ou menor a 1250,00 tem aumento de 15%.
# Entrada: Valor Salário.
# Saida: Salário reajustado.
# Autor: Rafael Florentino.

"""" Início  do Programa """

salario = float(input('Digite o valor do salário para receber o aumento: '))

if salario <= 1250 :
    aumento = salario + (salario / 100 * 15)
    print('Antigo Salário: {} novo Salário: {}'.format(salario,aumento))
else:
    aumento = salario + (salario / 100 * 10)
    print('Antigo Salário: {} novo Salário: {}'.format(salario, aumento))

"""" Fim  do Programa """