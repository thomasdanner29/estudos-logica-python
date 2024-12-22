
# Algoritmo 8: Contar vogais em uma string
def contar_vogais(string):
    vogais = "aeiouAEIOU"
    return sum(1 for char in string if char in vogais)

if __name__ == "__main__":
    print(contar_vogais("Olá Mundo"))
