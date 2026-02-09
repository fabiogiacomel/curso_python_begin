# Aula 06: Análise de Dados

**Objetivo:** Responder perguntas sobre um conjunto de dados sem precisar olhar um por um.

---

## Funções Poderosas (Built-in)
O Python já sabe fazer contas com listas inteiras.
Suponha a lista: `vendas = [100, 200, 50, 500]`

### 1. Somar Tudo (`sum`)
```python
total = sum(vendas) # 850
```

### 2. O Maior Valor (`max`)
```python
melhor_venda = max(vendas) # 500
```

### 3. O Menor Valor (`min`)
```python
pior_venda = min(vendas) # 50
```

### 4. Quantidade (`len`)
```python
quantidade = len(vendas) # 4
```

## Combinando para criar a Média
A média não tem função pronta direta no Python básico (tem na biblioteca `statistics`, mas vamos fazer na mão para aprender a lógica).
**Média = Soma / Quantidade**

```python
media = sum(vendas) / len(vendas)
print(f"Média de vendas: {media}")
```
