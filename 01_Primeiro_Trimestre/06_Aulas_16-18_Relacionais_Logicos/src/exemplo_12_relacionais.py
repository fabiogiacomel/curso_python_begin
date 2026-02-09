# Exemplo 12: Comparações
# O resultado é sempre True ou False

a = 10
b = 5

print(f"A={a}, B={b}")
print("---")

print(f"A é igual a B? {a == b}")
print(f"A é diferente de B? {a != b}")
print(f"A é maior que B? {a > b}")
print(f"A é menor que B? {a < b}")

# Comparando textos
senha_correta = "1234"
senha_digitada = input("Digite a senha: ")

print(f"Acesso liberado? {senha_digitada == senha_correta}")
