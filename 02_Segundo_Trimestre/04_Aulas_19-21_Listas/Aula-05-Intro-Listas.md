# Aula 05: Introdução às Listas

**Objetivo:** Parar de criar `variavel1`, `variavel2`, `variavel3`... e usar uma lista só!

---

## 1. O que é uma Lista?
É uma variável especial que guarda vários valores, separados por vírgula, dentro de **colchetes `[]`**.

```python
# Sem lista (ruim)
fruta1 = "Maçã"
fruta2 = "Banana"
fruta3 = "Uva"

# Com lista (bom)
frutas = ["Maçã", "Banana", "Uva"]
```

## 2. Acessando Itens (Índice)
Cada item tem um número (endereço).
**IMPORTANTE:** A contagem começa no **ZERO**!

*   `frutas[0]` -> "Maçã"
*   `frutas[1]` -> "Banana"
*   `frutas[2]` -> "Uva"

## 3. Tamanho da Lista (`len`)
Para saber quantos itens tem:
```python
print(len(frutas)) # Vai dar 3
```

## 4. Fatiamento (Slicing)
Pegar um pedaço da lista.
`lista[inicio:fim]` (O fim não é incluído, igual ao `range`).

*   `frutas[0:2]` -> Pega o 0 e o 1 ("Maçã", "Banana").
