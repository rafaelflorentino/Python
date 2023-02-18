# Objetivo: Crie um programa que receba a temperatura em graus Celcius, e converta em Fahrenheit
# Entrada: Graus Celcius.
# Saida: Graus em fahrenheit.
# Autor: Rafael Florentino.

celsius = float(input('Digite a temperatura em graus Celsius: '))
fahrenheit = ((9 * celsius) / 5) + 32

print('A quantidade em Celsius: {}°C; a quantidade em Fahrenheit é: {}°F'.format(celsius, fahrenheit))