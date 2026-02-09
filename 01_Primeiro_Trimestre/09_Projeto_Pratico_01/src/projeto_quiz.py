# Projeto Quiz - Exemplo Completo

print("="*30)
print("     QUIZ DE CONHECIMENTOS     ")
print("="*30)

pontuacao = 0

# --- Pergunta 1 ---
print("\n1. Qual a capital da França?")
print("a) Londres")
print("b) Paris")
print("c) Berlim")
resposta = input("Sua resposta: ")

if resposta == "b" or resposta == "Paris":
    print("✅ CERTA RESPOSTA!")
    pontuacao = pontuacao + 10
else:
    print("❌ ERROU! A capital é PARIS.")

# --- Pergunta 2 ---
print("\n2. Qual o resultado de 5 * 5?")
resposta_num = int(input("Sua resposta: "))

if resposta_num == 25:
    print("✅ ACERTOU MIZERAVI!")
    pontuacao = pontuacao + 10
else:
    print("❌ ERROU! É 25.")

# --- Pergunta 3 ---
print("\n3. O Python é uma linguagem de programação?")
print("Responda 'sim' ou 'nao'")
resp_txt = input("R: ")

if resp_txt == "sim":
    print("✅ ISSO AÍ!")
    pontuacao = pontuacao + 10
else:
    print("❌ ERROU! Claro que é.")

# --- Placar Final ---
print("\n" + "="*30)
print(f"PONTUAÇÃO FINAL: {pontuacao} pontos")

if pontuacao == 30:
    print("🏆 Nível: JEDI")
elif pontuacao >= 10:
    print("🙂 Nível: APRENDIZ")
else:
    print("😢 Nível: NOOB (Tente de novo)")
