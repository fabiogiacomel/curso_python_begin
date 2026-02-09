# Exercícios 09: Matemática com Python

---

## Série A: Reprodução
**A1.** Crie `meu_calculo.py` e execute:

```python
x = 5
y = 2
print(f"Soma: {x + y}")
print(f"Potência: {x ** y}")
print(f"Resto da divisão: {x % y}")
```

---

## Série B: Modificação
**B1.** Mude `x` para `10` e `y` para `3`.
**B2.** Antes de rodar, tente adivinhar:
-   Quanto é `10 % 3`? (Resto de 10 dividido por 3)
-   Quanto é `10 // 3`? (Divisão inteira)

Execute e confira.

---

## Série C: Criação (Conversor de Temperaturas)
**C1.** Crie um programa que converta Graus Celsius para Fahrenheit.
A fórmula é: `F = C * 1.8 + 32`

1.  Peça a temperatura em C (`input` e `float`).
2.  Faça a conta.
3.  Mostre o resultado.

---

## Série D: Desafio (Média Escolar)
**D1.** Crie um programa que calcula a média de 3 notas.

**Atenção à Precedência!**
Se você fizer `n1 + n2 + n3 / 3`, o Python vai dividir só a nota 3!
Use parênteses para somar tudo primeiro.

Exemplo de saída:
```text
Nota 1: 8.0
Nota 2: 7.5
Nota 3: 9.0
A média é: 8.16
```
(Dica: use `:.2f` para ficar bonito)
