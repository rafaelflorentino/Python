# Objetivo: Faça um Programa que faça algumas funções, calule o imc, verifique se o nome tem vogais, receba e retorne dados.
# Entrada: Nome, peso, altura.
# Saida: Mensagens e o imc. 
# Autor: Rafael Florentino.

# Função Hello
def hello():
    print('Ola, Mundo!')
hello()
print('\n')

# Função Contem Vogais
def nomes():
    nome = str(input('Digite seu nome: '))
    if set('aeiou').intersection(nome.lower()): # intersection caso exista intercessão entre os dois conjuntos volta true
        print('Seu nome contém uma vogal.') #  set('aeiou') tranforma num conjunto para poder comparar com a outra astring
    else:
        print('Seu nome não contém uma vogal.')
    for letra in nome:
        print(letra)
#nomes()
print('\n')

# Função, Argumentos
def adiciona_numeros(x, y, z):
    a = x + y
    b = x + z
    c = y + z
    print(a, b, c)
adiciona_numeros(1, 2, 3)
print('\n')

# Função, Com Argumentos Nomeados
def profile_info(usuario, seguidores):
    print('Usuário: ' + usuario)
    print('Seguidores: ' + str(seguidores))
profile_info('José', 100)
profile_info(seguidores=200, usuario='Paulo')
print('\n')

# Função, Com Retorno
def quadrado(x):
    y = x ** 2
    return y
resultado = quadrado(3)
print(resultado)

# Função, Com Retorno multiplo, retorna um tupla
def retorna_numeros(x, y, z):
    a = x + y
    b = x + z
    c = y + z
    return a,b,c # retorna um tupla
num = retorna_numeros(1, 2, 3)
print(num)
print('\n')

# Função, return quebra o laço.
def meu_laco():
    for x in range(0, 25):
        print(x)
        if x == 5:
            return # Encerra a iteração antecipadamente.
    print('Esta linha não será executada.') # Codigo não vai chegar aqui por causa do return.
meu_laco()
print('\n')

# Função, breack não quebra o laço.
def meu_laco():
    for x in range(0, 25):
        print(x)
        if x == 5:
            break; # Encerra apenas o laço for.
    print('Esta linha não será executada.') # Codigo é executado.
meu_laco()
print('\n')

# Funcção Main()
def main1():
    print('Função Principal')
    hello()
main1()

# Fucao Main
nome = str(input('Digite seu nome: '))
def tem_vogal():
    if set('aeiou').intersection(nome.lower()):
        print('Seu nome contém vogais.')
    else:
        print('Seu nome não contém vogais.')

def imprime_letras():
    for letra in nome:
        print(letra)

def main2():
    tem_vogal() # Chama função 
    imprime_letras() # Chama função 

if __name__ == '__main__':
    main2() # Chama função mai2

# 1 Crie uma função que imprime 'Olá <nome>' onde <nome> é um parâmetro da função

def saudar(nome):
    print('Olá ' + nome)
saudar('Tiago')

# 2 Crie uma função chamada ehPar que devolve True se um número passado como argumento for par ou False se for ímpar
def ehPar(numero):
    return numero % 2 == 0
    print(ehPar(136))

# 3 Usando a instrução if __name__ == '__main__' crie um programa que contém uma função chamada IMC, que recebe os dados de
# altura e peso do usuário e retorna seu IMC, a função main() deverá receber os dados como entrada do usuário, acionar a 
# função IMC e imprimir a respost
def imc(altura, peso):
    return peso / (altura**2)
def main():
    altura = float(input('Digite sua altura: '))
    peso = float(input('Digite seu peso: '))
    imc_usuario = imc(altura, peso)
    print('Seu imc é {}'.format(imc_usuario))
if __name__ == '__main__':
    main()