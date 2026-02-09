# Exemplo 03: Return e Escopo

def calcular_media(nota1, nota2):
    soma = nota1 + nota2
    media = soma / 2
    return media # Devolve o valor 8.5 (por exemplo)

def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

# --- USANDO ---

aluno1 = calcular_media(8, 9)
resultado1 = verificar_aprovacao(aluno1)

print(f"Aluno 1: Média {aluno1} -> {resultado1}")

# Podemos fazer tudo direto, sem criar variáveis intermediárias
resultado2 = verificar_aprovacao(calcular_media(5, 6))
print(f"Aluno 2: {resultado2}")

# Teste de Escopo (Descomente para ver o erro)
# print(soma) 
# Erro: A variável 'soma' só existe DENTRO da função calcular_media.
