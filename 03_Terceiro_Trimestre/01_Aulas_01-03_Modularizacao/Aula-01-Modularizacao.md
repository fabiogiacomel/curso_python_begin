# Aula 01: Modularização (Funções)

**Objetivo:** Criar seus próprios comandos.

---

## O Problema
Imagine que toda vez que você quisesse limpar a tela ou mostrar um menu, tivesse que escrever 10 linhas de código.
Se precisar mudar algo, terá que mudar em TODOS os lugares.

## A Solução: Funções (`def`)
Uma função é um bloco de código com um **nome**.
Quando você chama o nome, o código roda.

### Sintaxe
```python
def nome_da_funcao():
    <codigo indentado>
```

### Exemplo
```python
def dar_oi():
    print("Olá, tudo bem?")
    print("Seja bem-vindo!")

# Usando a função (Chamada)
dar_oi()
dar_oi()
dar_oi()
```
Isso vai imprimir as mensagens 3 vezes.

## Regras
1.  O `def` só **CRIA** a função. Ele não executa.
2.  Você precisa **CHAMAR** a função usando parênteses `()` para ela rodar.
3.  O `def` deve ficar no começo do arquivo (boas práticas).
