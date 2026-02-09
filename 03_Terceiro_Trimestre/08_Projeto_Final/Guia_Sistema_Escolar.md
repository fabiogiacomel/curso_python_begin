# Guia: Sistema de Gestão Escolar

## Passo 1: O esqueleto
Crie o loop principal com o menu.

```python
while True:
    print("1. Cadastrar")
    print("2. Listar")
    print("0. Sair")
    op = input("Opção: ")
    if op == "0": break
```

## Passo 2: Os Dados
Precisamos guardar os nomes e as médias.
```python
nomes = []
medias = []
```

## Passo 3: A Função Cadastrar
Essa é a parte mais complexa.
1.  Peça o nome.
2.  Faça um loop `for i in range(1, 4)` para pedir as 3 notas.
3.  Vá somando as notas.
4.  No final, divida por 3 para achar a média.
5.  Adicione nas listas: `nomes.append(nome)` e `medias.append(media)`.

## Passo 4: A Função Listar (Visualização)
Use um loop `for i in range(len(nomes))` para percorrer todos os alunos.
Use `f-strings` com alinhamento para ficar bonito:
`print(f"{nomes[i]:<20} | {medias[i]:.1f}")`
