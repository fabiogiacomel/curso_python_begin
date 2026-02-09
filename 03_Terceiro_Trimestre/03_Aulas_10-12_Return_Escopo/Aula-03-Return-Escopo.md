# Aula 03: Return e Escopo

**Objetivo:** Parar de apenas mostrar coisas na tela e começar a **usar** os resultados.

---

## 1. O comando `return`
Até agora, nossas funções usavam `print`. Elas mostravam o resultado e jogavam fora.
O `return` **entrega** o resultado para quem chamou a função.

### Exemplo: A Pizzaria
*   **Função com Print:** O pizzaiolo faz a pizza e come na sua frente (mostra, mas não te dá).
*   **Função com Return:** O pizzaiolo faz a pizza e **te entrega** na caixa.

```python
def somar_com_return(n1, n2):
    resultado = n1 + n2
    return resultado

# Agora eu posso guardar o valor numa variável!
minha_soma = somar_com_return(10, 20)
print(f"O triplo da soma é {minha_soma * 3}")
```

## 2. Print vs Return
*   `print`: Só serve para o humano ler. O computador não consegue usar o valor depois.
*   `return`: Serve para o computador continuar calculando.

## 3. Escopo (Vida das Variáveis)
Variáveis criadas **DENTRO** da função só existem lá dentro (Escopo Local).
Se você tentar usar fora, dá erro.

```python
def teste():
    segredo = 123
    print(segredo) # Funciona

# print(segredo) # ERRO! O computador não sabe o que é 'segredo' aqui fora.
```
