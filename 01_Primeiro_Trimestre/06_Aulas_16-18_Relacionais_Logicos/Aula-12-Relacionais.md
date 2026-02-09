# Aula 12: Operadores Relacionais

**Objetivo:** Comparar coisas. O resultado de uma comparação é SEMPRE um Booleano (`True` ou `False`).

---

## A Tabela de Comparação

| Símbolo | Significado | Exemplo | Resultado |
| :---: | :--- | :--- | :--- |
| `==` | Igual a | `5 == 5` | `True` |
| `!=` | Diferente de | `5 != 3` | `True` |
| `>` | Maior que | `10 > 2` | `True` |
| `<` | Menor que | `10 < 2` | `False` |
| `>=` | Maior ou Igual | `10 >= 10` | `True` |
| `<=` | Menor ou Igual | `5 <= 4` | `False` |

### CUIDADO: `==` vs `=`
*   `=` (um igual): **ATRIBUIÇÃO**. (Guarda valor na caixa).
*   `==` (dois iguais): **COMPARAÇÃO**. (Pergunta se é igual).

```python
x = 10  # Guarda 10 no x
x == 10 # Pergunta: x é igual a 10? (Responde True)
```
