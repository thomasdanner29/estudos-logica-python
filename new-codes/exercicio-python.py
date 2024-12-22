def soma_impares(numeros):
    return sum(num for num in numeros if num % 2 != 0)

def subtracao_impares(numeros):
    impares = [num for num in numeros if num % 2 != 0]
    resultado = impares[0]
    for num in impares[1:]:
        resultado -= num
    return resultado

# Exemplo de uso
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Soma dos ímpares:", soma_impares(numeros))
print("Subtração dos ímpares:", subtracao_impares(numeros))