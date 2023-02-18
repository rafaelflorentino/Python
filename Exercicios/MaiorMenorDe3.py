# Objetivo: Crie um programa que leia 3 números e diga qual é o maior e o menor.
# Entrada: Três números.
# Saida: Maior número menor número ou mensagem de todos números iguais.
# Autor: Rafael Florentino.

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

if n1 == n2 == n3:
    print('Todos os números são iguais')
else:
    if n1 > n2:
        if n1 > n3:
            maior = n1

            if n2 > n3:
                menor = n3
                print('O maior número é: {} o menor número é: {}'.format(maior, menor))
            else:
                menor = n2
                print('O maior número é: {} o menor número é: {}'.format(maior, menor))
        else:
            maior = n3

            if n1 > n2:
                menor = n2
                print('O maior número é: {} o menor número é: {}'.format(maior, menor))
            else:
                menor = n1
                print('O maior número é: {} o menor número é: {}'.format(maior, menor))
    else:
        if n2 > n3:
            maior = n2

            if n1 > n3:
                menor = n3
                print('O maior número é: {} o menor número é: {}'.format(maior, menor))
            else:
                menor = n1
                print('O maior número é: {} o menor número é: {}'.format(maior, menor))
        else:
            maior = n3
            menor = n1
            print('O maior número é: {} o menor número é: {}'.format(maior, menor))
