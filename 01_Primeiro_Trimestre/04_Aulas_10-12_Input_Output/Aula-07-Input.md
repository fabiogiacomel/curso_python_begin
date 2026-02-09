# Aula 07: Entrada de Dados (Input)

**Objetivo:** Fazer o programa parar e esperar o usuário digitar algo.

---

## O Comando `input()`
Quando o Python encontra um `input()`, ele **pausa** e fica piscando o cursor, esperando você digitar e apertar ENTER.

### Exemplo
Abra `src/exemplo_07_input.py`.

```python
nome = input("Digite seu nome: ")
print("Olá, " + nome)
```

1.  O texto dentro do `input("...")` é a pergunta que aparece na tela.
2.  O que você digitar vai para dentro da caixa (variável) `nome`.

---

## O Problema do Texto
O `input()` **SEMPRE** lê tudo como **Texto (str)**. Mesmo que você digite um número.

```python
idade = input("Sua idade: ")
# Se você digitar 15, a variável idade terá o texto "15"
# Você NÃO pode fazer contas com texto!
```

### A Solução: Converter (Casting)
Se queremos ler um número, temos que avisar o Python para converter.

*   `int( texto )` -> Transforma em Inteiro.
*   `float( texto )` -> Transforma em Decimal.

```python
idade_texto = input("Digite sua idade: ")
idade_numero = int(idade_texto)
# Agora sim é um número!
```

Ou, mais comum (tudo numa linha só):
```python
idade = int(input("Digite sua idade: "))
```
