# Exemplo 16: Classificação de Produto (Elif)

preco = float(input("Digite o preço do produto: "))

if preco < 50:
    print("Produto BARATO")
elif preco < 100:
    print("Produto NORMAL")
elif preco < 500:
    print("Produto CARO")
else:
    print("Produto MUITO CARO (Luxo)")

# Teste com:
# 30 (Barato)
# 80 (Normal)
# 200 (Caro)
# 1000 (Luxo)
