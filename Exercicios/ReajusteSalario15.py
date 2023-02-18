# Objetivo: Crie um programa que receba o valor do salário e faça um reajuste de 15%.
# Entrada: Valor salário.
# Saida: Salário reajustado.
# Autor: Rafael Florentino.

salario = float(input('Digite o seu salário: '))
aumento = salario + (salario * 15 / 100)

print('O seu salario é: {:.2f} com aumento de 15% fica: {}'.format(salario, aumento))