# Exemplo 02: Funções com Parâmetros

# Função que recebe UM dado
def saudar(nome_pessoa):
    print(f"Bem-vindo(a), {nome_pessoa}!")
    print("Espero que você goste do sistema.")
    print("-" * 20)

# Função que recebe DOIS dados
def calcular_area(largura, altura):
    area = largura * altura
    print(f"Uma sala de {largura}x{altura} tem {area} metros quadrados.")

# --- USANDO AS FUNÇÕES ---

# Teste 1: Saudação
saudar("Ana")
saudar("Pedro")

# Teste 2: Área
calcular_area(5, 4)  # 20m²
calcular_area(10, 10) # 100m²
