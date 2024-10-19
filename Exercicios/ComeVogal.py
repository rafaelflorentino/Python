# Solicita ao usuário para inserir uma palavra
user_word = input("Digite uma palavra: ")

# Converte a palavra para maiúsculas
user_word = user_word.upper()

# Loop for para percorrer cada letra da palavra
for letter in user_word:
    # Verifica se a letra é uma vogal
    if letter in 'AEIOU':
        continue
    # Imprime as letras não consumidas em linhas separadas
    print(letter)