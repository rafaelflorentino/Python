# Objetivo: Faça um Programa que receba nomes e números e imprima mensagem na tela.
# Entrada: Numero, nome, idade, peso, dia, mês, ano.
# Saida: Mensagem com os dados.
# Autor: Rafael Florentino.

'''
Testes e pytom

'''

# Teste 2
numero1 = input('Digite o primeiro número: ')
numero2 = input('Digite o segundo número: ')
soma = int(numero1) + int(numero2)
print('A soma dos numeros e igual a: ',str(soma))


# Teste 3
dia = input('Qual o dia voce nasceu? ')
mes = input('Em qual mês voce nasceu(número)?  ')
ano = input('Em qual ano voce nasceu?  ')
print('Você nasceu em:',dia+'/'+mes+'/'+ano,' Correto?')

# Teste 2
nome2 = input('Qual e o seu nome? ')
print('Olá ',nome2+' ! Prazer em te conhecer!')

# Teste 1
nome = input('Qual é o seu nome?')
idade = input('Qual é a sua idade?')
peso = input('Qual é o seu peso?')
print(nome, idade, peso)
