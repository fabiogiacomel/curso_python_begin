# Guia de Desenvolvimento: Quiz

Não tente escrever tudo de uma vez. Vá por etapas (Steps).

## Etapa 1: A Estrutura Básica
Crie um arquivo `quiz.py`.
1.  Dê boas vindas.
2.  Crie uma variável `pontos` começando com 0.

```python
print("Bem-vindo ao Quiz Python!")
pontos = 0
```

## Etapa 2: A Primeira Pergunta
1.  Use `input` para fazer a pergunta.
2.  Use `if` para ver se acertou.
3.  Se acertou: Aumente `pontos` e dê parabéns.
4.  Se errou: Mostre a resposta certa e não dê pontos.

```python
print("P1: Quanto é 2 + 2?")
resp = input("R: ")

if resp == "4":
    print("Correto!")
    pontos = pontos + 1
else:
    print("Errado! A resposta é 4.")
```

## Etapa 3: Mais Perguntas
Copie e cole a estrutura da Etapa 2, mudando a pergunta e a resposta.
Faça pelo menos mais 2 perguntas diferentes.
*   Dica: Cuidado com maiúsculas/minúsculas nas respostas de texto!

## Etapa 4: Resultado Final
No final do código, use `if/elif/else` para avaliar o desempenho.
*   Se acertou tudo: "Você é um gênio!"
*   Se acertou mais ou menos: "Muito bom!"
*   Se errou tudo: "Precisa estudar mais."

Mostre a pontuação final com `f-string`.
