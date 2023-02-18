# Objetivo: Faça um Programa que imprima na tela tipos de elementos e Funções de String.
# Entrada: Sem entrada.
# Saida: Tipos de elemetos, funçoes de string.
# Autor: Rafael Florentino.

a=b=c=0; # inicializa as 3 variaveis com 0
print('Variaveis inicializadas juntas A, B e C: ',a,b,c)
j,k,l ='tubarao',2.05,15 # Pode inicializar variáveis, na mesma linha mesmo com tipos diferentes
print('Variaveis Diferentes inicializadas juntas J, K e L: ',j,k,l)

num1 =5 # Variavel global
print('Váriavel Global num1: ',num1)
def minha_funtion():
    num1 = 10 # Variável local com memso nome da global, Sombreia a variável global
    num2 = 3 # Variáravel local
    global num3 # Tranforma em tipo global, não será apenas local
    num3 = 100
    print('Váriavel Global num1 Dentro da função é Sombreada pela local num1:',num1)
    print('Váriavel local num2: ',num2)

minha_funtion()
print('Váriavel Global num1 depois da função: ',num1)
print('Váriavel Global num3 Definida dentro da função: ',num3) 

meu_ponto_flutuante = 1.54
meu_inteiro= -25
meu_texto = 'Agua 7'
meu_boolean_falso = False
meu_boolean_verdadeiro = 2 > 1
minha_lista = [0,1,2,3,4,5,6]
minha_tupla = ('coral azul', 'coral rosa', 'coral vermelho') # Valores imutáveis
meu_dicionario = {'nome': 'Tutu', 'animal': 'tubarão', 'cor': 'azul', 'local': 'oceano'} # Chave : Valor

print('\nMeu Inteiro: ',meu_inteiro+ 3)
print('Meu Ponto Flutuante: ',meu_ponto_flutuante)
print("Meu 'Texto': ",meu_texto," Mais texto")
print('Meu "Texto": 4X '*4)
print('Meu Booleano Falso: ',meu_boolean_falso)
print('Meu Booleano Verdadeiro: ',meu_boolean_verdadeiro)
print('Minha Lista: ',minha_lista)
print('Minha Lista: ',minha_tupla)
print('Meu Dicionário: ',meu_dicionario)
print("""\nString 
Com
Varias
Linhas""") # """ três aspas pra quebrar linhas
print('\n\"Olá\" \nMundo\\ \n') # \ caractere de escape, \\ para apareer uma \ 
print(r"\Olá: \"Mundo\" ") # r antes das aspas permite sair a string crua, do jeito que esta escrito.

texto = 'Olá Mundo!'
numero = 5
print(texto.upper()); # tranforma texto em maiúsculo
print(texto.lower()); # tranforma texto em minúsculo
print("\n")

# Metodos Booleanos para verificar dados da String, retorna true ou false;
print('É alfanumérico: ',str.isalnum(texto)) # A string consiste apenas em caracteres alfanuméricos (sem símbolos);
print('É alfanumérico: ',texto.isalnum()) 
print('É sem símbolos: ', str.isalpha(texto)) # A string consiste apenas em caracteres alfabéticos (sem símbolos);
print('Esta em minúsculo: ',str.islower(texto)) # Os caracteres alfabéticos da string estão em letras minúsculas;
print('Só tem espaço em branco: ',str.isspace(texto)) # String consiste apenas em caracteres de espaço em branco;
print('Esta capitalizado: ',str.istitle(texto)) # String está com capitalização de título (Foo Bar);
print('Esta em maiúsculo: ',str.isupper(texto)); # Os caracteres alfabéticos da string estão em maiúsculas;
print('É numéricos: ', texto.isnumeric()) # String consiste apenas em caracteres numéricos;
print('É numéricos: ', str.isnumeric(texto))


# Booleanos usam AND, OR, NOT e nao usa:(&&, ||, !)
print('\nComparadores booleanos AND, OR e NOT')
print ((9 > 7) and (2 < 4)) # True V e V
print ((8 == 8) or (6 != 6)) # True V ou F
print (not (3 <= 1)) # True # nega a operação F=V
print('\n')


print(len(texto)) # Retorna o tamanho da string
print('-'.join('Mundo'))# Interpola a string com "-" sai: M-u-n-d-o
print(''.join(['M', 'u', 'n', 'd', 'o']))# Interpola a string com '' vazio sai: Mundo

print('Olá, Mundo'.split()) # Divide a string, apartir dos espaços em branco, sai : ['Olá,', 'mundo!']
print('Olá, Mundo'.split(',')) # Divide a string, apartir das virgulas, sai:  ['Olá', ' mundo!']

print('Olá, mundo!'.replace('mundo', 'todos')) # subistitui a palavra por outra, sai : Olá, todos!

print('Ola '+'Mundo')
print('Ola'+' '+'Mundo')