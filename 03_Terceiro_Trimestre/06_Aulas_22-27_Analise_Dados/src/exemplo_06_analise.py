# Exemplo 06: Analisando Temperaturas

temperaturas = [28.5, 30.2, 25.0, 18.5, 32.0, 29.0]

print(f"Dados: {temperaturas}")

# 1. Análise Básica
print(f"Temperatura Máxima: {max(temperaturas)}°C")
print(f"Temperatura Mínima: {min(temperaturas)}°C")

# 2. Média
soma_temp = sum(temperaturas)
qtd_dias = len(temperaturas)
media = soma_temp / qtd_dias

print(f"Média da semana: {media:.1f}°C")

# 3. Análise Condicional (Quantos dias quentes?)
# Para isso, precisamos iterar (Aula passada)
quentes = 0
for t in temperaturas:
    if t > 30:
        quentes = quentes + 1

print(f"Dias muito quentes (>30°C): {quentes}")
