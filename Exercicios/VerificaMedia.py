# Objetivo: Faça um Programa que recebe 2 notas e calcule a média, se media >= 6 aprovado,parabnens boa nota <6 reprovado, sua nota 
# foi ruim estude mais, 
# Entrada: Duas notas.
# Saida: Média, mensagem de aprovado ou reprovado.
# Autor: Rafael Florentino.

nota1 = float(input('Digite a primeira nota: ').strip()) # .strip() remove espaõ emb branco, 
nota2 = float(input('Digite a segunda nota: ').strip())
media = (nota1 + nota2) /2

print('\nAPROVADO' if media >= 6 else '\nREPROVADO')
print('Sua média é: {}'.format(media))
if media >= 6:
    print('Sua média foi Boa! PARABÉNS!!')
else:
    print('Sua média foi Ruim! ESTUDE MAIS')
print('\n')


# Objetivo: Faça um Programa que recebe o ano do carro se for <= 3 carro novo senao carro velho
# Entrada: Ano do carro.
# Saida: Mensagem se o carro e novo ou velho.
# Autor: Rafael Florentino.

tempo = int(input('Digite quantos anos tem seu carro: ').strip())

if tempo <= 3:
    print('Parabéns seu Carro é Novo!')
else:
    print('Infelizmente seu Carro é Velho...')
print('Continue com o Carro, ele ainda está Novo!' if tempo <=3 else 'Venda o Carro pois já esta Velho e compre um Carro Novo.')
print('\n--FIM--')
print('\n')

# Objetivo: Faça um Programa que recebeum nome caso nome == rafael, mensagem dizendo: 'Que nome Lindo você tem!!!' se não mensagem
# dizendo: 'Seu nome é tão normal e imprima uma mensagem de bom dia com o nome da pessoa.
# Entrada: Ano do carro.
# Saida: Mensagem se o carro e novo ou velho.
# Autor: Rafael Florentino.

nome = str(input('Digite o seu nome: ')).strip()  # txt.strip(",.grt") remove , . g r t da string
print('Bom dia {}'.format(nome))
if nome == 'rafael':
    print('Que nome Lindo você tem!!!')
else:
    print('Seu nome é tão normal...')
print('\n')
