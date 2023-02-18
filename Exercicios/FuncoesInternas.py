# Objetivo: Faça um Programa que realize algumas das funções internas do python.
# Entrada: Números, caracateres.
# Saida: Resultado das operações, tpo do dado, mensagem.
# Autor: Rafael Florentino.

# Valor absoluto abs()
# Calcular a distância percorrida
km_inicial = 125
km_final = 33
print('Diferença: ' + str(km_final - km_inicial)) # Diferença: -92

distancia_percorrida = abs(km_final - km_inicial)
print('A distância percorrida foi: ' + str(distancia_percorrida) + 'km.') # A distância percorrida foi: 92km.


# Quociente e Resto divmod()
a=10
b=3
print(divmod(a,b)) # Retornado em formato de tupla (Quociente, Resto) imutavel.
print(a // b , a % b) # Equivale a divisão inteira e ao modulo.

# Contar a quantidade de palavras dividida por paginas do livro
palavras = 80000
por_pagina_A = 300
por_pagina_B = 250
msg = '\nCom a opção {0} são necessárias {1[0]} páginas e sobram {1[1]} palavras'
# Opção A
resA = divmod(palavras,por_pagina_A) # Com a opção A são necessárias 266 páginas e sobram 200 palavras.
print(msg.format('A', resA))
# Opção B
resB = divmod(palavras,por_pagina_B)
print(msg.format('B', resB)) # Com a opção B são necessárias 320 páginas e sobram 0 palavras.


# Potenciação pow()
# Uma bacteria se reproduzindo por 24 horas, quantas baterias tera
horas = 24 
total_bacterias = pow(2,horas) # bacterias dobram a cada hora
print('\nTotal de Bacterias em {} horas e igual a: {} bacterias'.format(horas,total_bacterias)) 


# Arredondamento round()
i = 17.34989436516001
print(round(i,4))
# 17.3499

# Arredondar a conta e dividir entre 3 amigos
conta = 87.93
taxa = 0.2
nr_pessoas = 3
total_conta = conta + (conta * taxa)
valor_individual = total_conta / nr_pessoas
print('\nValor sem arredondar: ' +
str(valor_individual)) # Valor sem arredondar: 35.172000000000004
valor_individual = round(valor_individual, 2)
print('Valor arredondado: ' +
str(valor_individual))#Valorarredondado:3517

# Arredondando com 0
print('Valor: 345.98745903485 arredondado com 0 e igual: ',round(345.9874590348545304636, 0)) # 346.0


# Somatório sum()
alguns_floats = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
print('\nSomatório :',sum(alguns_floats)) # 49.5

print(sum((8,16,64,512))) # 600
print(sum({- 10: 'x', -20: 'y', -30: 'z'})) # -60 Soma so as chaves, não soma as valores
print(sum({-10: 30, -20: 'y', -30: 'z'})) # -60 Soma so as chaves, não soma as valores

alguns_floats = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
print(sum(alguns_floats, 0.5)) # 50.0



