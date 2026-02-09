# Aula 14: Condicional Simples (if)

**Objetivo:** Fazer um código que só roda AS VEZES.

---

## O comando `if` (Se)
Funciona assim:
```python
if <condicao>:
    <codigo que roda se for verdade>
```

### A IMPORTÂNCIA DA INDENTAÇÃO
No Python, o **espaço** no começo da linha diz o que está "dentro" do `if`.
Geralmente usamos a tecla **TAB** (ou 4 espaços).

#### Exemplo
Abra `src/exemplo_14_if.py`.

```python
idade = 20

if idade >= 18:
    print("Você é maior de idade.") # Tem TAB no começo
    print("Pode entrar.")           # Tem TAB no começo

print("Fim do programa.")           # NÃO tem TAB (roda sempre)
```

Se a idade for 10:
*   O Python pula as linhas com TAB.
*   Imprime apenas "Fim do programa.".

Se a idade for 20:
*   O Python entra no bloco com TAB.
*   Imprime tudo.

---

**Regra:** Sem o TAB (indentação), o Python dá erro (`IndentationError`).
