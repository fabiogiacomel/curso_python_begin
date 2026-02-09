# Aula 03: O Laço For e Range

**Objetivo:** Repetição com controle total.

---

## O Comando `for` (Para)
O `for` percorre uma **sequência**. Ele pega um item de cada vez.

```python
for item in sequencia:
    <fazer algo com o item>
```

## A Função `range()` (Intervalo)
O `range` cria uma sequência de números para o `for` percorrer.

### 1. Range Simples (Até onde ir)
`range(5)` -> Gera: `0, 1, 2, 3, 4`
*   Começa no 0.
*   Vai **ATÉ** o 5 (mas não inclui o 5). São 5 dedos na mão, começando do 0.

### 2. Range com Início (De onde começar)
`range(1, 6)` -> Gera: `1, 2, 3, 4, 5`
*   Começa no 1.
*   Termina antes do 6.

### 3. Range com Passo (De quanto em quanto)
`range(0, 11, 2)` -> Gera: `0, 2, 4, 6, 8, 10`
*   Vai de 0 até 10, pulando de 2 em 2.

---

## Exemplo
Abra `src/exemplo_02_range.py`.

```python
# Repete 3 vezes
for n in range(3):
    print(f"Repetição número {n}")
```

## While vs For
*   **Use While:** Quando você **não sabe** quantas vezes vai repetir (Ex: "Até o usuário digitar a senha certa").
*   **Use For:** Quando você **sabe** o limite (Ex: "Repetir 10 vezes" ou "Ler todos os itens da lista").
