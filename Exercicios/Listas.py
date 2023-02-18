# Objetivo: Faça um Programa que crie listas e imprima seu conteúdo na tela, use várias funções de lista.
# Entrada: Sem entrada.
# Saida: Elementos da lista.
# Autor: Rafael Florentino.

# Lista
criaturas_maritimas = ['tubarão', 'peixe', 'lula', 'camarão', 'anêmona']
print(criaturas_maritimas)
print(criaturas_maritimas[3]) # indice [3] camarão.
print(criaturas_maritimas[-5]) # indice [-5] Tubarão; Python aceita indices negativos, ordem fica de tras pra frente.
print('\n') 

print (criaturas_maritimas + ['polvo']) # Permite somar/juntar listas.

# Fatiamento de Lista
print(criaturas_maritimas[1:3]) # Exclusivo nap inclui o 3, pega [1] e [2] não pega [3]
print(criaturas_maritimas[:5]) # Pega do [0] ao [4] pega todo o início .
print(criaturas_maritimas[2:]) # Pega do [2] ao [4] pega todo o final
print('\n') 

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(numeros[1:11:2]) # PASSO 2 percorrer de 1 a 11 de dois em dois # [1, 3, 5, 7, 9]
print(numeros[::3]) # PASSO 3 percorrer toda lista de três em três.
print('\n') 

criaturas_maritimas = ['tubarão', 'peixe', 'lula', 'camarão', 'anêmona']
oceanos = ['Pacífico', 'Atlântico', 'Ártico', 'Índico','Antártico']
print(criaturas_maritimas + oceanos + ['hermitão'] ) # + Concatena listas em uma nova, e um iten só tem que por entre colchetes.

print(criaturas_maritimas * 2); # produto * escalar, gera uma nova lista contendo ela 2 vezes. 
print(oceanos * 3); 

criaturas_maritimas += ['Polvo'] # += Gera uma nova lista e adiciona polvo a lista.
print(criaturas_maritimas)
criaturas_maritimas *= 2 # *= Gera uma nova lista e Duplica os elementos da lista, repete ao final.
print(criaturas_maritimas)

del criaturas_maritimas[1] # Exclui o peixe.
print(criaturas_maritimas)

del criaturas_maritimas[2:4] # Exclui os elementos da posição 2 até a 4.
print(criaturas_maritimas)

# Lista de listas
nomes_marinhos = [['tubarão', 'peixe', 'camarão'], ['barbatana', 'nemo', 'cascudo']]# listas aninhadas
print(nomes_marinhos[0][1]) # Peixe
print(nomes_marinhos[1][2]) # cascudo
print('\n') 

linguagens = ['Python', 'Cobol', 'Lisp', 'C', 'C++']
print(linguagens[2])  # Lisp
print(linguagens[-1]) # C++
linguagens[0] = 'Java'
linguagens += ['Prolog']
print(linguagens) # ['Java', 'Cobol', 'Lisp', 'C', 'C++', 'Prolog']
print('\n') 

# list.append 
peixes = ['tilápia', 'bacalhau', 'sardinha', 'enguia']
peixes.append('salmao') # Adiciona elemento ao final da lista. Altera a propia lista, não cria nova lista.
print(peixes) # ['tilápia', 'bacalhau', 'sardinha', 'enguia', 'salmao']
print('\n') 

# list.insert(i, x)
peixes.insert(0, 'anchova') # Insere anchova na posição 0 da lista, e empurra os outros pra frente.
print(peixes) 
print('\n') 

# list.extend()
outros_peixes = ['lambari', 'traíra']
peixes.extend(outros_peixes) # Estende a lista de peixe adicionando no final os itens da lista outros_peixes.
print(peixes) 
print('\n') 

# list.remove()
peixes = ['tilápia', 'bacalhau', 'sardinha', 'enguia']
peixes.remove('tilápia') # Remove o elemento com valor tilápia, só remove o primeiro iten encontrado.
print(peixes)
print('\n') 

# list.pop()
print(peixes.pop(1)) # sardinha, Retorna o velor do elemento da posição e o remove da lista, ou remove ultimo valor.
print(peixes) # ['tilápia', 'enguia']
print('\n') 

# list.index()
peixes = ['tilápia', 'bacalhau', 'sardinha', 'enguia']
print(peixes.index('sardinha')) # 2 Retorna a posição do indice pelo valor.
print('\n') 

# list.copy()
peixes2 = peixes.copy() # Copia os elementos da outra lista dentro dela.
peixes.append('lambari')
print(peixes)  # ['tilápia', 'bacalhau', 'sardinha', 'enguia', 'lambari']
print(peixes2) # ['tilápia', 'bacalhau', 'sardinha', 'enguia']
print('\n') 


# list.reverse()
peixes.reverse() # inverte a ordem da lista.
print(peixes) # ['enguia', 'sardinha', 'bacalhau', 'tilápia']
print('\n') 

# list.count()
print(peixes.count('tilápia')) # 1 Conta a quantidades daquele elemento dentro da lista.
peixes.append('tilápia')
print(peixes) # ['tilápia', 'bacalhau', 'sardinha', 'enguia', 'tilápia']
print(peixes.count('tilápia')) # 2
print('\n') 

# list.sort()
peixes = ['tilápia', 'bacalhau', 'sardinha', 'enguia']
peixes.sort() # coloca em ordem alfabética.
print(peixes) # ['bacalhau', 'enguia', 'sardinha', 'tilápia']
print('\n') 

# list.clear()
peixes.clear() # Limpa todos os elementos da lista.
print(peixes) # []
print('\n') 

paises = ['Brasil', 'Nova Zelândia', 'Austrália', 'França']
paises.insert(0, 'Suécia')
print(paises.pop()) # França
paises2 = paises.copy()
paises.sort()
paises.reverse()
print(paises) # ['Suécia', 'Nova Zelândia', 'Brasil', 'Austrália']
print('\n') 














