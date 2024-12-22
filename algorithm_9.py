
# Algoritmo 9: Calcular a média de uma lista de números
def calcular_media(lista):
    return sum(lista) / len(lista) if lista else 0

if __name__ == "__main__":
    print(calcular_media([10, 20, 30, 40, 50]))
