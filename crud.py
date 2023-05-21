def cadastro(lista_contatos):
    contato = {}
    contato["Nome"] = input("Digite o seu nome: ")
    contato["Sobrenome"] = input("Digite o seu sobrenome: ")
    contato["Telefone"] = input("Digite o seu telefone: ")
    contato["Endereco"] = input("Digite o seu endereco: ")
    contato["Email"] = input("Digite o seu email: ")
    lista_contatos.append(contato)
    print("Contato cadastrado com sucesso!")    
    
def consulta(lista_contatos):
    nome = input("Digite o nome do contado que deseja buscar: ")
    contatosEncontrados = []
    for contato in lista_contatos:
        if contato["Nome"] == nome:
            contatosEncontrados.append(contato)
        if len(contatosEncontrados) > 0:
            print("Contato(s) encontrados(s): ")
            print()
            for contato in contatosEncontrados:
               resultado = f"""
                ========================================
                                                    
                   Nome: {contato["Nome"]}          
                   Sobrenome: {contato["Sobrenome"]}
                   Telefone: {contato["Telefone"]}  
                   Endereco: {contato["Endereco"]}  
                   Email: {contato["Email"]}        
                                                    
                ========================================
                
                """
            print(resultado)
        else:
            print()
            print("Nenhum contato encontrado com esse nome.")
            
def atualizar(lista_contatos):
    nome = input("Digite o nome do contato que deseja atualizar: ")
    
    for contato in lista_contatos:
        if contato["Nome"] == nome:
               resultado = f"""
                ========================================
                   
                   Contato encontrado:
                   
                   Nome: {contato["Nome"]}          
                   Sobrenome: {contato["Sobrenome"]}
                   Telefone: {contato["Telefone"]}  
                   Endereco: {contato["Endereco"]}  
                   Email: {contato["Email"]}        
                                                    
                ========================================
                
                """
        print(resultado)

        campo = input("Digite o nome do campo que deseja atualizar (ou digite cancelar para voltar para o menu): ")

        if campo == "cancelar":
            break

        if campo in contato:
            valor = input("Digite o novo valor para o campo: ")
            contato[campo] = valor
            print("Contato atualizado com sucesso!")
        else:
            print("Campo inválido, digite novamente")

def deletar(lista_contatos):
    nome = input("Digite o nome do contato que deseja deletar: ")

    for contato in lista_contatos:
        if contato["Nome"] == nome:
            confirmacao = input("Você tem certeza? \n")
            if confirmacao.lower() == 'sim':
                lista_contatos.remove(contato)
                print("Contato deletado com sucesso!")
            else:
                break
        else:
            print("Nenhum contato encontrado com esse nome e sobrenome.")




