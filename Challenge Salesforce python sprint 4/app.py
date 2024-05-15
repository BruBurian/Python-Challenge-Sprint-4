import json
import oracle

# Função para exportar dados para JSON
def export_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Função principal para simular o site Salesforce
def main():
    connection = oracle.connect_to_oracle("<username>", "<password>", "<hostname>", "<port>", "<service_name>")

    while True:
        print("\n*** Salesforce ***")
        print("1. Inserir")
        print("2. Alterar")
        print("3. Excluir")
        print("4. Consultar")
        print("5. Exportar consulta para JSON")
        print("6. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            # Implemente a lógica para inserção de dados
            pass
        elif choice == "2":
            # Implemente a lógica para alteração de dados
            pass
        elif choice == "3":
            # Implemente a lógica para exclusão de dados
            pass
        elif choice == "4":
            # Implemente a lógica para consulta de dados
            pass
        elif choice == "5":
            # Implemente a lógica para exportar dados para JSON
            pass
        elif choice == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

    connection.close()

if __name__ == "__main__":
    main()