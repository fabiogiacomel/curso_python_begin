# Aula 02: Decomposição (Dividir para Conquistar)

**Objetivo:** Aprender a quebrar um problema grande em pedaços pequenos.

---

## O que é Decomposição?
É transformar uma tarefa difícil em várias tarefas fáceis. O computador precisa de instruções *simples*.

### Exemplo: "Fazer o Café da Manhã"
Isso é muito vago para um robô. Vamos decompor:

1.  Fazer café
2.  Torrar pão
3.  Servir frutas

Ainda está vago. Vamos decompor "Fazer café":
1.1. Esquentar água
1.2. Colocar pó no filtro
1.3. Passar a água

Agora sim! Passos pequenos são mais fáceis de programar.

---

## Exemplo Prático: O Robô que Anda
Imagine um robô em um grid (tabuleiro). Ele precisa ir do ponto A ao ponto B.

**Problema:** Ir até a porta.
**Decomposição:**
1.  Andar 2 passos
2.  Virar à direita
3.  Andar 3 passos

### Veja o Código (Exemplo Python)
Abra o arquivo `src/exemplo_02_robot.py`.
Neste exemplo, vamos simular o robô falando o que está fazendo.

```python
print("--- INICIANDO ROBÔ ---")
print("Passo 1: Frente")
print("Passo 2: Frente")
print("Passo 3: Virar Direita")
print("Passo 4: Frente")
print("Passo 5: Frente")
print("Passo 6: Frente")
print("--- CHEGOU ---")
```

---

## Abstração (Ignorar Detalhes)
Quando dizemos "Andar", não precisamos detalhar "ligar motor da perna esquerda, mover 30 graus...". Nós **abstraímos** (escondemos) a complexidade.
Em Python, usamos funções para isso (veremos mais tarde), mas por enquanto, entenda que comandos como `print` são abstrações. Você não sabe como o Python coloca letras na tela, você só usa!

---

## Próximos Passos
Vá para `Exercicios_02.md` para praticar decomposição.
