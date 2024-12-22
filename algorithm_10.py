
# Algoritmo 10: Encontrar números pares em uma lista
def numeros_pares(lista):
    return [x for x in lista if x % 2 == 0]

if __name__ == "__main__":
    print(numeros_pares([1, 2, 3, 4, 5, 6]))
