
# 6 - Verificando Palíndromos 🔄
# Descrição: Vamos testar se uma palavra é um palíndromo.

# Solução:
palavra = input("Digite uma palavra: ")

# Invertendo a palavra
palavra_invertida = palavra[::-1]

# Verificando se é palíndromo
if palavra == palavra_invertida:
    print("A palavra", palavra, "é um palíndromo!")
else:
    print("A palavra", palavra, "não é um palíndromo.")
