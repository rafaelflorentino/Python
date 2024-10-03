def calcular_imposto(renda):
    if renda <= 85528:
        imposto = (0.18 * renda) - 556.02
    else:
        imposto = 14839.02 + (0.32 * (renda - 85528))
    
    # Se o imposto for menor que zero, deve ser igual a zero
    if imposto < 0:
        imposto = 0
    
    # Arredondar o imposto para o valor inteiro mais próximo
    imposto = round(imposto)
    
    return imposto

# Exemplo de uso:
renda = float(input("Digite a sua renda: "))
imposto_calculado = calcular_imposto(renda)
print(f"O imposto calculado é: {imposto_calculado} talões")