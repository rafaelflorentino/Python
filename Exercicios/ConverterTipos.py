# Objetivo: Faça um Programa que converta tipos de variáveis em outros tipos.
# Entrada: Sem entrada.
# Saida: Variáveis com seus tipos trocados.
# Autor: Rafael Florentino.

# Coverter tipo float para tipo inteiro
print(int(10.999)) 

# Coverter tipo inteiro para tipo float
print(float(10))
num1 = 5
num2 = 2
num3 = 7.54
num4 = '34'
num5 = '2.98'
print(num1/num2) # No Pyton 3 resultado é: float 2.5, no Pyton 2 resultado é: inteiro 2 

# Converter inteiro em String 
print('\nConverter inteiro em String: '+ str(num1) +' para poder concatenar com outra string') 

# Converter Float em String 
print('Converter Float em String: '+ str(num3) +' para poder concatenar com outra string')

# Converter String em inteiro
print('Converter String em Inteiro:', int(num4))

# Converter String em float
print('Converter String em Float:', float(num5))

# Converter Lista em Tuplas
lista=['abacate','uva','laranja']
tupla = tuple(lista)
print('\nConverter Lista em Tupla')
print(tupla)
tupla = tuple('Ola Mundo!')
print(tupla)

# Converter Tuplas em Lista
tupla = ('azul','vermelho','amarelo')
lista= list(tupla)
print('\nConverter Tupla em Lista')
print(lista)
lista= list('Hello World.')
print(lista)
lista = list(str(5000)) # Não da para converter número pra lista e tupla sem converter em string primeiro. 
print(lista)


