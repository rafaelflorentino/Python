# Objetivo: Faça um Programa que receba do teclado e verifique o tipo, se o valor e numérico ou não, se esta maiusculo, minusculo,
# capitalizado, se só contem espaços.
# Entrada: Qualquer valor.
# Saida: Mensagem contendo informações sobre o valor digitado.
# Autor: Rafael Florentino.

v = input('Digite algo: ')
print('O tipo do valor: ', type(v))
print('O valor digitado e númerico: ',v.isnumeric())
print('O valor digitado e textual: ',v.isalpha())
print('O valor digitado e alfanúmerico: ',v.isalnum())
print('O valor digitado esta so em minusculo: ',v.isupper())
print('O valor digitado esta so em maiúsculo: ',v.islower())
print('O valor digitado esta Captitalizado: ',v.istitle())
print('O valor digitado so contem espaços em branco: ',v.isspace())



