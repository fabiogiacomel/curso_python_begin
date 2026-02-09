# Projeto Final: Sistema de Gestão Escolar
import os # Para limpar a tela (opcional)
import time # Para esperar um pouco (opcional)

# --- BANCO DE DADOS (Listas) ---
nomes = []
medias = []

# --- FUNÇÕES ---

def limpar_tela():
    # Comando para limpar tela no Windows (cls) ou Linux/Mac (clear)
    os.system('cls' if os.name == 'nt' else 'clear')

def titulo(texto):
    limpar_tela()
    print("=" * 40)
    print(f"{texto:^40}") # Centraliza o texto
    print("=" * 40)

def cadastrar():
    titulo("CADASTRO DE ALUNO")
    nome = input("Nome do Aluno: ").strip().title()
    
    # Validando notas (Loop até digitar certo)
    notas = []
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"Nota {i} (0-10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break # Sai do while e vai para a próxima nota
                else:
                    print("Erro: A nota deve ser entre 0 e 10.")
            except ValueError:
                print("Erro: Digite um número válido.")

    # Calculando média
    media_final = sum(notas) / len(notas)
    
    # Salvando nas listas principais
    nomes.append(nome)
    medias.append(media_final)
    print(f"\nSucesso! Média de {nome}: {media_final:.1f}")
    time.sleep(2)

def listar():
    titulo("LISTA DE ALUNOS")
    print(f"{'ID':<4} | {'NOME':<20} | {'MÉDIA':<5} | {'SITUAÇÃO'}")
    print("-" * 45)
    
    for i in range(len(nomes)):
        nome = nomes[i]
        media = medias[i]
        
        situacao = "APROVADO" if media >= 7 else "REPROVADO"
        
        print(f"{i:<4} | {nome:<20} | {media:<5.1f} | {situacao}")
    
    input("\nPressione ENTER para voltar...")

def relatorio():
    titulo("RELATÓRIO VISUAL DA TURMA")
    if len(medias) == 0:
        print("Nenhum dado para mostrar.")
    else:
        maior = max(medias)
        menor = min(medias)
        geral = sum(medias) / len(medias)
        
        print(f"Média Geral da Turma: {geral:.1f}")
        print(f"Melhor aluno: {maior:.1f}")
        print(f"Pior aluno:   {menor:.1f}")
        print("-" * 30)
        
        print("\nGRÁFICO DE DESEMPENHO:")
        for i in range(len(nomes)):
            nome = nomes[i]
            media = medias[i]
            barra = "█" * int(media) # Cada ponto vale um quadrado
            print(f"{nome:<10} | {barra} {media:.1f}")
            
    input("\nPressione ENTER para voltar...")

# --- PROGRAMA PRINCIPAL ---

while True:
    titulo("SISTEMA ESCOLAR v1.0")
    print("1. Cadastrar Aluno")
    print("2. Listar Turma")
    print("3. Relatório Estatístico")
    print("0. Sair")
    
    opcao = input("\nEscolha: ")
    
    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        relatorio()
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida!")
        time.sleep(1)
