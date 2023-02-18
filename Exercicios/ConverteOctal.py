# Objetivo: Recebe um numero inetiro, e depois passe em qual base o número deve converteido(binário, octal, hexadecimal).
# Entrada: Número, e a base.
# Saida: Número convertido na base passada.
# Autor: Rafael Florentino.

numero = int(input('Digite um numero inteiro: ').strip())
print('''Escolha uma das base para conversão:
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL ''')
base = int(input('Sua opção: '))

if base == 1 :
    print('{} Convertido para Binário e igual: {}'.format(numero, bin(numero)[2:]))
elif base == 2 :
    print('{} Convertido para Octal e igual: {}'.format(numero, oct(numero)[2:]))
elif base==3 :
    print('{} Convertido para Hexadecimal e igual: {}'.format(numero,hex(numero)[2:]))
else:
    print('\nOpção invalida, Digite um valor valido 1 (para Binário), 2 (octal) ou 3 (hexadecimal).'.format(numero))