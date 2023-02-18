# Objetivo: Crie um programa que leia o nome de uma cidade e diga se começa com a palavra SANTO.
# Entrada: Nome da cidade.
# Saida: Mensagem se contem Santo no nome da cidade.
# Autor: Rafael Florentino.

cidade = str(input('Digite o nome da cidade: ')).strip()

print(cidade[:5].upper() == 'SANTO')

"""" santo em qualquer lugar da palavra
c = cidade.split()
if c[0].count('santo') > 0:
    print('A cidade tem santo no nome:')
else:
    print('A cidade Não tem santo no nome') """