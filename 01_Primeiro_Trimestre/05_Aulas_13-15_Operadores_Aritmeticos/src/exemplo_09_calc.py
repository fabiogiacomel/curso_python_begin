# Exemplo 09: Calculadora Básica

a = 10
b = 3

print(f"Números: {a} e {b}")
print("-" * 20) # Truque: Multiplicar texto repete ele!

print(f"Soma:           {a + b}")
print(f"Subtração:      {a - b}")
print(f"Multiplicação:  {a * b}")
print(f"Divisão Real:   {a / b:.2f}") # Formatando com 2 casas
print(f"Divisão Inteira:{a // b}")    # Só a parte inteira
print(f"Resto (Módulo): {a % b}")     # O que sobra
print(f"Potência:       {a ** 2}")    # 10 ao quadrado
