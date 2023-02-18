
# Objetivo: Faça um programa que receba uma string, e imprima ta tela partes da string, e os principais métodos. 
# Entrada: Sem entrada.
# Saida: String frase.
# Autor: Rafael Florentino.

frase = 'curso em video python'

print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print(len(frase)) # Quantidade de caracteres na string
print(frase.count('o'))
print(frase.count('o',0,13)) # Ache o entre o 0 e 12
print(frase.find('deo')) # Se tem mostra a posição 15
print(frase.find('Android')) # Não tem retorna -1
print('curso' in frase)  # True ou false
print(frase.replace('python','android'))# Modifica so na impreção, nao altera a variavel
print(frase.upper())
print(frase.lower())
print(frase.capitalize())# Transforma tudo em minuscolo e so a primeira em maiusculo
print(frase.title())  # Tranforma todas 1 letras das palavras em maiusculo
print(frase.strip())  # Remove os 1°s espaços em branco e os ultimos
print(frase.rstrip()) # Remove so so espaços em branco da direita
print(frase.lstrip()) # Remove so so espaços em branco da esquerda
print(frase.split())
print(frase)
frase2 = frase.split()
print(frase2[2])# Mostra segunda palavara do vetor
print(frase2[2][3])# Mostra 4 letra do vetor
print('-'.join(frase2))

print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""")

print(frase.lower().count('o')) # Transformar tudo em minúsculo para procurar letra o