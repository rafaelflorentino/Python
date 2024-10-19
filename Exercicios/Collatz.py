# Solicita ao usuário para inserir um número natural
c0 = int(input("Insira um número natural (diferente de zero): "))

# Verifica se o número é válido
if c0 <= 0:
    print("O número deve ser maior que zero.")
else:
    # Inicializa a contagem de etapas
    steps = 0

    # Loop para executar as operações até c0 ser igual a 1
    while c0 != 1:
        print(c0)
        if c0 % 2 == 0:
            c0 = c0 // 2
        else:
            c0 = 3 * c0 + 1
        steps += 1

    # Imprime o valor final de c0 e o número de etapas
    print(c0)
    print("Número de etapas:", steps)