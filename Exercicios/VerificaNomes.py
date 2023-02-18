# Objetivo: Crie um programa que leia o nome de uma pessoa e diga se tem SILVA no nome.
# Entrada: Nome.
# Saida: Mensagem se contém silva no nome.
# Autor: Rafael Florentino.

nome = str(input('Digite um nome: ')).strip()

print('Tem silva no nome: {}'.format('silva' in nome.lower()))

"""if nome.count('silva') > 0:
    print('A pessoa tem silva no nome!!!')
else:
    print('A pessoa Não tem silva no nome.')"""