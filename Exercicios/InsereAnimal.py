# Objetivo: Faça um Programa que gere uma lista de animal onde o usuário precisa preencher, só aceita nomes com mais de 3 letras.
# Entrada: Nome do animal.
# Saida:  Lista com os animais inseridos.
# Autor: Rafael Florentino.

animais = []
inseridos = 0
while inseridos <= 5:
    print('Digite o nome de um animal: ')
    animal = input()
    if len(animal) <= 3:
        print('\nNome deve ter mais de 3 letras.')
    else:
        animais.append(animal)
        inseridos += 1
print(animais)