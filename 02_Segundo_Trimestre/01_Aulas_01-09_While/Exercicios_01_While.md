# Exercícios 01: Laço While

**ATENÇÃO:** Para parar um LOOP INFINITO, clique no terminal e aperte `Ctrl + C`.

---

## Série A: Reprodução
**A1.** Crie `meu_loop.py`.
**A2.** Copie e execute:
```python
n = 0
while n < 3:
    print("Repetindo...")
    n = n + 1
```

---

## Série B: Modificação (Passo)
**B1.** Mude o código para contar de 2 em 2 (0, 2, 4, 6... até 20).
-   Dica: Mude a condição (`< 21`) e o passo (`n = n + 2`).

---

## Série C: Criação (Tabuada)
**C1.** Crie um programa que pede um número para o usuário (ex: 7).
**C2.** Use o `while` para mostrar a tabuada desse número de 1 a 10.
Exemplo:
`7 x 1 = 7`
`7 x 2 = 14`
...
`7 x 10 = 70`

---

## Série D: Desafio (Senha Infinita)
**D1.** Crie um sistema de login chato.
1.  Peça a senha.
2.  **ENQUANTO** a senha não for "1234", mostre "Erro!" e peça de novo.
3.  Quando acertar, o loop acaba e o programa diz "Bem-vindo!".

```python
senha = input("Senha: ")

while senha != "1234":
    print("Senha errada!")
    senha = input("Tente de novo: ")

print("Acesso Liberado!")
```
**Pergunta:** Por que precisamos pedir a senha duas vezes (uma fora e uma dentro do loop)?
