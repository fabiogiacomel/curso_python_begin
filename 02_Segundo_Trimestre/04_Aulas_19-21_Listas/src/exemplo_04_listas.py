# Exemplo 04: Trabalhando com Listas

# Criando uma lista de notas
notas = [8.5, 7.0, 9.5, 6.0, 10.0]

print("--- Acessando ---")
print(f"Primeira nota: {notas[0]}")
print(f"Segunda nota: {notas[1]}")
print(f"Última nota: {notas[4]}")

# Usando índices negativos (conta de trás pra frente)
print(f"Última nota (jeito ninja): {notas[-1]}")

print("--- Modificando ---")
print(f"Antes: {notas}")
notas[1] = 7.5 # Corrigindo a segunda nota
print(f"Depois: {notas}")

print("--- Fatiando (Slicing) ---")
# Pegar as 3 primeiras (0, 1, 2)
primeiras = notas[0:3]
print(f"As 3 primeiras: {primeiras}")
