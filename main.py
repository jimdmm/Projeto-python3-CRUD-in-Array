import crud

def menu():
    tela = """
    ==============================================
    ||                                          ||
    ||         ♣ CADASTRO DE CONTATOS ♣         ||
    ||                                          ||
    ||   Escolha uma opção:                     ||
    ||                                          ||
    ||   Cadastro - 1                           ||
    ||   Buscar - 2                             ||
    ||   Atualizar - 3                          ||
    ||   Deletar - 4                            ||
    ||   Sair - 0 ou exit                       ||
    ||                                          ||
    ==============================================    
    """
    print(tela)

contatos = []

while True:
    menu()
    opcao = input("Digite o número da opção desejada: ")
    print()
    if opcao == '1':
        crud.cadastro(contatos)
    elif opcao == '2':
       crud.consulta(contatos)
    elif opcao == '3':
        crud.atualizar(contatos)
    elif opcao == '4':
        crud.deletar(contatos)
    elif opcao == '0' or opcao.lower() == 'exit':
        print("Obrigado por usar o programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
    print()