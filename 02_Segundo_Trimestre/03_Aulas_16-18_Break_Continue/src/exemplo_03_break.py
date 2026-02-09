# Exemplo 03: Break e Continue

print("--- Exemplo 1: Break (Banco) ---")
# Imagine que você está procurando um saldo negativo na conta
saldos = [100, 50, 200, -10, 500]

for valor in saldos:
    print(f"Verificando valor: {valor}")
    if valor < 0:
        print("ALERTA: Saldo negativo encontrado! Parando análise.")
        break # Para tudo!

print("\n--- Exemplo 2: Continue (Pular Zeros) ---")
# Imagine que você vai dividir 100 por vários números
# Mas não pode dividir por 0!
numeros = [10, 5, 0, 2, 0, 4]

for n in numeros:
    if n == 0:
        print("Pulando divisão por zero...")
        continue # Vai para o próximo número da lista
    
    resultado = 100 / n
    print(f"100 dividido por {n} é {resultado}")
