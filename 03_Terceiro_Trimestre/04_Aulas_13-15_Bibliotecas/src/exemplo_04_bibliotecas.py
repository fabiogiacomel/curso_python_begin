# Exemplo 04: Math e Random

import math
import random

print("--- Matemática ---")
numero = 16
raiz = math.sqrt(numero)
print(f"A raiz quadrada de {numero} é {raiz}")

nota_quebrada = 9.2
print(f"Nota original: {nota_quebrada}")
print(f"Arredondada pra cima: {math.ceil(nota_quebrada)}")
print(f"Arredondada pra baixo: {math.floor(nota_quebrada)}")

print("\n--- Sorteio (Random) ---")
dado = random.randint(1, 6)
print(f"Você jogou o dado e saiu: {dado}")

moeda = ["Cara", "Coroa"]
resultado = random.choice(moeda)
print(f"Jogando a moeda... Deu {resultado}!")
