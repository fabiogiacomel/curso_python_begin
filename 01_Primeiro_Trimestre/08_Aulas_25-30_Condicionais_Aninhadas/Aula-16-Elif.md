# Aula 16: O comando Elif (Senão Se)

**Objetivo:** Escolher entre várias opções.

---

## O Problema do `if/else`
O `if/else` só serve para 2 caminhos (Verdadeiro ou Falso).
E se eu tiver 3 opções? (Ex: Positivo, Negativo ou Zero?)

Poderíamos fazer muitos `if` separados, mas o computador testaria todos à toa.

## A Solução: `elif`
É um "Meio Termo". Se o primeiro `if` falhar, ele testa o `elif`. Se o `elif` falhar, ele tenta o próximo... até chegar no `else` final.

```python
if <condicao 1>:
    <faz isso>
elif <condicao 2>:
    <faz aquilo>
else:
    <faz o resto>
```

### Exemplo
Abra `src/exemplo_16_elif.py`.

```python
idade = 10

if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")
```

**Importante:** Assim que o Python encontra uma verdade, ele executa e **PULA** todo o resto. Ele não testa os outros `elif`.
