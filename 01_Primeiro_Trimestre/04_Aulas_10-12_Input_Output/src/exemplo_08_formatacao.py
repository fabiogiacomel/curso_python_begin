# Exemplo 08: f-strings (Formatação)

produto = "Celular"
preco = 2150.999
desconto = 0.10 # 10%

valor_com_desconto = preco - (preco * desconto)

# Sem formatação (fica feio)
print("--- Sem formatação ---")
print("Produto: " + produto)
print("Preço final: " + str(valor_com_desconto))

# Com f-string (fica bonito)
print("--- Com f-string ---")
print(f"O produto {produto} custava R$ {preco:.2f}")
print(f"Com desconto, sai por R$ {valor_com_desconto:.2f}")
