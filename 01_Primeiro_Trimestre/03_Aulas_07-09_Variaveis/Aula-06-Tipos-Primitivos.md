# Aula 06: Tipos Primitivos

**Objetivo:** Entender que dados diferentes têm comportamentos diferentes.

---

## Os 4 Tipos Básicos
O Python precisa saber se o dado é texto ou número para saber o que fazer com ele.
(Não dá para somar "Maçã" + "Banana" matematicamente).

### 1. `str` (String / Texto)
-   Sempre entre aspas: `"Olá"`, `'123'`, `"A"`.
-   É uma corrente (string) de caracteres.

### 2. `int` (Integer / Inteiro)
-   Números sem vírgula: `1`, `10`, `-5`, `0`.
-   Usado para contar coisas.

### 3. `float` (Floating Point / Ponto Flutuante)
-   Números com vírgula (ponto em inglês): `1.5`, `3.14`, `-0.01`.
-   Usado para medidas, dinheiro, notas.
-   **Atenção:** Use PONTO `.`, não vírgula `,`.

### 4. `bool` (Boolean / Lógico)
-   Só tem dois valores: `True` (Verdadeiro) ou `False` (Falso).
-   Usado para lógica e condições.

---

## Como descobrir o tipo?
A função `type()` diz o tipo de uma variável.

Abra `src/exemplo_06_tipos.py`:
```python
nome = "Ana"
idade = 17
altura = 1.65
estudante = True

print(type(nome))       # <class 'str'>
print(type(idade))      # <class 'int'>
print(type(altura))     # <class 'float'>
print(type(estudante))  # <class 'bool'>
```
