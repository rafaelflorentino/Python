# Solicita ao usuário para inserir uma palavra
user_word = input("Digite uma palavra: ")

# Converte a palavra para maiúsculas
user_word = user_word.upper()

# Inicializa uma variável para armazenar as letras não consumidas
word_without_vowels = ""

# Loop for para percorrer cada letra da palavra
for letter in user_word:
    # Verifica se a letra é uma vogal
    if letter in 'AEIOU':
        continue
    # Concatena as letras não consumidas na variável word_without_vowels
    word_without_vowels += letter

# Imprime a variável word_without_vowels
print(word_without_vowels)