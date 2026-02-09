# Exercícios 03: Controle de Fluxo

---

## Série A: Reprodução
**A1.** Crie `meu_break.py`.
**A2.** Copie o código abaixo. Ele deveria contar até 10, mas algo vai parar ele no 5.
```python
x = 0
while x < 10:
    x = x + 1
    if x == 5:
        break
    print(x)
print("Fim")
```

---

## Série B: Modificação (Pular o 13)
**B1.** Faça um loop de 1 a 20 (`range`).
**B2.** Se o número for 13, use `continue` para não imprimir ele (dizem que dá azar).
Imprima todos os outros.

---

## Série C: Criação (Menu Infinito)
**C1.** Crie uma Calculadora que NUNCA para.
1.  Use `while True`.
2.  Mostre as opções: `1. Somar` e `0. Sair`.
3.  Peça a opção.
4.  Se for `1`, peça dois números e some.
5.  Se for `0`, mostre "Tchau!" e use `break` para encerrar.
6.  Se for outra coisa, mostre "Opção inválida".

---

## Série D: Desafio (Login com 3 tentativas)
**D1.** Crie um sistema de senha que bloqueia após 3 erros.
1.  Use um loop `for` com `range(3)` (para dar 3 chances).
2.  Peça a senha.
3.  Se acertar:
    *   Mostre "Bem-vindo!"
    *   Use `break` para parar de perguntar.
4.  Se errar:
    *   Mostre "Senha incorreta".
5.  Se o loop acabar sem o break (você pode testar isso com `else` no for, ou apenas colocar uma mensagem de "Conta Bloqueada" se usar uma variável de controle), avise que bloqueou.

**Dica:** Uma forma simples de saber se bloqueou é criar uma variável `acertou = False` antes do loop e mudar para `True` se acertar. No final, se `acertou` continuar `False`, é porque falhou todas.
