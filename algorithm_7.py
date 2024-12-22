
# Algoritmo 7: Verificar se uma palavra é um palíndromo
def is_palindromo(palavra):
    return palavra == palavra[::-1]

if __name__ == "__main__":
    print(is_palindromo("arara"))
