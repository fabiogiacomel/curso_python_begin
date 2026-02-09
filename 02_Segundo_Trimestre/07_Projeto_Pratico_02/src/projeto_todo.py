# Projeto: ToDo List (Gerenciador de Tarefas)

tarefas = []

while True:
    print("\n" + "="*20)
    print("AGENDA DE TAREFAS")
    print("="*20)
    print("1. Nova Tarefa")
    print("2. Listar Tarefas")
    print("3. Concluir Tarefa (Apagar)")
    print("0. Sair")
    
    opcao = input("Opção: ")

    if opcao == "0":
        print("Saindo... Até mais!")
        break

    elif opcao == "1":
        nome = input("Digite a tarefa: ")
        tarefas.append(nome)
        print("Tarefa salva!")

    elif opcao == "2":
        print("\n--- SUAS TAREFAS ---")
        # Dica: 'enumerate' numera automaticamente
        # Se não quiser usar enumerate, use um contador manual
        for i, t in enumerate(tarefas):
            print(f"{i} - {t}")
            
        if len(tarefas) == 0:
            print("(Nenhuma tarefa pendente)")

    elif opcao == "3":
        indice = int(input("Digite o número da tarefa para apagar: "))
        
        # Verificando se o número existe para não dar erro
        if indice >= 0 and indice < len(tarefas):
            removida = tarefas.pop(indice)
            print(f"Tarefa '{removida}' concluída com sucesso!")
        else:
            print("ERRO: Tarefa não encontrada.")

    else:
        print("Opção inválida.")
