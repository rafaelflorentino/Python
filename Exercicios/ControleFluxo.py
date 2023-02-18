# Objetivo: Faça um Programa que faça operações de controle de fluxo, listas e utilize o fatiamento.
# Entrada: Senha.
# Saida:  Mensagem de aprovado ou reprovado e listas.
# Autor: Rafael Florentino.

# IF
nota = 70
if nota >= 65: # Condição
    print('Aprovado!') # 1 Blocoo de código if: True
else: 
    print('Reprovado.') # 2 Blocoo de código if: False
print('\n')


# Elif
nota = 60
if nota >= 65: # Condição
    print('Aprovado!') 
elif nota >= 60:
    print('Recuperação.') # elif = else if 
else: 
    print('Reprovado.') 
print('\n')

nota = 72
if nota >= 90:
    print('A')
elif nota >= 80:
    print('B')
elif nota >= 70:
    print('C')
elif nota >= 60:
    print('D')
else:
    print('Reprovou')
print('\n')

# IF Aninhado
nota1 = 80
nota2 = 50
if nota1 > 60:
    if nota2 > 60:
        print('Passou nas duas fases')
    else:
        print('Só passou na primeira fase')
else:
    print('Não passou na primeira fase')
print('\n')

# Combinação de Condições, Condições Compostas
nota1 = 80
nota2 = 70
if nota1 > 60 and nota2 > 60:
    print('Passou nas duas fases')
elif nota1 > 60:
    print('Só passou na primeira fase')
else:
    print('Não passou na primeira fase')
print('\n')

# Laços de Repetição

# While
senha = ''
while senha != 'admin':
    print('Digite a senha(admin):')
    senha = input()
print('Senha correta!')
print('\n')

# For
for i in range(0,5): # Range gera um intervalo entre 0 e 5 = 4
    print(i) # 0 # 1 # 2 # 3 # 4
print('\n')

# Somente com stop
for i in range(6):
    print(i)
print('\n')

# Com start e stop
for i in range(20, 25): # vai do do 20 ao 24
    print(i) # 20 # 21 # 22 # 23 # 24
print('\n')

# Com start, stop e step
for i in range(0, 15, 3):
    print(i) # 0 # 3 # 6 # 9 # 12
print('\n')

# Com start, stop e step negativo
for i in range(50, 0, -10):
    print(i) # 50 # 40 # 30 # 20 # 10
print('\n')

# Percorrendo um lista
animais = ['gato', 'cachorro', 'papagaio', 'canguru']
for animal in animais:
    print(animal) # gato # cachorro # papagaio # canguru
print('\n')

# Percorrendo um lista com range() e len()
animais = ['gato', 'cachorro', 'papagaio', 'canguru']
for item in range(len(animais)): # len passa ora range o tamnaho da lista dde animais para o intervalo de repetição.
    animais.append('animal') # Adiciona 'animal ao final da lista 4X.
print(animais) # ['gato', 'cachorro', 'papagaio', 'canguru', 'animal', 'animal','animal', 'animal']
print('\n')

# Percorrendo um lista com range() 
inteiros = []
for i in range(10): # 0 a 9
    inteiros.append(i)
print(inteiros) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('\n')

# Pecorrendo uma String(é um tipo de dado iteravel)
nome = 'animal'
for letra in nome:
    print(letra) # a # n # i # m # a # l
print('\n')

# Percorrendo um Dicionário
cliente = {'nome': 'José', 'idade': '31', 'cidade': 'Brasília', 'UF': 'DF'}
for chave in cliente:
    print (chave + ': ' + cliente[chave]) # Percorre pelas chaves
# nome: José
# idade: 31
# cidade: Brasília
# UF: DF
print('\n')

# Laço Aninhado
minha_lista = []
for x in [20, 40, 60]:
    for y in [2, 4, 6]:
        minha_lista.append(x * y)
print(minha_lista) # [40, 80, 120, 80, 160, 240, 120, 240, 360]
print('\n')

# Laço Aninhado número e string
lista_numeros = [1, 2, 3]
lista_letras = ['a', 'b', 'c']
for numero in lista_numeros:
    print(numero)
    for letra in lista_letras:
        print(letra)
print('\n')

# Lista de listas
lista_de_listas = [['cavalo', 'vaca', 'gato'],[0, 1, 2],[9.9, 8.8, 7.7]]
for lista in lista_de_listas: # se passar so 1 for imprimi cada lista inteira.
    print(lista)
# ['cavalo', 'vaca', 'gato']
# [0, 1, 2]
# [9.9, 8.8, 7.7]
print('\n')

# Percorrer todos os itens da lista em lista
lista_de_listas = [['cavalo', 'vaca', 'gato'],[0, 1, 2],[9.9, 8.8, 7.7]]
for lista in lista_de_listas:
    for item in lista: 
        print(item) # cavalo # vaca # gato # 0 # 1 # 2 # 9.9 # 8.8 # 7.7
print('\n')

# Break
numero = 0
for numero in range(10):
    numero = numero + 1
    print(numero) # 1 # 2 # 3 # 4 # 5 
    if numero == 5:
        break # encerra todas as iteraçoes do for, sai do for, quebra olaço de repetição.
print('Fora do laço') # Fora do laço
print('\n')

# Continue
numero = 0
for numero in range(10):
    numero += 1
    if numero == 5:
        continue # pula essa iteração(ignora ela) e vai ra proxima iteração.
    print(numero) # 1 # 2 # 3 # 4 # 6 # 7 # 8 # 9 # 10 
print('Fora do laço')# Fora do laço
print('\n')

# Pass
numero = 0
for numero in range(10):
    numero = numero + 1
    if numero == 5:
        pass # Serve para preencheer o espaço até vc colocar um codigo, e respeitar a identação do bloco de codigo aninhado.
    print(numero)
print('Fora do laço')
print('\n')



# 1 Crie um laço for que imprima os valores de 0 a 9
for i in range(0, 10):
    print(i)
print('\n')

# 2 Crie um laço for que imprima os valores de 9 a 0 reduzindo 2 unidades por vez
for i in range(9, -1, -2):
    print(i)
print('\n')

# 3 Crie um laço for que imprime a lista ['joao', 'maria', 'pedro', 'paulo'] em ordem inversa
nomes = ['joao', 'maria', 'pedro', 'paulo']
for i in range(len(nomes)-1, -1, -1):
    print(nomes[i])
print('\n')

# 4 Usando laços for aninhados, imprima a tabuada de 0 a 5
for i in range(11):
    for j in range(11):
        print('{}*{}={}'.format(i, j, i*j))
    print('\n')    
print('\n')

# 5 Crie um laço for que itera de 1 a 10 porém só imprime os números pares usando a instrução continue
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print('{} é par'.format(i))
print('\n')











   





