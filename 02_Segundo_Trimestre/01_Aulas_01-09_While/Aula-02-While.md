# Aula 02: O Laço While (Enquanto)

**Objetivo:** Repetir um bloco de código enquanto uma condição for verdadeira.

---

## Sintaxe
É quase igual ao `if`, mas ele volta para o começo!

```python
while <condicao>:
    <codigo a repetir>
    <passo de mudanca>
```

### Exemplo: Contar até 5
Precisamos de 3 coisas para um loop funcionar bem no `while`:
1.  **Início:** Uma variável de controle (contador).
2.  **Condição:** O teste para saber se continua.
3.  **Passo:** Mudar a variável para não ficar preso para sempre.

Abra `src/exemplo_01_contagem.py`.

```python
contador = 1          # 1. Início

while contador <= 5:  # 2. Condição
    print(contador)
    contador = contador + 1 # 3. Passo (Incremento)

print("Fim!")
```

## O Perigo: Loop Infinito
Se você esquecer o passo (`contador = contador + 1`), a condição `1 <= 5` será SEMPRE verdadeira.
O programa nunca vai parar de imprimir "1".
Isso trava o computador!
**Para parar:** Use `Ctrl + C` no terminal.
