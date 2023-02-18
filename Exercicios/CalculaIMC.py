# Objetivo: Recebe peso, altura, e calcule o imc da pessoa.
# Entrada: Peso, altura.
# Saida: Imc da pessoa.
# Autor: Rafael Florentino.

peso = float(input('Digite seu peso? (kg): '))
altura = float(input('digite sua altura? (m): '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu IMC é: {}'.format(imc))
    print('Você está ABAIXO DO PESO.')
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é: {}'.format(imc))
    print('Você está com o PESO IDEAL.')
elif imc > 25 and imc <= 30:
    print('Seu IMC é: {}'.format(imc))
    print('Você está com SOBREPESO.')
elif imc > 30 and imc <=40:
    print('Seu IMC é: {}'.format(imc))
    print('Você está com OBESIDADE.')
elif imc > 40:
    print('Seu IMC é: {}'.format(imc))
    print('Você está com OBESIDADE MÓRBIDA.')

