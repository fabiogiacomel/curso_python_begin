# Exemplo 06: Iteração (For Each)

print("--- Lista de Compras ---")
compras = ["Arroz", "Feijão", "Batata", "Carne"]

# Para cada 'item' na lista 'compras':
for item in compras:
    print(f"Preciso comprar: {item}")


print("\n--- Calculando a Média ---")
notas = [8.5, 7.0, 9.5, 6.0]
soma = 0

for nota in notas:
    print(f"Somando nota: {nota}")
    soma = soma + nota # Acumula o valor

media = soma / len(notas)
print(f"A média final é: {media}")


print("\n--- Filtrando (Só Pares) ---")
numeros = [1, 2, 3, 4, 5, 6, 7, 8]

for n in numeros:
    if n % 2 == 0:
        print(f"{n} é PAR")
