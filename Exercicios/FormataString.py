# Objetivo: Faça um Programa que concatene strings, e receba um número e diga qual e oseu antecessor e seu sucessor.
# Entrada: Número inteiro.
# Saida: Mensagem, o número e seu antecessor e o sucessor.
# Autor: Rafael Florentino.

print('Pedro tem {} laranjas e {} maças'.format(5,2)) # Coloca valores na ordem que as variáveis foram passados.
print('Pedro tem {1} laranjas e {0} maças'.format(5,2)) # Ordem das variáveis de acordo com a posição que vc coloca.
print('Pedro tem {of} laranjas e {1} maças {0} peras'.format('cinco','quatro',of="duas")) # usa chave pra chamar valor

modelo = 'Pedro tem {0:s} laranjas e {1:3d} maças e {2:.3f} peras.' #:s coonveerte em string; :3d faz ter 3 digitos ou espaço
print(modelo.format("cinco",10, 3.55477)) # :.3f limita as casas decimais do float para 3 depois da virgula.

numero = int(input('Digite um numero: '))
antecessor = numero -1
sucessor = numero + 1

print('Analisando o valor', numero, ' Seu antecessor é:', antecessor, 'Seu sucessor é:',sucessor)
print('Analisando o valor {}, Seu antecessor é: {} Seu sucessor é: {}'.format(numero, antecessor, sucessor))
print('Analisando o valor {}, Seu antecessor é: {} Seu sucessor é: {}'.format(numero, numero-1, numero+1))
