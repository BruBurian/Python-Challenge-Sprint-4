import cadastro

def menu_principal():
    while True:
        cria_barra()
        print("Salesforce")
        print("1. Cadastro de Usuário")
        print("2. Acesso ao CRUD de Usuários")
        print("3. Consultar e Exportar Usuários")
        print("4. Acessar Página Inicial")
        print("5. Sair")
        cria_barra()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastro.cadastrar_usuario()
        elif opcao == "2":
            submenu_crud_usuarios()
        elif opcao == "3":
            cadastro.consultar_e_exportar()
        elif opcao == "4":
            acessar_pagina_inicial()
        elif opcao == "5":
            print("Saindo...")
            exit()
        else:
            print("Opção inválida. Tente novamente.")

def submenu_crud_usuarios():
    while True:
        cria_barra()
        print("\nCRUD de Usuários")
        print("1. Listar Usuários")
        print("2. Alterar Usuário")
        print("3. Excluir Usuário")
        print("4. Voltar ao Menu Principal")
        cria_barra()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastro.listar_usuarios()
        elif opcao == "2":
            cadastro.alterar_usuario()
        elif opcao == "3":
            cadastro.excluir_usuario()
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

def acessar_pagina_inicial():
    cria_barra()
    print("\nPágina Inicial")
    print("1. Produtos")
    print("2. Indústrias")
    print("3. Suporte")
    print("4. Voltar ao Menu Principal")
    cria_barra()
   
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        Produtos()
    elif opcao == "2":
        Industrias()
    elif opcao == "3":
        Suporte()
    elif opcao == "4":
        return
    else:
        print("Opção inválida. Tente novamente.")

def Produtos():
    cria_barra()
    print("Selecione o Produto da Salesforce que deseja ver.")
    print("1. Customer 360")
    print("2. Inteligência Artificial")
    print("3. Data Cloud")
    print("4. Voltar para página inicial")
    cria_barra()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print('O Customer 360, todo o nosso portfólio de produtos, ajuda você a se conectar com seus clientes de uma maneira totalmente nova.')
        print('Para mais informações acesse: https://www.salesforce.com/br/products/')
        acessar_pagina_inicial()
    elif opcao == "2":
        print('A IA da Salesforce oferece inteligência artificial confiável e extensível, com base na estrutura da nossa plataforma Einstein 1.')
        print('Para mais informações acesse: https://www.salesforce.com/br/products/einstein-ai-solutions/')
        acessar_pagina_inicial()
    elif opcao == "3":
        print('Ative todos dados dos seus clientes nos diversos apps da Salesforce com o Data Cloud.')
        print('Para mais informações acesse: https://www.salesforce.com/br/products/data/')
        acessar_pagina_inicial()
    elif opcao == "4":
        acessar_pagina_inicial()
    else:
        print("Opção inválida. Tente novamente.")

def Industrias():
    cria_barra()
    print("Explore o Salesforce para diferentes indústrias..")
    print("1. Automotivo")
    print("2. Comunicações")
    print("3. Bens de Consumo")
    print("4. Voltar para página inicial")
    cria_barra()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print('Salesforce para o setor Automotivo, Impulsione uma vida de fidelidade!')
        print('Para mais informações acesse: https://www.salesforce.com/br/solutions/industries/automotive/overview/')
        acessar_pagina_inicial()
    elif opcao == "2":
        print('Redefina o foco da comunicação no cliente com uma plataforma flexível e escalável.')
        print('Para mais informações acesse: https://www.salesforce.com/br/solutions/industries/communications/overview/')
        acessar_pagina_inicial()
    elif opcao == "3":
        print('Salesforce para bens de consumo, Proporcione crescimento lucrativo.')
        print('Para mais informações acesse: https://www.salesforce.com/br/solutions/industries/consumer-goods/overview/')
        acessar_pagina_inicial()
    elif opcao == "4":
        acessar_pagina_inicial()
    else:
        print("Opção inválida. Tente novamente.")

def Suporte():
    cria_barra()
    print("Precisando de ajuda? Registre casos, encontre documentos e muito mais. Receba todo o suporte que você precisar, a qualquer momento..")
    print('Para mais informações acesse: https://help.salesforce.com/s/')

def cria_barra():
    print('-' * 32)

if __name__ == "__main__":
    menu_principal()
