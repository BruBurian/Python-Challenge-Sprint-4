import database

def cadastrar_usuario():
    print("\nCadastro de Usuário")
    try:
        nome_empresa = input("Digite o nome da empresa: ")
        email = input("Digite o email: ")
        senha = input("Digite a senha: ")

        # Verificar se o email já está em uso
        usuarios = database.consultar_por_email(email)
        if usuarios:
            print("Email já cadastrado. Tente novamente.")
            return

        database.cadastrar_usuario(nome_empresa, email, senha)
        print("Usuário cadastrado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro durante o cadastro: {e}")
    finally:
        print("Cadastro concluído.")

def listar_usuarios():
    print("\nLista de Usuários:")
    try:
        usuarios = database.listar_usuarios()
        for i, usuario in enumerate(usuarios, 1):
            print(f"{i}. Nome da Empresa: {usuario[1]}, Email: {usuario[2]}")
    except Exception as e:
        print(f"Ocorreu um erro ao listar usuários: {e}")

def alterar_usuario():
    print("\nAlterar Usuário")
    try:
        listar_usuarios()
        id = int(input("Selecione o ID do usuário que deseja alterar: "))
        novo_nome = input("Novo nome da empresa: ")
        novo_email = input("Novo email: ")
        novo_senha = input("Nova senha: ")
        database.alterar_usuario(id, novo_nome, novo_email, novo_senha)
        print("Usuário alterado com sucesso!")
    except ValueError:
        print("Por favor, insira um número válido.")
    except Exception as e:
        print(f"Ocorreu um erro durante a alteração: {e}")
    finally:
        print("Alteração concluída.")

def excluir_usuario():
    print("\nExcluir Usuário")
    try:
        listar_usuarios()
        id = int(input("Selecione o ID do usuário que deseja excluir: "))
        database.excluir_usuario(id)
        print("Usuário excluído com sucesso!")
    except ValueError:
        print("Por favor, insira um número válido.")
    except Exception as e:
        print(f"Ocorreu um erro durante a exclusão: {e}")
    finally:
        print("Exclusão concluída.")

def consultar_e_exportar():
    print("\nConsultar Usuários com Filtros e Exportar")
    try:
        filtro = input("Escolha o filtro (1: Email, 2: Nome da Empresa): ")
        if filtro == '1':
            email = input("Digite o email: ")
            usuarios = database.consultar_por_email(email)
        elif filtro == '2':
            nome_empresa = input("Digite o nome da empresa: ")
            usuarios = database.consultar_por_empresa(nome_empresa)
        else:
            print("Filtro inválido.")
            return
        
        for i, usuario in enumerate(usuarios, 1):
            print(f"{i}. ID: {usuario[0]}, Nome da Empresa: {usuario[1]}, Email: {usuario[2]}")

        if usuarios:
            exportar = input("Deseja exportar os resultados para um arquivo JSON? (s/n): ")
            if exportar.lower() == 's':
                filename = input("Digite o nome do arquivo (ex: usuarios.json): ")
                data_to_export = [{"id": u[0], "nome_empresa": u[1], "email": u[2], "senha": u[3]} for u in usuarios]
                database.exportar_para_json(data_to_export, filename)
                print(f"Dados exportados para {filename} com sucesso!")
        else:
            print("Nenhum usuário encontrado com o filtro fornecido.")
    except Exception as e:
        print(f"Ocorreu um erro durante a consulta: {e}")
    finally:
        print("Consulta concluída.")
