# Aula 10: Divisão Inteira e Resto

**Objetivo:** Fazer contas de "dividir balas para crianças" (onde não dá para quebrar a bala).

---

## 1. Divisão Inteira (`//`)
Pega apenas a parte inteira do resultado, jogando fora o decimal.

*   `5 / 2` = `2.5` (Divisão Normal)
*   `5 // 2` = `2` (Divisão Inteira)

## 2. Resto da Divisão ou Módulo (`%`)
Lembra da conta de divisão na chave? O "resto" é o que sobra lá embaixo.

*   Se eu tenho 5 balas para 2 crianças:
    *   Cada uma ganha 2 balas (`5 // 2`).
    *   Sobra **1** bala (`5 % 2`).

### Para que serve o `%`?
O uso mais comum é descobrir se um número é **Par ou Ímpar**.
*   Todo número par dividido por 2 sobra 0 (Ex: `10 % 2` é `0`).
*   Todo número ímpar dividido por 2 sobra 1 (Ex: `5 % 2` é `1`).

```python
print(10 % 3) # Sobra 1 (3 x 3 = 9, para 10 falta 1)
```
