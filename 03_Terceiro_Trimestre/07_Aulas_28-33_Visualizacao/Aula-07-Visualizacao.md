# Aula 07: Visualização de Dados (ASCII Art)

**Objetivo:** "Uma imagem vale mais que mil números".

---

## 1. Multiplicação de Strings
No Python, podemos multiplicar texto!
`"A" * 5` vira `"AAAAA"`.

Isso é perfeito para fazer gráficos de barra simples.
Se o valor é 10, desenhamos 10 asteriscos.

```python
valor = 5
barra = "#" * valor
print(f"{valor} | {barra}")
# Resultado:
# 5 | #####
```

## 2. Alinhamento com F-Strings
Para o gráfico ficar bonito, os nomes precisam ter o mesmo tamanho.
Podemos forçar um tamanho usando `:10` (ocupa 10 espaços).

*   `{variavel:<10}`: Alinha à ESQUERDA (padrão).
*   `{variavel:>10}`: Alinha à DIREITA.
*   `{variavel:^10}`: CENTRALIZA.

### Exemplo
```python
nome = "Ana"
print(f"|{nome:<10}|") # |Ana       |
print(f"|{nome:>10}|") # |       Ana|
```
