# Aula 02: Funções com Parâmetros

**Objetivo:** Fazer a função trabalhar com dados diferentes a cada vez.

---

## O Problema
A função `dar_oi()` da aula passada sempre dizia a mesma coisa.
E se eu quisesse dizer "Oi, Fabio" ou "Oi, Maria"?

## A Solução: Parâmetros
O que colocamos dentro dos parênteses `()` funciona como uma **variável temporária**.

### Sintaxe
```python
def dar_oi(nome):
    print(f"Olá, {nome}!")
```

### Usando (Chamada)
Agora somos **obrigados** a entregar um nome quando chamamos a função.

```python
dar_oi("Fabio") # Imprime: Olá, Fabio!
dar_oi("Maria") # Imprime: Olá, Maria!
```

## Múltiplos Parâmetros
Podemos pedir quantas coisas quisermos, separando por vírgula.

```python
def somar(n1, n2):
    resultado = n1 + n2
    print(f"A soma é {resultado}")

somar(10, 5) # 15
somar(50, 50) # 100
```
Importante: A ordem importa! O primeiro valor vai para `n1`, o segundo para `n2`.
