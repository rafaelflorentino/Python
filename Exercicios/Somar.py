# Objetivo: Faça um Programa que receba do teclado dois números e some, divida, faça divisão inteira, eleve a potência.
# Entrada: Dois números.
# Saida: Mensagem contendo o resultado das operações.
# Autor: Rafael Florentino.

n1 = int(input('Digite um Número: '))
n2 = int(input('Digite Outro Número: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é: {} \nO produto é: {}\nA divisão é: {:.3f} '.format(s, m, d), end='')
print('Divisão inteira é: {} a potencia é:{}'.format(di, e))

print('\nO valor de digitado 20 com espaços {:=^20}!'.format(n1))# {:<20}! ; {:^20}! ; {:=^20}!