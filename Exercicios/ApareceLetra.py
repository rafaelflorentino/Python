# Objetivo: Faça um programa que leia uma frase pelo teclado e diga quantas vezes aparece a letra a, em que posição ela aparece 
# a primeira vez, em que posição ela aparece a ultima vez.
# Entrada: Frase.
# Saida: Letra, palavra, posição.
# Autor: Rafael Florentino.

""""Início do programa """

frase = str(input('Digite uma frase: ').strip()).lower()

print('A letra a aparece: {} vezes'.format(frase.count('a')))
print('A primeira Letra a aparece na posição {}'.format(frase.find('a')+1))
print('A Ultima Letra a aparece na posição {}'.format(frase.rfind('a')+1))

""""Fim do programa """