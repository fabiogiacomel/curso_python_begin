# Exemplo 07: Gráficos no Terminal

vendas = {
    "Segunda": 5,
    "Terça": 12,
    "Quarta": 8,
    "Quinta": 15,
    "Sexta": 20
}
# Nota: Estou usando Dicionário (chave: valor) para facilitar,
# mas poderia ser duas listas (dias e valores).

print("\n--- GRÁFICO DE VENDAS SEMANAIS ---")
print("(Cada # vale 1 venda)")

for dia, qtd in vendas.items():
    barra = "#" * qtd
    # {dia:<8} faz o dia ocupar 8 espaços fixos
    print(f"{dia:<8} | {barra} ({qtd})")

print("-" * 30)

print("\n--- GRÁFICO DE BATERIA ---")
carga = 75
tamanho_total = 20
# Regra de 3 para saber quantos quadradinhos pintar
pintar = int((carga / 100) * tamanho_total)
vazio = tamanho_total - pintar

barra_carga = "█" * pintar
barra_vazia = "░" * vazio

print(f"Bateria: [{barra_carga}{barra_vazia}] {carga}%")
