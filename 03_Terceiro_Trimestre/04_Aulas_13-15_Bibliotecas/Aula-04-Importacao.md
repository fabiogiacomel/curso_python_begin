# Aula 04: Bibliotecas (Modules)

**Objetivo:** Expandir os poderes do Python.

---

## 1. O comando `import`
O Python vem com "baterias incluídas", mas elas estão guardadas em caixas separadas para não pesar.
Para usar, precisamos importar.

```python
import math
import random
```

## 2. A Biblioteca `math` (Matemática)
Funções que vão além do `+ - * /`.

*   `math.sqrt(25)`: Raiz quadrada (Square Root). Dá 5.0.
*   `math.ceil(4.1)`: Arredonda para CIMA (Teto). Dá 5.
*   `math.floor(4.9)`: Arredonda para BAIXO (Chão). Dá 4.
*   `math.pow(2, 3)`: Potência (2 elevado a 3). Igual a `2 ** 3`.

## 3. A Biblioteca `random` (Aleatório)
Essencial para jogos e simulações.

*   `random.randint(1, 10)`: Sorteia um número INTEIRO entre 1 e 10.
*   `random.random()`: Sorteia um decimal entre 0.0 e 1.0.
*   `random.choice(lista)`: Escolhe um item aleatório de uma lista.

### Exemplo
```python
import random

frutas = ["Maçã", "Uva", "Banana"]
escolhida = random.choice(frutas)
print(f"A fruta do dia é: {escolhida}")
```
