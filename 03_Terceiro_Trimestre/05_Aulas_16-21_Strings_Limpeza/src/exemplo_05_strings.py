# Exemplo 05: Limpeza de Dados

msg_suja = "   OlÁ MunDO   "

print(f"Original: '{msg_suja}'")

# 1. Limpando espaços
limpa = msg_suja.strip()
print(f"Sem espaços: '{limpa}'")

# 2. Padronizando
print(f"Maiúsculo: {limpa.upper()}")
print(f"Minúsculo: {limpa.lower()}")

# 3. Substituindo
texto_errado = "Eu gosto de Java"
texto_corrigido = texto_errado.replace("Java", "Python")
print(f"\nFrase errada: {texto_errado}")
print(f"Frase corrigida: {texto_corrigido}")

# 4. Fatiamento (Slicing) de Texto
cpf = "123.456.789-00"
# Pegar só os 3 primeiros números
inicio = cpf[0:3]
print(f"\nOs primeiros dígitos do CPF são: {inicio}")
