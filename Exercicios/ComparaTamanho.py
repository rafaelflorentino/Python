# Objetivo: Escreva um programa que leia 2 numeros inteiros e fale qual e o maior valor, qual e o menor valor ou sãp iguais.
# Entrada: Dois Números.
# Saida: Número e maior menor ou igual.
# Autor: Rafael Florentino.

primeiro = int(input('Digite o primeiro valor: ').strip())
segundo = int(input('Digite o segundo valor: ').strip())

if primeiro > segundo :
    print('O primeiro valor: {} e MAIOR que o segundo valor: {}'.format(primeiro,segundo))
elif segundo > primeiro :
    print('O segundo valor: {} e MAIOR que o primeiro valor: {}'.format(segundo,primeiro))
else:
    print('O primeiro valor: {} e segundo o valor: {}, SÃO IGUAIS!'.format(segundo, primeiro))