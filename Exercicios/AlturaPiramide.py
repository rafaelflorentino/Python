# Solicita ao usuário para inserir o número de blocos
blocks = int(input("Insira o número de blocos: "))

# Inicializa as variáveis
altura = 0
blocos_usados = 0

# Loop para construir a pirâmide
while blocos_usados + (altura + 1) <= blocks:
    altura += 1
    blocos_usados += altura

# Imprime a altura da pirâmide
print("A altura da pirâmide:", altura)