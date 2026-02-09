# Exemplo 02: O poder do Range

print("--- Contando de 0 a 4 ---")
for i in range(5):
    print(i)

print("--- Contando de 1 a 5 ---")
for i in range(1, 6):
    print(i)

print("--- Números Pares (0 a 10) ---")
for n in range(0, 11, 2):
    print(f"Par: {n}")

print("--- Contagem Regressiva ---")
# Começa no 10, vai até -1 (para parar no 0), andando -1
for foguete in range(10, -1, -1):
    print(foguete)
print("FOGO!")
