# Objetivo: Faça um Programa que receba valores do teclado realize operações concatene strings, receba um valor e 
# informe o tipo da variavel e imprima os resultados na tela. 
# Entrada: Números, caracateres.
# Saida: Resultado das operações, tpo do dado, mensagem.
# Autor: Rafael Florentino.

# Em Booleano, Se não colocar valor = False, se colocar Valor = True
b= bool(input('Digite ou não algo:'))
print('Voce digitou algo:',b)

a= -19 # Operadores de atribuição =, +=, -=, **=, //=, %=, /=,  ++ e --
print('\nNúmero : {} com o sinal de + Retorna o valor indentidade : {}'.format(a,+a)) # Operador Unário +
print('Número : {} com o sinal de - Retorna o valor invertido: {}'.format(a,-a)) # Operador Unário -


# Soma entre 2 numeros inteiros, também comando .format

n1 = int(input('\nDigite um numero: '))
n2 = int(input('Digite outro numero: '))
soma = n1 + n2
divisao_inteira = n1 // n2
divisao_resto = n1 % n2
elevado = n1 ** n2

print('\nA Soma de {} + {} = {}'.format(n1,n2,soma))
print('A Divisão inteira de {} // {} = {}'.format(n1,n2,divisao_inteira ))
print('O Resto da divisão de {} % {} = {}'.format(n1,n2,divisao_resto ))
print('Elevar {} ** {} = {}'.format(n1,n2,elevado ))

# Juntar o conteudo de 2 Strings

n3 = input('\nDigite um numero: ')
n4 = input('Digite outro numero: ')
soma2 = n3 + n4

print('A Concatenação de {} + {} = {}'.format(n3,n4,soma2))

# Verificar Tipo de caracter

valor = int(input('insira algum caracter: '))

print("Valor: {} Tipo: {}".format(valor,type(valor)))

