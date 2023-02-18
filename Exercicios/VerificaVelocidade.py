# Objetivo: Faça um Programa que que leia a velocidade do carro, se passar de 80km/h avisar que foi multado e calculle o valor da 
# multa 7,00 reais para cada kilometro acima da velocidade.
# Entrada: Velocidade do carro.
# Saida: Mensagem Dentro do limite ou Mensagem de multa com valor da multa.
# Autor: Rafael Florentino.
velocidade = float(input('Digite a velocidade atual do carro: ').strip())

if velocidade < 80 :
    print('Velocidade Dentro do limite: {}'.format(velocidade))
elif velocidade == 80 :
    print('Você atingiu o limite maximo permitido de velocidade: {}'.format(velocidade))
else: # velocidade > 80 :
    multa = (velocidade - 80) * 7
    print('Você foi MULTADO! Excedeu o limite de 80km/h, valor da multa: R${} reais.'. format(multa))
print('Tenha um bom dia! dirija em segurança.')