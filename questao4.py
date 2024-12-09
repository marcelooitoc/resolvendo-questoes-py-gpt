
# 4 - Verificando Números Pares e Ímpares 🧮
# Descrição: Como entrada, receba um número inteiro e verifique se ele é par ou ímpar.

# Solução:
numero = int(input("Digite um número inteiro: "))

# Verificando se o número é par ou ímpar
if numero % 2 == 0:
    print("O número", numero, "é par.")
else:
    print("O número", numero, "é ímpar.")
