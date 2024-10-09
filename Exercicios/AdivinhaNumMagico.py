secret_number = 777
numero = 0

print(
"""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhe o número que escolhi   |
| para você.                        |
| Então, qual é o número secreto?   |
+===================================+
""")

while numero != secret_number:
    try:
        numero = int(input("Digite o número que você acha que o mágico escolheu: "))
        if numero == secret_number:
            print("Parabéns! Você adivinhou o número secreto!")
        elif numero < secret_number:
            print("O número secreto é maior.")
        else:
            print("O número secreto é menor.")
    except ValueError:
        print("Por favor, insira um número inteiro.")