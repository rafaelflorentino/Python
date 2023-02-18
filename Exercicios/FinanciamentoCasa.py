# Objetivo: Crie um programa que aprove ou não um emprestimo para compra de uma casa, 
# recebe o valor da casa, valor do salário, em quantos anos vai pagar,prestação mensal
# não pode exceder 30% do salário, senão e negado o emprestimo.
# Entrada: salario, valor da casa, anos de financiamento.
# Saida: Emprestimo aprovado ou não.
# Autor: Rafael Florentino.

salario = float(input('Digite o salário do comprador: '))
casa = float(input('Digite o valor da casa: '))
anos = int(input('Digite quantos anos de financiamento: '))
prestacao = casa / (anos * 12)

if prestacao > ((salario / 100) * 30) :
    print('Emprestimo não aprovado prestação de {:.2f} ultrapasou 30% do seu salário'.format(prestacao), end='')
    print('. ')
else:
    print('Emprestimo aprovado !!! valor da casa: {}, Valor das prestaçôes: {:.2f}, tempo: {} anos'.format(casa, prestacao, anos), end='')
    print('. ')