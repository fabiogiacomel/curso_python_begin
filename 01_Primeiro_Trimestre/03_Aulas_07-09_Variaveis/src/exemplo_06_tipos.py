# Exemplo 06: Tipos de Dados
# Python descobre o tipo automaticamente (Tipagem Dinâmica)

produto = "Notebook"   # String (str)
quantidade = 10        # Integer (int)
preco = 2500.50        # Float (float)
disponivel = True      # Boolean (bool)

print("--- Dados do Produto ---")
print(produto)
print(quantidade)
print(preco)
print(disponivel)

print("--- Tipos das Variáveis ---")
print(type(produto))
print(type(quantidade))
print(type(preco))
print(type(disponivel))

# CUIDADO: "10" é diferente de 10
numero_texto = "10"
numero_real = 10
print(type(numero_texto))
print(type(numero_real))
