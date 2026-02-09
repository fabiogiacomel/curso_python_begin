# Exercícios 07: Entrada e Saída

**Foco:** Conversar com o usuário e formatar respostas bonitas.

---

## Série A: Reprodução
**A1.** Crie `meu_dialogo.py`.
**A2.** Copie e execute. Responda as perguntas quando o programa pedir.

```python
nome = input("Qual seu nome? ")
cor = input("Qual sua cor favorita? ")
print(f"Olha só! O {nome} gosta de {cor}!")
```

---

## Série B: Modificação (Casting)
**B1.** O código abaixo tem um erro de lógica (ele concatena texto em vez de somar).
Corrija usando `int()` onde necessário para que ele some de verdade.

```python
# Código com "erro" (ele junta os números como texto)
n1 = input("Digite um número: ")
n2 = input("Digite outro: ")
soma = n1 + n2
print(f"A soma é {soma}")
```

**B2.** Execute com os números 5 e 5.
-   Antes de corrigir, deve dar `55`.
-   Depois de corrigir, deve dar `10`.

---

## Série C: Criação (Calculadora Simples)
**C1.** Crie um programa `dobro.py` que:
1.  Peça um número para o usuário: `Digite um número:`
2.  Calcule o dobro desse número (`numero * 2`).
3.  Mostre o resultado em uma frase bonita: `O dobro de X é Y.`

---

## Série D: Desafio (Interação Completa)
**D1.** Crie um programa para um **Cadastro de Jogador**.
Pergunte:
1.  Nome do Jogador (texto)
2.  Nível (número inteiro)
3.  Pontuação (número real/float)

No final, mostre um cartão formatado assim:
```text
--- PLAYER CARD ---
Name: [Nome]
Level: [Nível]
Points: [Pontuação]
-------------------
```
**Dica:** Use `f-string` para montar o cartão.
