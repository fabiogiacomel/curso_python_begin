# Aula 06: Métodos de Listas

**Objetivo:** Adicionar e tirar coisas da "gaveta".

---

## O Ponto Mágico `.`
Listas têm "superpoderes" (métodos) que acessamos usando o PONTO `.`.
`lista.comando()`

### 1. Adicionar (`append`)
Coloca um item novo no **FINAL** da lista.
```python
mochila = ["Caneta", "Caderno"]
mochila.append("Borracha")
# Agora mochila tem 3 itens
```

### 2. Remover pelo Valor (`remove`)
Procura o item e tira a **primeira** aparição dele.
```python
mochila.remove("Caneta")
# Agora só tem Caderno e Borracha
```
*   **Cuidado:** Se o item não existir, dá Erro!

### 3. Remover pela Posição (`pop`)
Tira o item de um índice específico.
```python
mochila.pop(0) # Tira o primeiro item
```

### 4. Ordenar (`sort`)
Coloca em ordem alfabética ou numérica.
```python
numeros = [5, 1, 8, 3]
numeros.sort() # Vira [1, 3, 5, 8]
```
