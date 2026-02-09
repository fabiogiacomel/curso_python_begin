# Projeto Calculadora - Exemplo Completo

print("--- SUPER CALCULADORA ---")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

opcao = input("Escolha a operação (1-4): ")

# Pedindo os números
num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))

if opcao == "1":
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")

elif opcao == "2":
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")

elif opcao == "3":
    resultado = num1 * num2
    print(f"Resultado: {num1} * {num2} = {resultado}")

elif opcao == "4":
    # Tratamento de erro (Divisão por Zero)
    if num2 == 0:
        print("ERRO: Não é possível dividir por zero!")
    else:
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")

else:
    print("Opção Inválida! Escolha de 1 a 4.")
