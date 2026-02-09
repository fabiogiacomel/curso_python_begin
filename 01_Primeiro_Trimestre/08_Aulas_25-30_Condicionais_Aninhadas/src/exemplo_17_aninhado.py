# Exemplo 17: Jogo de Adivinhação com Dica (Aninhado)

numero_secreto = 7
chute = int(input("Adivinhe o número (0 a 10): "))

if chute == numero_secreto:
    print("Parabéns! Você acertou na mosca.")
else:
    print("Você errou...")
    # Condicional aninhada (só roda se errou)
    if chute > numero_secreto:
        print("Dica: O número secreto é MENOR.")
    else:
        print("Dica: O número secreto é MAIOR.")

    print("Tente de novo na próxima!")
