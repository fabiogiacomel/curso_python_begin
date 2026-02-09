# Exemplo 05: Manipulando Listas

# Lista de convidados inicial
convidados = ["Ana", "Bruno", "Carlos"]
print(f"Início: {convidados}")

# 1. Chegou mais gente (append)
print("Chegando Daniel e Eduardo...")
convidados.append("Daniel")
convidados.append("Eduardo")
print(convidados)

# 2. Alguém foi embora (remove)
print("Bruno foi embora...")
convidados.remove("Bruno")
print(convidados)

# 3. Organizando a fila (sort)
print("Organizando por ordem alfabética...")
convidados.sort()
print(convidados)

# 4. Contando quantos tem (len)
total = len(convidados)
print(f"Temos {total} pessoas na festa.")
