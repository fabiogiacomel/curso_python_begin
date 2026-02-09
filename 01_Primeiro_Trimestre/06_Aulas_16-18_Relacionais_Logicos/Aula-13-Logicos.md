# Aula 13: Operadores Lógicos

**Objetivo:** Fazer perguntas mais complexas (compostas).

---

## 1. Operador `and` (E)
Só é verdade se **TUDO** for verdade.
Ex: "Para passar de ano, precisa ter nota azul **E** presença alta."

*   `True and True` = **True**
*   `True and False` = **False**
*   `False and False` = **False**

## 2. Operador `or` (OU)
É verdade se **PELO MENOS UM** for verdade.
Ex: "Hoje vou sair se fizer sol **OU** se eu tiver dinheiro."

*   `True or False` = **True**
*   `False or False` = **False**

## 3. Operador `not` (NÃO)
Inverte o valor.
*   `not True` = **False**
*   `not False` = **True**

### Exemplo Prático
Sou obrigado a votar?
```python
idade = 20
obrigado = idade >= 18 and idade < 70
```
