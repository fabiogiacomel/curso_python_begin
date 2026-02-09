# Exemplo 15: Par ou Ímpar

numero = int(input("Digite um número inteiro: "))

# Verifica o resto da divisão por 2
if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")

# O programa NUNCA vai imprimir "PAR" e "ÍMPAR" ao mesmo tempo.
# É um ou outro.
