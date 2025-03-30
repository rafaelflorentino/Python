hat_list = [1, 2, 3, 4, 5] # Lista atual de números ocultos no hat

# Etapa 1
numero_usuario = int(input("Insira um número inteiro para substituir o número do meio: "))
hat_list[len(hat_list) // 2] = numero_usuario

# Etapa 2
hat_list.pop()

# Etapa 3
print("Comprimento atual da lista:", len(hat_list))

print(hat_list)