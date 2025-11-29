tarefas = []

def  adicionar_tarefa ():
    nova_tarefa = input("Digite a tarefa: ")
    # Cada tarefa é uma TUPLA: (descrição, estado)
    tarefa_com_estado = (nova_tarefa, "Pendente")
    tarefas.append(tarefa_com_estado)
    print("Tarefa adicionada!")

def listar_tarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
        return
    
    print("\n--- LISTA DE TAREFAS ---")
    for i in range(len(tarefas)):
        descricao, estado = tarefas[i]  # desempacota a tupla
        print(f"{i+1}. [{estado}] {descricao}")

def concluir_tarefa():
    listar_tarefas()
    
    if len(tarefas) == 0:
        return
    
    try: 
        num = int(input("Número da tarefa concluída: ")) - 1
        
        if num >= 0 and num < len(tarefas): 
            descricao, estado = tarefas[num]
            tarefas[num] = (descricao, "Concluída")
            print("Tarefa marcada como concluída!")
        else: 
            print("Número Inválido!")
    except:
        print("Digite um número válido!")

def editar_tarefa():
    listar_tarefas()
    
    if len(tarefas) == 0:
        return
    
    try: 
        num = int(input("Número da tarefa para editar: ")) - 1
        
        if num >= 0 and num < len(tarefas): 
            descricao_antiga, estado = tarefas[num]
            nova_descricao = input(f"Nova descrição (atual: {descricao_antiga}): ")
            tarefas[num] = (nova_descricao, estado)
            print("Tarefa editada com sucesso!")
        else: 
            print("Número Inválido!")
    except:
        print("Digite um número válido!")
        
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
