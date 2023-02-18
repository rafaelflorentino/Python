# Objetivo: Mostre as diferenças entre um codigo Python correto e um errado
# Entrada: Sem entrada.
# Saida:  Mensagem e números na tela.
# Autor: Rafael Florentino.

# For correto
letras = ["P", "F"]
for x in letras:
    print(x)

# For errado

#letras == ["P", "F"]
#for x in letras
#{
#print(x)
#} # Só precisava de um =, não dois ==; Faltou os : depois de letras, e não precisava das { } e faltou identação de espaços antes do print.


# If Correto
if 5 > 2:
    print("True!")

#if Errado

# If 5 > 2
#{
#print("True!")
#} # Faltou os : depois do 2, e não precisava das { } e faltou identação de espaços antes do print.


# While Correto
a,b = 0,1 # a=0 e b=1 atribuir varios valores e uma vez.
while b < 10: # 1 < 10
    print (b) # 1
    a, b = b, a+b # a=b(1) e b=a+b(0+1=1)





