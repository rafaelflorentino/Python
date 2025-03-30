# 3) Type annotations
def calcular_taxa(faturamento: float) -> float:
    if faturamento < 1000:
        taxa = 0
    elif faturamento < 10000:
        taxa= 0.1
    elif faturamento < 500000:
        taxa= 0.15
    else:
        taxa = 0.2
    return taxa

def calcular_imposto(faturamento: float) -> float:
    #  2) divisão de funções
    # Chama e traz o resultado da funcção calcular taxa
    taxa = calcular_taxa(faturamento)
        
    imposto = taxa * faturamento
    print(imposto)
    return imposto

# so executa abaixo se este arquivo.py estiver sendo executado, se outro aqruivo importar não executa as linhas abaixo
# 1 ) Testar moduluos
if __name__ == "__main__":
    # calcular_imposto(1000)    
    
   
    faturamentos = [1000, 1500, 3000, 4000, 70000, 300000, 51000]
    
    # 4) list comprehension 
    #  isso:
    impostos = []
    for faturamento in faturamentos:
        imposto = calcular_imposto(faturamento)
        impostos.append(imposto)
    print ("\n Fim \n")  
      
    # vira isso:
    impostos2 = [calcular_imposto(faturamento) for faturamento in faturamentos ]
    print (impostos2)
    print ("\n Fim3 \n")  
    
    # tambem posso
    impostos3 = list(map(calcular_imposto, faturamentos))
    print (impostos3)  