# Objetivo: Função que calcula o enésimo número de Fibonacci
# Entrada: Sem entrada.
# Saida: O enésimo número de Fibonacci.
# Autor: Rafael Florentino.

def Fibonacci(n): # Função Fibonacci(n); Funçôes usam () parenteses;
    if n<=0: # Número menor ou igual 0, não aceita negativos nem 0
        print('Entrada inválida')
    # O primeiro número de Fibonacci é 0
    elif n==1:
        return 0
    # O segundo número de Fibonacci é 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

if __name__ == '__main__': # Função principal, de inicialização
    print(Fibonacci(9)) # Chama a função Fibonnacci()
