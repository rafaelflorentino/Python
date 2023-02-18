# Objetivo: Programa que receba o ano de nascimento e diga qual a categoria de natação do atleta: 1)até 9 mirim 2)até 14 infantil
# 3)até 19 júnior 4)até 20 sénior 5) Acima 20 master.
# Entrada: Ano de nascimento, sexo.
# Saida: Mensagem com o asituação do alistamento da pessoa.
# Autor: Rafael Florentino.

"""" Início do Programa """

from datetime import date
ano = date.today().year
nascimento = int(input('Digite o ano que você nasceu: '))
idade = ano - nascimento;

if idade <= 9:
    print('Sua idade é: {}, categoria: MIRIM'.format(idade))
elif idade > 9 and idade <= 14:
    print('Sua idade é: {}, categoria: INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('Sua idade é: {}, categoria: JUNIOR'.format(idade))
elif idade > 19 and idade <= 20:
    print('Sua idade é: {}, categoria: SÉNIOR'.format(idade))
else:
    print('Sua idade é: {}, categoria: MASTER'.format(idade))

"""" Fim do Programa """