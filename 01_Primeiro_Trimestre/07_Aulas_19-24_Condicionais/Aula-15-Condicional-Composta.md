# Aula 15: Condicional Composta (if/else)

**Objetivo:** Criar dois caminhos. O programa escolhe um OU o outro. Nuca os dois.

---

## O comando `else` (Senão)
Usamos o `else` quando queremos garantir que algo aconteça caso o `if` falhe.

```python
if <condicao>:
    <caminho da verdade>
else:
    <caminho da mentira>
```

### Exemplo
Abra `src/exemplo_15_else.py`.

```python
idade = 15

if idade >= 18:
    print("Maior de idade. Pode dirigir.")
else:
    print("Menor de idade. Vá de bicicleta.")
```

**Nota:**
1.  O `else` **não** tem condição. Ele é "todo o resto".
2.  O `else` precisa de dois pontos `:`.
3.  O código dentro do `else` também precisa de **TAB**.
