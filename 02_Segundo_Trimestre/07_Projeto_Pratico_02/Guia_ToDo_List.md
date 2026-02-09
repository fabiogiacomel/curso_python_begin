# Guia: Criando sua ToDo List

## Etapa 1: O Menu Loop
Comece criando a lista vazia e o loop infinito.

```python
tarefas = []

while True:
    print("\n--- MENU ---")
    print("1. Adicionar Tarefa")
    print("2. Ver Tarefas")
    print("3. Sair")
    
    opcao = input("Escolha: ")
    
    if opcao == "3":
        break
```

## Etapa 2: Adicionar
Se a opção for 1, peça o nome da tarefa e adicione `append`.
```python
    elif opcao == "1":
        nova = input("O que precisa fazer? ")
        tarefas.append(nova)
        print("Adicionado!")
```

## Etapa 3: Listar (O Pulo do Gato)
Para mostrar os números bonitinhos (1. Estudar), precisamos de um contador manual ou usar o `enumerate` (extra). Vamos fazer com contador manual.

```python
    elif opcao == "2":
        print("\n--- LISTA ---")
        i = 0
        for t in tarefas:
            print(f"{i}. {t}")
            i = i + 1
```

## Etapa 4: Remover
Pedimos o número (índice) para remover com `pop`.
**CUIDADO:** O usuário conta a partir do 1? Ou do 0? Decida isso no seu código. Se mostrar a partir do 0, é mais fácil.

```python
    elif opcao == "4": # Adicione essa opção no menu lá em cima!
        numero = int(input("Qual número apagar? "))
        tarefas.pop(numero)
```
