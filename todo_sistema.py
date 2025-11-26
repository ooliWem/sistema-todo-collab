tarefas = []

def mostrar_menu(): 
    print("\n" + "=" * 25)
    print("SISTEMA TO DO - Organizador de Tarefas")
    print("=" * 25)
    print("1. Adicionar nova tarefa")
    print("2. Listar tarefas existentes")
    print("3. Marcar tarefa como concluída")
    print("4. Editar tarefa")
    print("5. Remover tarefa")
    print("6. Sair do sistema")
    print("-" * 25)

# Programa principal
print("Bem-vindo ao Sistema TO DO - Organizador de Tarefas")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        concluir_tarefa()
    elif opcao == "4": 
        editar_tarefa()
    elif opcao == "5":
        remover_tarefa()
    elif opcao == "6":
        print("Obrigado por usar o sistema!")
        break 
    else: 
        print("Opção inválida! Tente 1, 2, 3, 4, 5 ou 6.")