# Objetivo: Programa que recebe o ano do nascimento do jovem: se for menor de 18 mensagem de não precisa se alistar, é tambem 
# quanto tempo falta para ele se alistar, caso tenha 18 mensagem de já está na hora de se alistar; caso mais de 18 mensagem de 
# Já passou do praso de se alistar, é quanto tempo já passou do prazo.
# Entrada: Ano de nascimento, sexo.
# Saida: Mensagem com o asituação do alistamento da pessoa.
# Autor: Rafael Florentino.

from datetime import date
ano = date.today().year
sexo = str(input('Digite o sexo da pessoa: '))

if sexo =='femenino':
    print('\nO alistamento não e obrigatório para o sexo Femenino.')
else:
    nascimento = int(input('Digite o ano em que você nasceu: '))
    idade = ano - nascimento
    if idade < 18:
        print('\nQuem nasceu em {} tem {} anos de idade em {}.'.format(nascimento, idade, ano))
        print('Ainda falta {} anos para você se alistar.'.format(18 - idade))
        print('Seu alistamento vai ser em {}'.format(nascimento + (18 - idade) ))

    elif idade == 18:
        print('\nQuem nasceu em {} tem {} anos de idade em {}.'.format(nascimento, idade, ano))
        print('Você está na idade de se Alistar IMEDIATAMENTE!!!.'.format(idade))
    else:
        print('\nQuem nasceu em {} tem {} anos de idade em {}.'.format(nascimento, idade, ano))
        print('Você já deveria ter se alistado há {} anos.'.format(idade -18))
        print('Seu alistamento foi em {}.'.format(nascimento + 18))
