# Aula 03: Hello World (Olá Mundo)

**Objetivo:** Fazer o computador falar com a gente pela primeira vez.

---

## O Comando `print()`
O comando `print` serve para **imprimir** (escrever) uma mensagem na tela do computador.

### Exemplo 1: O Clássico
Abra `src/exemplo_03_hello.py` e execute.

```python
print("Hello, World!")
```

### Regras Importantes (Sintaxe)
1.  **Parênteses `()`:** O `print` é uma função, e funções precisam de parênteses.
2.  **Aspas `""`:** Textos precisam estar dentro de aspas (podem ser simples `'` ou duplas `"`).

---

## O que acontece se errar? (Erros de Sintaxe)
Se você esquecer um parêntese, o Python vai reclamar. Isso se chama **Syntax Error**.

**Errado:**
`print "Olá"` (Faltam parênteses)

**Errado:**
`print(Olá)` (Faltam aspas - o Python acha que Olá é uma variável, veremos isso depois)

**Correto:**
`print("Olá")`

---

## Exercício Rápido
Tente fazer o computador escrever seu nome completo em 3 linhas diferentes.
```python
print("Meu nome é:")
print("Bond")
print("James Bond")
```
