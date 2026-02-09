# Aula 07: Iteração (Percorrendo Listas)

**Objetivo:** Fazer o computador ler a lista inteira para nós.

---

## O Comando `for` com Listas
Já usamos o `for` com `range()`. Agora vamos usar direto na lista.
É muito fácil. O Python pega um item de cada vez.

```python
animais = ["Gato", "Cachorro", "Pato"]

for bicho in animais:
    print(f"Olha o {bicho}!")
```

O computador faz assim:
1.  Pega "Gato", chama de `bicho` -> Executa o print.
2.  Pega "Cachorro", chama de `bicho` -> Executa o print.
3.  Pega "Pato", chama de `bicho` -> Executa o print.
4.  Acabou a lista? Para.

## Filtrando Dados (Busca)
Podemos colocar um `if` dentro do loop para achar coisas específicas.

```python
numeros = [10, 5, 8, 20, 3]

for n in numeros:
    if n > 9:
        print(f"{n} é um número grande!")
```

## Somando Tudo (Acumulador)
```python
total = 0
precos = [10, 20, 30]

for p in precos:
    total = total + p

print(f"Total: {total}")
```
