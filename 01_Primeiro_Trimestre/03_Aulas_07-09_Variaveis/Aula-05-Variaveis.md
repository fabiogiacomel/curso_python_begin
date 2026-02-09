# Aula 05: Variáveis

**Objetivo:** Guardar valores para usar depois.

---

## O Conceito de Caixa (Variável)
Imagine que a memória do computador é um armazém gigante cheio de caixas.
Uma **variável** é uma etiqueta que colamos em uma caixa para saber o que tem dentro.

No código: `nome = "Maria"`
1.  O Python cria uma caixa na memória.
2.  Coloca o texto "Maria" dentro.
3.  Cola a etiqueta `nome` na caixa.

### Exemplo
Abra `src/exemplo_05_variaveis.py` e execute.

```python
mensagem = "Olá, tudo bem?"
print(mensagem)
```

O `print` não imprimiu a palavra "mensagem", ele imprimiu o que estava DENTRO da caixa `mensagem`.

---

## Regras para nomes de variáveis
1.  Não pode começar com número (`1nome` é proibido).
2.  Não pode ter espaços (`nome completo` é proibido). Use `_` (underline): `nome_completo`.
3.  O Python diferencia maiúsculas de minúsculas (`Idade` é diferente de `idade`).

---

## Mudando o valor
Podemos colocar outra coisa na mesma caixa. O valor antigo é jogado fora.

```python
idade = 15
print(idade) # Imprime 15

idade = 16
print(idade) # Imprime 16
```
