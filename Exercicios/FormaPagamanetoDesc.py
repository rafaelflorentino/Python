# Objetivo: Calcule o preço a ser pago de um produto, recebe preço normal e condição de pagamento: a vista dinheiro/cheque, 10% 
# de desconto; a vista no cartão, 5% de desconto, 2x no cartão preço normal, 3x no cartão juros de 20%.
# Entrada: Valor da Compra, forma de pagamento.
# Saida: Valor da compra com juros, desconto ou normal.
# Autor: Rafael Florentino.

"""" Início do programa """

print('{:=^40}'.format('LOJAS RAFAEL'))

valor = float(input('Digite o valor das compras R$: '))
print('''Digite a forma de pagamento:
[ 1 ] Dinheiro ou Cheque
[ 2 ] A vista no Cartão
[ 3 ] 2x no Cartão
[ 4 ] 3x ou mais no Cartão: ''')
formapagamento = int(input('Sua opção? '))

if formapagamento == 1:
    final = valor - (valor / 100 * 10)
    print("\nForma de Pagamento: Dinheiro/Cheque.")
elif formapagamento == 2:
    final = valor - (valor / 100 * 5)
    print("\nForma de Pagamento: A vista Cartão.")
elif formapagamento == 3:
    final = valor
    print("\nForma de Pagamento: 2x Cartão, valor das parcelas: {}".format(final/2))
elif formapagamento == 4:
    final = valor + (valor / 100 * 20)
    print("\nForma de Pagamento: 3x ou mais no Cartão.")
    parcelas = int(input('Quantas parcelas? '))
    print("\nForma de Pagamento: {}x Cartão".format(parcelas))
else:
    final = 0
    print("\nForma de Pagamento inválida, Tente novamente.")
print("Valor da compra: {}; Valor a ser pago: {}".format(valor, final))

"""" Fim do programa """