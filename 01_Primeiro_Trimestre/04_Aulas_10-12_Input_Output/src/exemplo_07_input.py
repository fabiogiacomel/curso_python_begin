# Exemplo 07: Interagindo com o usuário
# O input pausa o programa e espera o Enter

print("--- CADASTRO ---")
nome = input("Digite seu nome completo: ")
cidade = input("Onde você mora? ")

print("--- RESUMO ---")
print("Nome cadastrado:")
print(nome)
print("Cidade:")
print(cidade)

# Exemplo de erro comum (descomente para testar o erro)
# num1 = input("Digite um número: ") # Vai ser texto "10"
# num2 = input("Digite outro: ")     # Vai ser texto "5"
# print(num1 + num2)                 # Vai juntar texto: "105" (NÃO soma!)

# O jeito certo de somar
n1 = int(input("Digite um numero real: "))
n2 = int(input("Digite outro: "))
print(n1 + n2) # Agora soma 15
