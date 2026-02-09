# Exercícios 02: Laço For

---

## Série A: Reprodução
**A1.** Crie `meu_for.py`.
**A2.** Copie para ver a tabuada do 5:
```python
print("Tabuada do 5")
for n in range(1, 11):
    resultado = 5 * n
    print(f"5 x {n} = {resultado}")
```

---

## Série B: Modificação (Tabuada Flexível)
**B1.** Mude o código para perguntar qual tabuada o usuário quer (`input` + `int`).
**B2.** Use a variável digitada no lugar do número 5 fixo.

---

## Série C: Criação (Soma de 1 a 100)
**C1.** Crie um programa que some todos os números de 1 a 100.
1.  Crie uma variável `soma = 0` (acumulador).
2.  Faça um loop de 1 a 100 (`range(1, 101)`).
3.  Dentro do loop, some o número atual na variável `soma` (`soma = soma + i`).
4.  No final (fora do loop), mostre o total.

---

## Série D: Desafio (Números Ímpares)
**D1.** Peça um número final para o usuário (ex: 50).
**D2.** Imprima apenas os números ímpares de 1 até esse número.
Use o `range()` com passo 2, começando do 1.

Exemplo:
`Digite o limite: 10`
`1`
`3`
`5`
`7`
`9`
