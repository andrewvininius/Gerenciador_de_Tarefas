import os

def exibir_tarefas(tarefas):
    if not tarefas:
        print("Não há tarefas na lista.")
    else:
        print("Lista de Tarefas:")
        for idx, tarefa in enumerate(tarefas, start=1):
            print(f"{idx}. {tarefa}")

def adicionar_tarefa(tarefas):
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def editar_tarefa(tarefas):
    exibir_tarefas(tarefas)
    indice = int(input("Digite o número da tarefa que deseja editar: ")) - 1
    if 0 <= indice < len(tarefas):
        nova_tarefa = input("Digite a nova tarefa: ")
        tarefas[indice] = nova_tarefa
        print("Tarefa editada com sucesso!")
    else:
        print("Índice inválido.")

def excluir_tarefa(tarefas):
    exibir_tarefas(tarefas)
    indice = int(input("Digite o número da tarefa que deseja excluir: ")) - 1
    if 0 <= indice < len(tarefas):
        tarefa_excluida = tarefas.pop(indice)
        print(f"Tarefa '{tarefa_excluida}' excluída com sucesso!")
    else:
        print("Índice inválido.")

def salvar_tarefas_arquivo(nome_arquivo, tarefas):
    with open(nome_arquivo, "w") as arquivo:
        for tarefa in tarefas:
            arquivo.write(tarefa + "\n")

def carregar_tarefas_arquivo(nome_arquivo):
    tarefas = []
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, "r") as arquivo:
            tarefas = arquivo.read().splitlines()
    return tarefas

def main():
    nome_arquivo = "tarefas.txt"
    tarefas = carregar_tarefas_arquivo(nome_arquivo)

    while True:
        print("\nMenu:")
        print("1. Exibir Tarefas")
        print("2. Adicionar Tarefa")
        print("3. Editar Tarefa")
        print("4. Excluir Tarefa")
        print("5. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            exibir_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas)
        elif opcao == "3":
            editar_tarefa(tarefas)
        elif opcao == "4":
            excluir_tarefa(tarefas)
        elif opcao == "5":
            salvar_tarefas_arquivo(nome_arquivo, tarefas)
            print("Tarefas salvas. Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
