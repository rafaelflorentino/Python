# Objetivo: Programa que receba 2 nota do aluno, média abaixo de 5.0 reprovado, media entre 5.0 e 6.9 recuperação, media 7.0 ou 
# superior aprovado.
# Entrada: Ano de nascimento, sexo.
# Saida: Mensagem com o asituação do alistamento da pessoa.
# Autor: Rafael Florentino.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/ 2

if media < 5:
    print('sua média foi: {:.1f}, REPROVADO!'.format(media))
elif media >= 5 and media < 7:
    print('Sua média foi: {:.1f}, RECUPERAÇÃO!!'.format(media))
else:
    print('Sua média foi: {:.1f}, APROVADO!!!'.format(media))
